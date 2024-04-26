#!/usr/bin/env python3
""" aunthent module """

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound

import uuid


def _generate_uuid() -> str:
    """ generates unique user id """
    return str(uuid.uuid4())


def _hash_password(password: str) -> bytes:
    """ is a salted hash of the input password """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ instantiating """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ registers new users """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            user = self._db.add_user(email, _hash_password(password))
        else:
            raise ValueError("User {} already exists".format(email))
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """ ret true if email and password match e&p from db """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode("utf-8"), user.hashed_password)
