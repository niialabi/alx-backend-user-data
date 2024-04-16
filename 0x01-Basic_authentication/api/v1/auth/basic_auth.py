#!/usr/bin/env python3
""" basic authen class modu """
from api.v1.auth.auth import Auth


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
