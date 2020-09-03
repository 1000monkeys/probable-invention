if __name__ == "__main__":
    rivers = {
        'nile': 'egypt',
        'limpopo': 'mozambique',
        'okavango': 'angola',
        'gambia': 'gambia'
    }

    for name in sorted(set(rivers.keys())):
        print(name)

    for value in sorted(set(rivers.values())):
        print(value)
