import os
import csv
import random
import string
import time
import matplotlib.pyplot as plt

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
    def __init__(self, user_id='u_0000000000', user_name='', user_password='', user_register_time='00-00-0000_00:00:00', user_role='customer'):
        super().__init__(user_id, user_name, user_password, user_register_time, user_role)

class Admin(User):
    def __init__(self, user_id='u_0000000000', user_name='', user_password='', user_register_time='00-00-0000_00:00:00', user_role='admin'):
        super().__init__(user_id, user_name, user_password, user_register_time, user_role)

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
                        return True, "customer"
                    elif user_data['user_role'] == 'admin':
                        return True, "admin"
        return False, ""

class Product:
    def __init__(self, pro_id='', pro_model='', pro_category='', pro_name='', pro_current_price=0.0, pro_raw_price=0.0, pro_discount=0, pro_likes_count=0):
        self.pro_id = pro_id
        self.pro_model = pro_model
        self.pro_category = pro_category
        self.pro_name = pro_name
        self.pro_current_price = pro_current_price
        self.pro_raw_price = pro_raw_price
        self.pro_discount = pro_discount
        self.pro_likes_count = pro_likes_count

    def __str__(self):
        return f"{{'pro_id': '{self.pro_id}', 'pro_model': '{self.pro_model}', 'pro_category': '{self.pro_category}', 'pro_name': '{self.pro_name}', 'pro_current_price': '{self.pro_current_price}', 'pro_raw_price': '{self.pro_raw_price}', 'pro_discount': '{self.pro_discount}', 'pro_likes_count': '{self.pro_likes_count}'}}"

class ProductOperation:
    @staticmethod
    def extract_products_from_files():
        products = []
        source_dir = "insource"

        for filename in os.listdir(source_dir):
            if filename.endswith(".csv"):
                file_path = os.path.join(source_dir, filename)
                with open(file_path, newline="") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        product = {
                            "pro_id": row["pro_id"],
                            "pro_model": row["pro_model"],
                            "pro_category": row["pro_category"],
                            "pro_name": row["pro_name"],
                            "pro_current_price": row["pro_current_price"],
                            "pro_raw_price": row["pro_raw_price"],
                            "pro_discount": row["pro_discount"],
                            "pro_likes_count": row["pro_likes_count"],
                        }
                        products.append(product)

        with open("data/products.txt", "w") as file:
            for product in products:
