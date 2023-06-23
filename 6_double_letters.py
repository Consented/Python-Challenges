def double_letters(string):
    for i in range(0,len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

print(double_letters("hello"))


def efficient_double_letters(string): #Thanks for the help explaining this!
    return any([a == b for a, b in zip(string, string[1:])])#zip goes through the strings adding each letter to a tuple, this is then compared if they are both
# the same letter and adding to a list of booleans values, any then checks if any are true

print(efficient_double_letters("hello"))
