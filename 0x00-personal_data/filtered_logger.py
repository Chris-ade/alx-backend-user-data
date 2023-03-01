#!/usr/bin/env python3
"""
A module containing a function filter_datum that returns an obfuscated log message.
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    A function that obfuscates the specified fields in the given message.

    Args:
        fields (List[str]): A list of strings representing all fields to obfuscate.
        redaction (str): A string representing by what the field will be obfuscated.
        message (str): A string representing the log line.
        separator (str): A string representing by which character is separating all fields in the log line (message).

    Returns:
        str: The obfuscated log message.

    """
    return re.sub(fr"(?<={separator})\s*({'|'.join(fields)})=[^;]+", f" {redaction}", message)
