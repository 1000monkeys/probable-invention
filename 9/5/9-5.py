from user import User

user = User("Kjell", "Vos", "DarkRanger99", "12-12-2012")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attemptss)