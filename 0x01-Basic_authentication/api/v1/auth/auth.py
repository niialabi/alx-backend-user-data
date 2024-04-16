#!/usr/bin/env python3
""" contains authent class """
from flask import request
from typing import List, TypeVar


class Auth():
    """ Authentication Class in app """

    def require_auth(self,
                     path: str,
                     excluded_paths: List[str]) -> bool:
        """ returns path if not excluded """
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """ get auth from flask obj """
        if request == None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user """
        if request == None:
            return None
        return None
