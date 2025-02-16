# report
This web application uses AI to interpret dreams based on Jungian psychological principles. Once a dream has been prompted by a user, the app uses OpenAI’s gpt-4o-mini, and DALL-E-2 model to generate a textual analysis and an image that embodies the symbolic of the dream, respectively. This is done through a web interface build using flask, where the user’s entry is sent to OpenAI API for processing. This part is done with a specific message that include, two roles, a temperature, and a maximum of tokens allowed for processing. First, the developer role specifies to the API what is supposed to be done with the information it receives, i.e. interpret the prompt through a Jungian psychology lense. Second the information to be analysed, i.e. the user prompt. Third, set temperature of 1.0, for its probability for randomness. And lastly, a maximum token size of 250. This is responsible of capping the number of tokens generated in the completion of the task. Although, this does not imply that all answers will use 250 tokens for their generation. The app is also using an OpenAI service in DALL-E-2 to generate an image corresponding to the dream. This is also done through a general prompt that includes the suer prompt in itself. Specifying a canvas size of 1024x1024 pixels to the model, the flask app sent this general prompt to the OpenAI API similarly to the text generation.

The implementation of Jungian Psychology in the dream analysis includes key concepts such as archetypes and symbolic, that are easily found in Jung’s framework. Ideally, these concepts will provide insight to the dream prompted. This, paired with the DALL-E generated imagery, offers a unique interoperation of the user’s imagination. 

However, the web app can surely be improved. First there is no customization, meaning that the suer can’t specify what specific aspect of the Jungian analysis should be used to explore their dream. Meaning that the user could interreact with the developer role, and not only the user. Moreover, a higher maximum amount of token could be allocated for the analysis, thus helping the clarity and the quality of it. Finally, a better model for the imagery, such as DALL-E-3, could be used to illustrate the dream. A better model could be more detailed and more cohesive with the text generated analysis.

# minimal-flask-app
Minimal code for Flask app making calls to the OpenAI API

```
# Create virtual environment
python3 -m venv ./venv

# Activate your virtual environment
source venv/bin/activate

# Install the required packages. For example
pip3 install flask openai python-dotenv

# Rename the file .env-bup to .env 
# Add your OPENAI_API_KEY to the .env file.

# Run the app
python3 app.py
```