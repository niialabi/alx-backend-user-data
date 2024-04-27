#!/usr/bin/env python3
""" flask app imp. """

from auth import Auth
from flask import Flask, jsonify, request, abort, redirect
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


@app.route('/sessions', methods=['DELETE'])
def logout() -> str:
    """ logout function implement """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile')
def profile() -> str:
    """ responds to get profile """
    session_id = request.cookies.get('session_id')
    if not session_id:
        return abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        return abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token() -> str:
    """ Get reset password token mandatory """
    email = request.form.get('email')
    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)
    return jsonify({"email": email, "reset_token": reset_token})


@app.route('/reset_password', methods=['PUT'])
def update_password() -> str:
    """ update password """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')
    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        return abort(403)
    return jsonify({"email": email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
