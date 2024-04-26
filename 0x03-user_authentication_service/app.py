#!/usr/bin/env python3
""" flask app imp. """

from auth import Auth
from flask import Flask, jsonify, request, abort
app = Flask(__name__)

AUTH = Auth()


@app.route('/')
def hello_main() -> str:
    """ jasonify dict """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users() -> str:
    """ endpoint to register users """
    email, password = request.form.get("email"), request.form.get("password")
    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": f'{email}', "message": "user created"})


@app.route('/sessions', methods=['POST'])
def login() -> str:
    """ log in function """
    email, password = request.form.get("email"), request.form.get("password")
    if not AUTH.valid_login(email, password):
        abort(401)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", AUTH.create_session(email))
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
