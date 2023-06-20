def capital_indexes(string):
    capital_index = []
    for i in range(len(string)):
        if ord(string[i]) >= 65 and ord(string[i]) <= 90:
            capital_index.append(i)
    return capital_index

print(capital_indexes("HeLlO"))


def efficient_capital_indexes(string):
    return capital_index = [i for i in range(len(string)) if ord(string[i]) >= 65 and ord(string[i]) <= 90]

print(efficient_capital_indexes("HeLlO"))
