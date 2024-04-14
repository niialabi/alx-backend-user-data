#!/usr/bin/env python3
""" filter datun function """

import re
from typing import List
import logging
import os
from mysql.connector import (connection)

logger = logging.getLogger(__name__)
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
        Filters sensitive data from a message.

        Parameters:
            fields (list[str]): List of sensitive fields to be redacted.
            redaction (str): Redaction string to replace sensitive data.
            message (str): The message containing sensitive data.
            separator (str): Separator used to distinguish fields & values.

        Returns:
            str: The message with sensitive fields redacted.
    """
    for field in fields:
        escaped_field = re.escape(field)
        pattern = re.compile(fr'{escaped_field}=.*?{re.escape(separator)}')
        replacement = f'{field}={redaction}{separator}'
        message = re.sub(pattern, replacement, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ instantiating redacting formater """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ filter values in incoming log records using filter_datum """
        record.msg = filter_datum(self.fields,
                                  self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """ returns a logging.Logger object """
    user_data = logging.getLogger('user_data')
    user_data.setLevel(logging.INFO)
    user_data.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))

    user_data.addHandler(stream_handler)
    return user_data


def get_db() -> connection.MySQLConnection:
    """ returns a connector to the database """
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    database = os.getenv("PERSONAL_DATA_DB_NAME", )
    return connection.MySQLConnection(host=host,
                                      username=username,
                                      password=password,
                                      database=db_name)
