from user import User

class Administrator(User):
    def __init__(self, first_name, last_name, username, date_of_birth):
        super(Administrator, self).__init__(first_name, last_name, username, date_of_birth)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.privileges)
