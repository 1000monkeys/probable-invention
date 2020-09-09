from user import User
from privileges import Privileges

class Administrator(User):
    def __init__(self, first_name, last_name, username, date_of_birth):
        super(Administrator, self).__init__(first_name, last_name, username, date_of_birth)
        self.privileges = Privileges()
