from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Securely load API key

@app.route("/", methods=["GET", "POST"])

def index():
    result = None
    image_url = None

    if request.method == "POST":
        prompt = request.form["prompt"]
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",  
                messages=[
                    {"role": "developer", "content": "You are an AI that interprets dreams based on Jungian psychology and response with 2 or 3 short sentences. Analyze the dream in terms of archetypes, symbolic figures, actions, and settings, and provide insights into their potential meanings."},
                    {"role": "user", "content": prompt}
                ],
                temperature=1.0,
                max_tokens=250
            )
            result = response.choices[0].message.content

            response = openai.images.generate(
            model="dall-e-2",
            prompt=f"A blend of surreal dreamscapes with symbolic imagery that is a representation of the dream: {prompt}",
            size="1024x1024"
            )
            image_url = response.data[0].url
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("index.html", result=result, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)  # Run locally for testing
