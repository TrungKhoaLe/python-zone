"""
Creating new functions by partially applying arguments to an existing
function. It allows us to fix or freeze some of the arguments of a
function, creating a new function with a simplified interface.
"""

import functools


def greet(greeting, name):
    return f"{greeting}, {name}"


# creating a new function with fixed arguments using partial
say_hello = functools.partial(greet, "Hello")

# call the new function
message = say_hello("K.L.")  # --> Hello, K.L.
