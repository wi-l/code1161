"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
<<<<<<< HEAD
from __future__ import division
from __future__ import print_function
import os

print("hello! Let's get started")
jobs = ['get', 'this', 'file', 'to', 'pass', 'the', 'linter']
InOtherWords = "make it show no linter errors"
print(jobs)
print(InOtherWords)
print(1 + 1, "is smaller than", 7*0.5, "is", (1+1) < (7*0.5),
      ", which is a relief!")


def usefulFunction():
    print(os.getcwd())

=======
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']

for word in some_words:
    print(word)

for x in some_words:
    print(x)

print(some_words)

if len(some_words) > 3:
    print('some_words contains more than 3 words')

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())
>>>>>>> 15366771d4183b7eb1e2eae13cf4191fd51992e2

usefulFunction()
