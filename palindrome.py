def palindrome(word):
    if(not(len(word) % 2 == 0)):
        newword = ""
        for i, letter in enumerate(word):
            if(not(i == (int)(len(word) / 2))):
                newword += (letter)
        word = newword

    for i in range((int)(len(word) / 2)):
        if(not(word[i] == word[(int)("-" + (str)(i+1))])):
            return False
    return True


def palindrome2(word):

    for i in range((int)(len(word) / 2)):
        if(not(word[i] == word[(int)("-" + (str)(i+1))])):
            return False
    return True

print(palindrome2("12344321"))

def py_palindrome(word):
    return word == word[::-1]

print(py_palindrome("jhgjgjhf"))