from collections import OrderedDict

if __name__ == "__main__":
    lucky_numbers = OrderedDict()

    lucky_numbers['list'] = 'Een lijst van items.'
    lucky_numbers['value'] = 'Waarde van een variable'
    lucky_numbers['variable'] = 'Een verwijzing naar een waarde gebruikt in computer systemen. Deze waarde is veranderbaar.'
    lucky_numbers['for-loop'] = 'Een loop doe een bepaald aantal keren gedaan word.'
    lucky_numbers['ik heb geen nieuwe woorden geleerd'] = 'Hoop dat het boek snel moeilijker word.'
    lucky_numbers['sleutel1'] = 'informatie1'
    lucky_numbers['sleutel2'] = 'informatie2'
    lucky_numbers['sleutel3'] = 'informatie3'
    lucky_numbers['sleutel4'] = 'informatie4'
    lucky_numbers['sleutel5'] = 'informatie5'

    for key, value in lucky_numbers.items():
        print(str(key) + ":\n" + str(value) + "\n\n")
