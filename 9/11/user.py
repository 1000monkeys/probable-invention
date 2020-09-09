class User:
    def __init__(self, first_name, last_name, username, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.date_of_birth = date_of_birth
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name + " " + self.last_name)
        print("Goes by " + self.username)
        print("Born on " + self.date_of_birth)

    def greet_user(self):
        print("Hello " + self.first_name + " " + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Administrator(User):
    def __init__(self, first_name, last_name, username, date_of_birth):
        super(Administrator, self).__init__(first_name, last_name, username, date_of_birth)
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.privileges)