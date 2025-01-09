import openai
history = [
    {"role": "system", "content": "You are a Python programming tutor and assistant."}
]

def query_dynamic_generation(user_input):
    """
    Adjusts response verbosity based on query type.
    """
    # Check for keywords to determine verbosity
    if "explain" in user_input.lower() or "describe" in user_input.lower():
        prompt = f"""
        You are a Python tutor.Only answer questions related to Python programming and its libraries. Provide a concise explanation for the query, avoiding unnecessary details. 
        Focus on delivering the main point clearly and briefly.

        Query: {user_input}
        Response:
        """
    elif "example" in user_input.lower() or "code" in user_input.lower():
        prompt = f"""
        You are a Python tutor.Only answer questions related to Python programming and its libraries. Provide a detailed code example for the query, formatted properly for readability with simple explanation. 
        Avoid lengthy explanations; focus on the code.

        Query: {user_input}
        Response:
        """
    else:
        prompt = f"""
        You are a Python tutor.Only answer questions related to Python programming and its libraries. Provide a brief response that directly addresses the user's query.

        Query: {user_input}
        Response:
        """

    # Generate response using OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=history + [{"role": "user", "content": prompt}],  # Add the prompt to the message history
        temperature=0.5,
        max_tokens=500  # Ensure sufficient length for detailed code examples
    )
    return response.choices[0].message["content"].strip()


def format_code_block(response):
    """
    Formats code blocks for proper HTML rendering.
    """
    response = response.replace("```python", "<pre><code>").replace("```", "</code></pre>")
    response = response.replace("\n", "<br>")
    return response

