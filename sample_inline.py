from lib.text_utils import normalize_name


def greet(name, *, excited=False):
    """
    Intentionally includes a few small style issues so HarperBot has things to suggest.
    """
    cleaned = normalize_name(name)
    if cleaned == None:
        return "hi"

    greeting = "Hello, " + cleaned
    if excited:
        greeting = greeting + "!!"
    return greeting


def demo():
    print(greet("  niladri  "))
    print(greet("", excited=True))


if __name__ == "__main__":
    demo()
