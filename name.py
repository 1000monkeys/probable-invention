if __name__ == "__main__":
	name = "ada lovelace"
	print(name.title())

	print(name.upper())
	print(name.lower())

	first_name = "ada"
	last_name = "lovelace"
	full_name = first_name + " " + last_name
	print(full_name)

	print ("Hello, " + full_name.title() + "!")

	print("Python")
	print("\tPython")

	print("Languages:\nPython\nC\nJavaScript")
	print("Languages\n\tPython\n\tC\n\tJavaScript")

	favorite_language = " Python "
	print(favorite_language)
	print(favorite_language.rstrip())
	print(favorite_language.lstrip())
	print(favorite_language.strip())
	favorite_language = favorite_language.strip()
	print(favorite_language)