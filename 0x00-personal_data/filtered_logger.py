#!/usr/bin/env python3
"""Regex-ing"""

from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Return the log message obfuscated"""
    for field in fields:
        message = re.sub("{}=(.*?){}".format(field, separator), "{}={}{}"
                         .format(field, redaction, separator), message)
    return message
