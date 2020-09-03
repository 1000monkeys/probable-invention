if __name__ == "__main__":
    lucky_numbers = {
        'list': 'Een lijst van items.',
        'value': 'Waarde van een variable',
        'variable': 'Een verwijzing naar een waarde gebruikt in computer systemen. Deze waarde is veranderbaar.',
        'for-loop': 'Een loop doe een bepaald aantal keren gedaan word.',
        'ik heb geen nieuwe woorden geleerd': 'Hoop dat het boek snel moeilijker word.',
        'sleutel1': 'informatie1',
        'sleutel2': 'informatie2',
        'sleutel3': 'informatie3',
        'sleutel4': 'informatie4',
        'sleutel5': 'informatie5'
    }

    for key, value in lucky_numbers.items():
        print(str(key) + ":\n" + str(value) + "\n\n")
