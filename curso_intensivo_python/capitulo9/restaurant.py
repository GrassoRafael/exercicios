class Restaurant:
    """Output a restaurant infomations"""

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = number_served

    def describe_restaurant(self):
        """Describe the restaurant input"""
        print(f"The name of the restaurant is {self.restaurant_name} and your type is {self.cuisine_type}\n"
              f"People served: {self.number_served}")

    def open_restaurant(self):
        """Output the restaurant - name - is open"""
        print(f"The restaurant {self.restaurant_name} is open")

    def set_number_served(self, update_number_served):
        """Update the number os customers served"""
        self.update_number_served = update_number_served
        print(f"People served are now: {self.update_number_served}")

    def increment_number_served(self, increment_customers_served):
        """Adds to the total number of customers served"""
        self.number_served += increment_customers_served
        print(f"You served {increment_customers_served} custumers today, you total is {self.number_served}")

