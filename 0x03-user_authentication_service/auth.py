#!/usr/bin/env python3
""" aunthent module """

import bcrypt


def _hash_password(password: str) -> bytes:
    """ is a salted hash of the input password """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
