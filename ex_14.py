def getSortedKeys(dictionary):
    lst = []
    for key in dictionary:
        lst.append(key)

    lst.sort()
    return lst

x = getSortedKeys({
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964})

print(x)
