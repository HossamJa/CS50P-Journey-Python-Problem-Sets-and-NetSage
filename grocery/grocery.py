items = {}
while True:
    try:
        ask = input().strip().upper()
        if ask not in items:
            items.update({ask : 1})
        else:
            num = int(items[ask]) + 1
            items.update({ask : num})
    except EOFError:
        break
result = dict(sorted(items.items()))
for x in result:
    print(result.get(x), x)
