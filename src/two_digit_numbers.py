"""
filter out 2 digit numbers from a list of type str of any length
"""

def two_digit_numbers(list_):
    newlist = []
    for value in list_:
        if "-" in value:
            if not len(value) == 3:
                newlist.append(value)
        else:
            if not len(value) == 2:
                newlist.append(value)
    return newlist


if __name__ == "__main__":
    list_ = []
    list_ = ["13", "4", "-4", "563", "27", "-57", "8"]
    print(two_digit_numbers(list_))

# iminus = 0
# for i in range(len(list_)):
#     print(f"temp {temp}")
#     if("-" in temp):
#         if(len(temp) == 3):
#             list_.remove(list_[i-iminus])
#             iminus+=1
#     else:
#         if(len(temp) == 2):
#             list_.remove(list_[i-iminus])
#             iminus+=1
#     print((str)("-" in temp))