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



class Privileges:
    """Set admin privileges"""

    def __init__(self, privileges=[]):
        """Hold your privileges"""
        self.privileges = privileges

    def show_privileges(self):
        """Show the admin privileges"""
        for i, privilege in enumerate(self.privileges):
            print(f"The number {i+1} privilege is {privilege}")


class Admin(User):
    """Gives the admin privileges"""

    def __init__(self, first_name, last_name, login_attempt=0, privileges=[]):
        """"Admin privileges"""
        super().__init__(first_name, last_name, login_attempt)
        print(f"Hello Admin {self.first_name} {self.last_name}")
        self.privileges = Privileges(privileges)