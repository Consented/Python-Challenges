def capital_indexes(string):
    capital_index = []
    for i in range(len(string)):
        if ord(string[i]) >= 65 and ord(string[i]) <= 90:
            capital_index.append(i)
    return capital_index

print(capital_indexes("HeLlO"))


