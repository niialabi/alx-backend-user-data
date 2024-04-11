#!/usr/bin/env python3
""" filter datun function """

import re
from typing import List
import logging

logger = logging.getLogger(__name__)


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
        pattern = re.compile(f"{field}=([^;]*)")
        message = re.sub(pattern, f"{field}={redaction}", message)
    return message
