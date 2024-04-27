#!/usr/bin/env python3
"""  End-to-end integration main test"""

from auth import Auth
import requests

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"
BASE_URL = "http://127.0.0.1:5000"


def register_user(email: str, password: str) -> None:
    """Register a new user with the given email and password."""
    pass


def log_in_wrong_password(email: str, password: str) -> None:
    """Attempt to log in with the provided email and an incorrect password."""
    pass


def profile_unlogged() -> None:
    """Access the profile endpoint without auth, expecting a 403 error."""
    pass


def log_in(email: str, password: str) -> str:
    """Log in using the provided email and password, ret the ses ID."""
    return None


def profile_logged(session_id: str) -> None:
    """Access the profile endpoint with a valid session ID."""
    pass


def log_out(session_id: str) -> None:
    """Log out the user identified by the provided session ID."""
    pass


def reset_password_token(email: str) -> str:
    """Request a password reset token for the given email."""
    return None


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    Update the password associated with the provided email using the given
    reset token and new password.
    """
    pass


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
