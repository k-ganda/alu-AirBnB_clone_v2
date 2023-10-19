#!/usr/bin/python3


"""Script to start a Flask web application."""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """Route handler for the root URL ("/").

    Returns:
        str: The string "Hello HBNB!".
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Route handler for the "/hbnb" URL.

    Returns:
        str: The string "HBNB".
    """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Route handler for the "/c/<text>" URL.

    Args:
        text (str): The text parameter extracted from the URL.

    Returns:
        str: The modified string with underscores replaced by spaces and prefixed with "C ".
    """
    text = text.replace("_", " ")
    return f"C {text}"

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Route handler for the "/python" and "/python/<text>" URLs.

    Args:
        text (str, optional): The text parameter extracted from the URL. Defaults to "is cool".

    Returns:
        str: The modified string with underscores replaced by spaces and prefixed with "Python ".
    """
    text = text.replace("_", " ")
    return f"Python {text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
