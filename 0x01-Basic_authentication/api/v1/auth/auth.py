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
        if path is None or not excluded_paths:
            return True

        path = path.rstrip('/')

        for excluded_path in excluded_paths:
            excluded_path = excluded_path.rstrip('/')
            if path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ get auth from flask obj """
        if not request:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user """
        if not request:
            return None
        return None
