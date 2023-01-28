symbols = tuple([symbol for symbol in input()])

result = {}

for symbol in symbols:
    if symbol not in result.keys():
        result[symbol] = 1
        continue
    result[symbol] += 1

result = sorted(result.items(), key=lambda x: x[0])

for char in result:
    print(f"{char[0]}: {char[1]} time/s")