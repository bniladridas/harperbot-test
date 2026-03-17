import re


USERNAME_RE = re.compile(r"^[a-z0-9_\\-]{3,32}$")


def is_valid_username(username):
    if username is None:
        return False
    return USERNAME_RE.match(username) is not None

