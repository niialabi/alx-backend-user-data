#!/usr/bin/env python3
""" flask app imp. """

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def hello_main():
    """ jasonify dict """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
