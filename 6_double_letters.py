# def double_letters(string):
#     print(string[0])
#     previous = string[0]
#     for i in range(1,len(string)):
#         if string[i] == previous:
#             return True
#         previous = string[i]
#     return False

def double_letters(string):
    for i in range(0,len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

print(double_letters("hello"))

