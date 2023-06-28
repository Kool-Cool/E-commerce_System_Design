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

class Admin(User):
    def __init__(self, user_id='u_0000000000', user_name='', user_password='', user_register_time='00-00-0000_00:00:00', user_role='admin'):
        super().__init__(user_id, user_name, user_password, user_register_time, user_role)

# Main program
if __name__ == "__main__":
    # Create an admin object
    admin = Admin(user_id='u_0987654321', user_name='Admin', user_password='admin123')

    # Print admin information
    print(admin)

    # Save admin to file
    users_file = "data/users.txt"
    with open(users_file, 'a') as file:
        file.write(str(admin) + '\n')

