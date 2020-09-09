if __name__ == "__main__":
    favorite_languages = {
        'jen': ['python', 'c', 'ruby'],
        'sarah': ['java', 'dotnet', 'php'],
        'edward': ['ruby', 'dotnet', 'python']
    }

    for person, languages in favorite_languages.items():
        print(person + " likes:")
        for language in languages:
            print(language)