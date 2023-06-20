def mid(string):
    if len(string) % 2:
        return string[len(string)//2]
    return ""

print(mid("abc"))


def efficient_mid(string):
    return string[len(string)//2] if len(string) % 2 else ""

print(efficient_mid("abc"))
