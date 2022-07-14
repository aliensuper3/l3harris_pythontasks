

def base26(number):
    #chr(number - 96)
    word = ""
    
    i = 0
    while(26 ** i <= number):
        i += 1
    while(number):
        number, b = divmod(number-1, 26)
        word += chr(b + 97)
        #number -= ((26 ** i) * a )+ b
        i -= 1

    return word[::-1]

def unbase26(word):
    number = 0
    for i, letter in enumerate(word):
        number += (ord(letter) - 96) * 26 ** (len(word) - i - 1)
    return number

print(unbase26("gr"))