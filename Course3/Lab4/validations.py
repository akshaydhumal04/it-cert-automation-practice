#!/usr/bin/env python3

import re

def validate_user(username, min_length):
    # Check if the username meets the minimum length requirement
    if len(username) < min_length:
        return False

    # Check if the username starts with a letter and contains only alphanumeric characters
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9]*$', username):
        return False

    return True

# Test cases
print(validate_user("blue.kale", 3))    # True
print(validate_user(".blue.kale", 3))   # False
print(validate_user("red_quinoa", 4))   # True
print(validate_user("_red_quinoa", 4))  # False

