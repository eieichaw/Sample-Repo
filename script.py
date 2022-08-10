import math
from os import rename
import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    """
    Greeting to the user
    """
    greeting = f"Hello, {who_to_greet}"
    return greeting


r = requests.get("https://google.com")
print(r.status_code)
