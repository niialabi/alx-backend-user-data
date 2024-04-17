#!/usr/bin/env python3
""" basic authen class modu """
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """ BasicAuth that inherits from Auth """

    def extract_base64_authorization_header(
                                            self,
                                            authorization_header: str) -> str:
        """  returns Base64 part of the Authorization header """
        if not authorization_header:
            return None
        if not isinstance(authorization_header, str):
            return None
        auth_header_list = authorization_header.split(" ")
        if auth_header_list[0] != "Basic":
            return None
        else:
            return auth_header_list[1]

    def decode_base64_authorization_header(
                                           self,
                                           base64_authorization_header:
                                           str) -> str:
        """ returns the decoded value of a Base64 string """
        if not base64_authorization_header:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            return base64.b64decode(base64_authorization_header
                                    .encode()).decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ ret user email and password from the Base64 decoded value """
        if not decoded_base64_authorization_header:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        credential_list = decoded_base64_authorization_header.split(":")
        return (credential_list[0], credential_list[1])

    def user_object_from_credentials(self, user_email: str, user_pwd:
                                     str) -> TypeVar('User'):
        """ returns the User instance """
        if not user_email or not isinstance(user_email, str):
            return None
        if not user_pwd or not isinstance(user_pwd, str):
            return None
        try:
            user = User.search({'email': user_email})
        except KeyError:
            return None
        if not user or not user[0].is_valid_password(user_pwd):
            return None
        return user[0]
