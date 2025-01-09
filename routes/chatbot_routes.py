from flask import Blueprint, request, jsonify
import openai
import os
from dotenv import load_dotenv
from utils.quiz_utils import quiz_questions
from utils.openai_utils import query_dynamic_generation, format_code_block
from response import predefined_responses

# Load environment variables
load_dotenv()

# Initialize OpenAI API
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set!")

openai.api_key = openai_api_key

# Define a Blueprint for chatbot routes
chatbot_routes = Blueprint("test_hugging_face", __name__)

# Maintain a history for context-aware responses
history = [
    {"role": "system", "content": "You are a Python programming tutor and assistant."}
]

quiz_state = {}  # Initialize quiz state



def add_to_history(role, content):
    history.append({"role": role, "content": content})
    if len(history) > 5:  # Limit to the last 5 exchanges
        history.pop(1)


@chatbot_routes.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json.get("user_input", "").strip()

    if not user_input:
        return jsonify({"reply": "Please provide a valid input."})

    # Normalize user input
    user_input_normalized = user_input.lower()

    # Check if the input explicitly asks for an explanation or dynamic query
    if "explain" in user_input_normalized or "describe" or "what" in user_input_normalized:
        try:
            # Handle dynamic query generation for explanations
            add_to_history("user", user_input)
            chatbot_reply = query_dynamic_generation(user_input)
            add_to_history("assistant", chatbot_reply)
            chatbot_reply = format_code_block(chatbot_reply)
            return jsonify({"reply": chatbot_reply})
        except Exception as e:
            return jsonify({"reply": f"Error: {str(e)}"})

    # Check predefined responses for exact match (if no explanation keyword is found)
    if user_input_normalized in predefined_responses:
        chatbot_reply = predefined_responses[user_input_normalized]
        chatbot_reply = format_code_block(chatbot_reply)
        return jsonify({"reply": chatbot_reply})

    # Extract keywords for predefined responses
    keyword = extract_keywords(user_input_normalized)

    if keyword and keyword in predefined_responses:
        chatbot_reply = predefined_responses[keyword]
        chatbot_reply = format_code_block(chatbot_reply)
        return jsonify({"reply": chatbot_reply})

    # Fallback to dynamic query generation if no match is found
    try:
        add_to_history("user", user_input)
        chatbot_reply = query_dynamic_generation(user_input)
        add_to_history("assistant", chatbot_reply)
        chatbot_reply = format_code_block(chatbot_reply)
        return jsonify({"reply": chatbot_reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})



@chatbot_routes.route("/clear_history", methods=["POST"])
def clear_history():
    """
    Clears the conversation history and resets quiz state.
    """
    global history
    history = [
        {"role": "system", "content": "You are a Python programming tutor and assistant."}
    ]
    quiz_state.clear()  # Clear quiz state if any
    return jsonify({"reply": "Chat history cleared!"})


# Route: Start Quiz
@chatbot_routes.route("/start_quiz", methods=["POST"])
def start_quiz():
    """
    Initializes or resets the quiz for the user based on the selected difficulty level.
    """
    user_id = request.json.get("user_id", "default")
    level = request.json.get("level", "beginner")  # Default to beginner level

    # Reset quiz state if level changes or new quiz is started
    if user_id not in quiz_state or quiz_state[user_id].get("level") != level:
        quiz_state[user_id] = {
            "current": 0,
            "level": level,
            "questions": quiz_questions.get(level, []),
            "score": 0  # Reset score when starting a new quiz
        }

    state = quiz_state[user_id]

    # Check if there are more questions available
    if state["current"] < len(state["questions"]):
        current_question = state["questions"][state["current"]]
        return jsonify({"question": current_question["question"], "options": current_question["options"]})
    return jsonify({"reply": "Quiz finished! Great job!"})


# Route: Submit Answer
@chatbot_routes.route("/submit_answer", methods=["POST"])
def submit_answer():
    """
    Handles the user's answer, adjusts the score, and returns the next question or completion message.
    """
    user_id = request.json.get("user_id", "default")
    answer = request.json.get("answer", "").strip()
    state = quiz_state.get(user_id, {})
    time_up = request.json.get("timeUp", False)

    if not state:
        return jsonify({"reply": "No active quiz found. Start a quiz first."})

    current_index = state.get("current", 0)
    questions = state.get("questions", [])

    if current_index >= len(questions):
        return jsonify({"reply": f"Quiz completed! Final Score: {state.get('score', 0)}. Great job!"})

    correct_answer = questions[current_index]["answer"].strip()

    # Adjust the score based on the user's answer and timeUp flag
    if not time_up:
        if answer.lower() == correct_answer.lower():
             state["score"] += 10  # Add 10 points for a correct answer
             feedback = f"Correct! +10 points. Your current score: {state['score']}."
        else:
            state["score"] -= 5  # Deduct 5 points for an incorrect answer
            feedback = f"Incorrect! The correct answer was: {correct_answer}. -5 points. Your current score: {state['score']}."
    else:
        feedback = f"Time's up! The correct answer was: {correct_answer}. No points awarded."
    # Move to the next question
    state["current"] += 1

    # Check if there are more questions available
    if state["current"] < len(questions):
        next_question = questions[state["current"]]
        return jsonify({
            "reply": feedback,
            "next_question": next_question["question"],
            "options": next_question["options"],
            "score": state["score"]
        })
    else:
        return jsonify({
            "reply": f"{feedback} Quiz completed! Final Score: {state['score']}. Great job!",
            "score": state["score"]
        })


@chatbot_routes.route("/debug_quiz_state", methods=["GET"])
def debug_quiz_state():
    return jsonify(quiz_state)


def normalize_answer(answer):
    """
    Normalize the answer for case-insensitive and whitespace-insensitive matching.
    """
    import re
    # Remove extra spaces and make case-insensitive
    return re.sub(r"\s+", " ", answer.strip().lower())


def extract_keywords(user_input):
    """
    Extract keywords from user input to match predefined responses.
    """
    user_input_normalized = user_input.lower().strip()
    keywords = ["product", "fibonacci", "count characters", "add", "factorial", "if-else", "if else", "bubble sort example", "indentation error example", "path", "quiz"]
    for keyword in keywords:
        if keyword in user_input_normalized:
            return keyword
    return None




