def mergeDictionary(d1, d2):
    return {
        "d1": d1,
        "d2": d2
    }


x = mergeDictionary({
    "name": "Emil",
    "year": 2004
}, {
    "name": "Tobias",
    "year": 2007
}
)

print(x)
