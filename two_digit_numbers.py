"""
filter out 2 digit numbers from a list of type str of any length
"""
list_ = []
list_ = ["13", "4", "-4", "563", "27", "-57", "8"]
newlist = []
print(list_)

for value in list_:
    if "-" in value:
        if not len(value) == 3:
            newlist.append(value)
    else:
        if not len(value) == 2:
            newlist.append(value)


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

print(newlist)
