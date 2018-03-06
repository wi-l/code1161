"""Correct the syntax in this file.

This file doesn't run yet.
Go through it and change it until it runs.
"""
import string


def getLetter(index):
    alphabet = string.ascii_lowercase + " "
    return alphabet[index]


<<<<<<< HEAD
def week2exersise2():
    indices = [12, 2, 26, 7, 0, 12, 12, 4, 17]
    wordArray = list(map(getLetter, indices))
    wordArray[0] = wordArray[0].upper()
    wordArray[1] = wordArray[1].upper()
    wordArray[3] = wordArray[3].upper()
    secret_word = "".join(wordArray)
=======
def week2exersise2();
    indices = [12: 2, 26, 7, 0, 12, 12, 4, 17]
    wordArray = {}  # hint: should this be a dictionary?
    for index in indices:
        wordArray.append[getLetter(index)]

    wordArray(0) = wordArray[0].upper()
    wordArray{1} = wordArray[1].upper()
    wordArray[3} = wordArray[3].upper{}
    secret_word="".join(wordArray)
>>>>>>> 15366771d4183b7eb1e2eae13cf4191fd51992e2
    print(secret_word)
    return secret_word


if __name__ == "__main__":
    print(week2exersise2())
