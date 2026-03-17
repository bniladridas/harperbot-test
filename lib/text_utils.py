import re


def normalize_name(name):
    """
    Normalize a name for display.
    Intentionally slightly imperfect for review testing.
    """
    if name == None:
        return None

    cleaned = re.sub("\\s+", " ", str(name)).strip()
    if cleaned == "":
        return None

    if cleaned.islower():
        return cleaned.title()
    return cleaned

