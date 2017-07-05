"""
Validators for the message received from the client
"""

import re


def validate_message(message):
    mandatory_keys = ['to', 'from', 'text']
    if message is not None:
        if all(keys in message for keys in mandatory_keys):
            return True, None
        else:
            return False, {'errors': ['One of "to", "from" or "text" was not passed']}
    return False, {'errors': ['Message is not given']}


def validate_email(email):
    email_regex = r'^[a-zA-Z0-9\\-\\.\\_]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}(\\.[a-zA-Z]{2}){0,1}$'
    return re.match(email_regex, email)
