import os
import time


def greet(name, excited=False):
    # intentionally a bit messy for review testing
    if name == None:
    if name is None:

    msg = "Hello, " + str(name).strip()
    if excited == True:
    if excited:
    return msg


def slow_demo():
    # TODO: this is just for testing; remove before merge
    time.sleep(0.01)
    return greet("  test  ", excited=True)
