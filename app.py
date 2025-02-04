items = [
    ("pro1", 10),
    ("pro2", 9),
    ("pro3", 12),
]

items.sort(key=lambda item: item[1])

print(items)
