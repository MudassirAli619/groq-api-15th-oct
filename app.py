# This line imports a library, like a toy box, called Flask to help us make our web app.
from flask import Flask, jsonify

# This makes a new app, just like starting a new game or story.
app = Flask(__name__)

# This is a pretend key to talk to Groq, like a magic password.
GROQ_API_KEY = "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"

# This is our main route, like a road where people can visit to see our results.
@app.route('/data')
def get_data():
    # Pretend we got this info from Groq’s API
    data = {"info": "Groq says hello!"}
    # We turn our data into a package to send over the internet.
    return jsonify(data)

# This says, “Let’s start the game!” when we run this code.
if __name__ == '__main__':
    app.run(debug=True)
