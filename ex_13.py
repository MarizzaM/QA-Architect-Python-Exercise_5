def tryGetValue(dictionary, key):
    value = dictionary.get(key)

    if value != '':
        return value
    else:
        return None


x = tryGetValue({
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}, "model")

print(x)
