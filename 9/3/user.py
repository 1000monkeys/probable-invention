class User:
    def __init__(self, first_name, last_name, username, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.date_of_birth = date_of_birth

    def describe_user(self):
        print(self.first_name + " " + self.last_name)
        print("Goes by " + self.username)
        print("Born on " + self.date_of_birth)

    def greet_user(self):
        print("Hello " + self.first_name + " " + self.last_name)
