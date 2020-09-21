from pygal_maps_world import i18n


def get_country_code(country_name):
    """Return the Pygal 2 digit country code for the given country."""

    for code, name in i18n.COUNTRIES.items():
        if name == country_name:
            return code

    # Fix missing country codes
    if country_name == 'Yemen, Rep.':
        return 'ye'
    elif country_name == 'Virgin Islands (U.S.)':
        return 'vi'
    elif country_name == 'Vietnam':
        return 'vn'
    elif country_name == 'Trinidad and Tobago':
        return 'tt'
    elif country_name == 'Tanzania':
        return 'tz'
    elif country_name == 'Tonga':
        return 'to'
    elif country_name == 'Moldova':
        return 'md'
    elif country_name == 'Libya':
        return 'ly'
    elif country_name == 'Kosovo':
        return 'xk'

    # If the country wasn't found, return None.
    return None
