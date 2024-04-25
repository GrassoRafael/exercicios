# users
class User:
    """Greetings to a user"""

    def __init__(self, first_name, last_name, login_attempt=0):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.login_attempt = login_attempt
        print("Welcome to the site, please enter your information, you have three chances to log in or you "
              "will be temporarily blocked")


    def describe_user(self):
        """Describe the user first and last name"""
        print(f"Your first name is: {self.first_name}\nYour last name is: {self.last_name}")

    def greet_user(self):
        """Greet a user by stating your first and last name"""
        print(f"Greetings {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        """Increase the number of login attempts by 1"""
        if self.login_attempt < 3:
            self.login_attempt += 1
            print(f"Number of login attempt {self.login_attempt}")

        else:
            print("You are blocked for 1 minute")

    def reset_login_attempts(self):
        """Reset the login attempts"""
        self.login_attempt = 0
        print("Your login attempts have been reset")


user = User("rafael", "grasso")
user.increment_login_attempts() # Tentativa um
user.increment_login_attempts() # Tentativa dois
user.increment_login_attempts() # Tentativa tres
user.increment_login_attempts() # Bloqueio

print()
user.reset_login_attempts() # Resetando tentativas
print(f"Login attempts: {user.login_attempt}")
print()

user.increment_login_attempts() # nova tentativa
user.describe_user()
user.greet_user()
