Interactive Python Chatbot

📚 Overview

The Interactive Python Chatbot is a Flask-based web application designed to teach Python concepts interactively. Users can:

Ask Python-related questions and get detailed explanations.

View code examples for better understanding.

Test their Python knowledge with a fun quiz, complete with scoring and a timer.

This project is a part of my application challenge to build a fully functional and responsive chatbot using OpenAI API, Flask, and Hugging Face for deployment.


🚀 Features

Dynamic Chatbot: Answers Python-related queries using a combination of predefined responses and dynamic query generation via OpenAI API.

Interactive Quiz: Quizzes across beginner, intermediate, and advanced levels with scoring (+10 for correct answers, -5 for incorrect).

Timer: Each quiz question has a timer to challenge users.

Mobile Responsiveness: Optimized for desktop and mobile views.

Deployment: Deployed on Hugging Face Spaces using Docker for containerized application management.


🛠️ Tech Stack

Backend: Python, Flask

Frontend: HTML, CSS, JavaScript

API: OpenAI API for dynamic responses

Deployment: Hugging Face Spaces with Docker


Libraries:

flask

openai 

dotenv

requests

📂 Project Structure



Interactive_Python_Chatbot/

├── app.py                 # Main application file

├── routes/

│   ├── chatbot_routes.py  # Flask routes for chatbot and quiz logic

├── templates/

│   ├── tempor.html        # HTML file for the web interface

├── static/

│   ├── tempor.css         # CSS file for styling

├── requirements.txt       # Project dependencies

├── .env                   # Environment variables (e.g., OpenAI API key)

├── Dockerfile             # Docker configuration for deployment

└── README.md              # Project documentation


⚙️ Setup Instructions

1️⃣ Clone the Repository

git clone https://github.com/yourusername/Interactive_Python_Chatbot.git

cd Interactive_Python_Chatbot


2️⃣ Install Dependencies

Ensure you have Python 3.9+ installed. Then, run:

pip install -r requirements.txt


3️⃣ Configure Environment Variables

Create a .env file in the project root:

OPENAI_API_KEY=your_openai_api_key


4️⃣ Run the Application

Start the Flask app locally:

python app.py

Visit the app at http://127.0.0.1:5000.


🐳 Deploy with Docker

Build the Docker image:

docker build -t interactive-python-chatbot .

Run the Docker container:

docker run -p 5000:5000 interactive-python-chatbot

Access the app at http://127.0.0.1:5000.


🌐 Live Demo

Try the live version on Hugging Face Spaces:

https://huggingface.co/spaces/Kiruthikaramalingam/Interactive_Python_Chatbot1

📝 Future Improvements


Add more Python-related quiz questions and levels.

Enhance the chatbot interface for better user experience.

Integrate links to official Python documentation.

Improve mobile responsiveness and UI design.


🤝 Contributing

Contributions are welcome! Please open an issue or create a pull request for any changes or suggestions.


📧 Contact

Feel free to reach out for feedback or collaboration:

Email:kiruthikaramalingam@gmail.com

LinkedIn:www.linkedin.com/in/kiruthika-ramalingam-39b3011b
