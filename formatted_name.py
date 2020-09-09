def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name =  first_name + " " + last_name
    return full_name.title()

if __name__ == "__main__":
    musician = get_formatted_name('jimi', 'hendrix')
    print(musician)
