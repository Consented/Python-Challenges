statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(statuses):
    count = 0
    for x,y in statuses.items():
        if y == "online":
            count += 1
    return count

print(online_count(statuses))

