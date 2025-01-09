from flask import Flask, render_template
from routes.chatbot_routes import chatbot_routes
import os

# Explicitly set the templates folder
app = Flask(__name__, template_folder=os.path.join(os.getcwd(), "templates"))

# Register routes
app.register_blueprint(chatbot_routes)

@app.route("/")
def home():
    return render_template("tempor.html")

if __name__ == "__main__":
    app.run(debug=True)
