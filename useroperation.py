import random
import string

class UserOperation:
    @staticmethod
    def generate_unique_user_id():
        unique_id = ''.join(random.choices(string.digits, k=10))
        return f'u_{unique_id}'

    @staticmethod
    def encrypt_password(user_password):
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=len(user_password) * 2))
        encrypted_password = ''
        for i, char in enumerate(user_password):
            encrypted_password += random_string[i*2] + char
        encrypted_password = f"^^{encrypted_password}$$"
        return encrypted_password

    @staticmethod
    def decrypt_password(encrypted_password):
        decrypted_password = ''
        for i in range(2, len(encrypted_password)-2, 2):
            decrypted_password += encrypted_password[i]
        return decrypted_password

    @staticmethod
    def check_username_exist(user_name):
        users_file = "data/users.txt"
        with open(users_file, 'r') as file:
            for line in file:
                user_data = eval(line.strip())
                if user_data['user_name'] == user_name:
                    return True
        return False

    @staticmethod
    def validate_username(user_name):
        if len(user_name) >= 5 and user_name.isalnum():
            return True
        return False

    @staticmethod
    def validate_password(user_password):
        if len(user_password) >= 5 and any(char.isdigit() for char in user_password) and any(char.isalpha() for char in user_password):
            return True
        return False

    @staticmethod
    def login(user_name, user_password):
        users_file = "data/users.txt"
        with open(users_file, 'r') as file:
            for line in file:
                user_data = eval(line.strip())
                if user_data['user_name'] == user_name and UserOperation.decrypt_password(user_data['user_password']) == user_password:
                    if user_data['user_role'] == 'customer':
                        from CustomerClass import Customer
                        return user_name, user_password, Customer(**user_data)
                    elif user_data['user_role'] == 'admin':
                        from AdminClass import Admin
                        return user_name, user_password, Admin(**user_data)
        return None

# Main program
if __name__ == "__main__":
    # Generate a unique user ID
    unique_id = UserOperation.generate_unique_user_id()
    print(unique_id)

    # Encrypt a user password
    user_password = "admin1"
    encrypted_password = UserOperation.encrypt_password(user_password)
    print(encrypted_password)

    # Decrypt an encrypted password
    decrypted_password = UserOperation.decrypt_password(encrypted_password)
    print(decrypted_password)

    # Check if a username exists
    user_name = "JohnDoe"
    username_exists = UserOperation.check_username_exist(user_name)
    print(username_exists)

    # Validate a username
    username_valid = UserOperation.validate_username(user_name)
    print(username_valid)

    # Validate a password
    password_valid = UserOperation.validate_password(user_password)
    print(password_valid)

    # Perform user login
    logged_in_user = UserOperation.login(user_name, user_password)
    print(logged_in_user)
