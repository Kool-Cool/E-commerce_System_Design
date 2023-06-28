import os

class User:
    def __init__(self, user_id='u_0000000000', user_name='', user_password='', user_register_time='00-00-0000_00:00:00', user_role='customer'):
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_register_time = user_register_time
        self.user_role = user_role

    def __str__(self):
        return f"{{'user_id': '{self.user_id}', 'user_name': '{self.user_name}', 'user_password': '{self.user_password}', 'user_register_time': '{self.user_register_time}', 'user_role': '{self.user_role}'}}"

class Customer(User):
    def __init__(self, user_id='u_0000000000', user_name='', user_password='', user_register_time='00-00-0000_00:00:00', user_role='customer', user_email='', user_mobile=''):
        super().__init__(user_id, user_name, user_password, user_register_time, user_role)
        self.user_email = user_email
        self.user_mobile = user_mobile

    def __str__(self):
        return f"{super().__str__().strip('}')}, 'user_email': '{self.user_email}', 'user_mobile': '{self.user_mobile}'}}"

# Main program
if __name__ == "__main__":
    # Create a customer object
    customer = Customer(user_id='u_1234567890', user_name='John', user_password='password123', user_email='john@example.com', user_mobile='1234567890')

    # Print customer information
    print(customer)

    # Save customer to file
    users_file = "data/users.txt"
    with open(users_file, 'a') as file:
        file.write(str(customer) + '\n')

