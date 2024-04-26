#!/usr/bin/env python3
""" aunthent module """

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from typing import Union

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

    def create_session(self, email: str) -> str:
        """ creates session id for user """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """ Get user email from session_id if session is active """
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ destry session """
        if user_id:
            self._db.update_user(user_id, session_id=None)
