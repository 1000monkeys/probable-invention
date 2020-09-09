def show_magicians(magician_names):
    for magician_name in magician_names:
        print(magician_name)


def make_great(magician_names):
    i = 0
    while i < len(magician_names):
        magician_names[i] += " the Great!"
        i += 1


magician_names = ['Zabrecky, Rob', 'The Zancigs', 'Reveen, Peter', 'Ogawa, Shoot']
show_magicians(magician_names)
make_great(magician_names)
show_magicians(magician_names)
