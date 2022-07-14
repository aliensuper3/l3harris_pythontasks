"""
convert denary numbers into base26 and back
"""

def base26(number):
    """
    converts a denary number into base26
    """
    #chr(number - 96)
    word = ""
    i = 0
    while 26 ** i <= number:
        i += 1
    while number:
        number, rem = divmod(number-1, 26)
        word += chr(rem + 97)
        #number -= ((26 ** i) * a )+ b
        i -= 1

    return word[::-1]

def unbase26(word):
    """
    converts base26 letters into a denary number
    """
    number = 0
    for i, letter in enumerate(word):
        number += (ord(letter) - 96) * 26 ** (len(word) - i - 1)
    return number


if __name__ == "__main__":
    print(unbase26("gr"))
