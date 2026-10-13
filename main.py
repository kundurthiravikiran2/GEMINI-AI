from flask import Flask, request, render_template_string
from google import genai
import os

app = Flask(__name__)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

HTML = """
<!DOCTYPE html>

<html>

<head>

    <title>Gemini AI DevOps Assistant</title>

    <style>

        body {
            font-family: Arial;
            background: #f4f4f4;
            margin: 0;
            padding: 0;
        }

        .container {
            width: 70%;
            margin: 50px auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
        }

        h1 {
            text-align: center;
        }

        textarea {
            width: 100%;
            height: 150px;
            padding: 10px;
            font-size: 16px;
        }

        button {
            width: 100%;
            padding: 15px;
            margin-top: 15px;
            background: #4285f4;
            color: white;
            border: none;
            font-size: 18px;
            cursor: pointer;
        }

        .response {
            margin-top: 25px;
            padding: 20px;
            background: #eeeeee;
            white-space: pre-wrap;
        }

    </style>

</head>

<body>

<div class="container">

    <h1>🤖 Gemini AI DevOps Assistant</h1>

    <form method="POST">

        <textarea
            name="question"
            placeholder="Ask a DevOps question..."></textarea>

        <button type="submit">
            Ask Gemini
        </button>

    </form>

    {% if answer %}

    <div class="response">

        <h2>Gemini Response</h2>

        {{ answer }}

    </div>

    {% endif %}

</div>

</body>

</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""

    if request.method == "POST":

        question = request.form["question"]

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=question
        )

        answer = response.text

    return render_template_string(
        HTML,
        answer=answer
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )

