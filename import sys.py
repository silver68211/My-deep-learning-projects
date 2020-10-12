import math
import os
import sys

print(sys.version)
print(sys.executable)


def greet(how_to_greet):
    greeting = "Hello {}".format(how_to_greet)
    return greeting


print(greet("World!"))
