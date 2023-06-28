import re

class CustomerOperation:
    @staticmethod
    def validate_email(user_email):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, user_email) is not None

    @staticmethod
    def validate_mobile(user_mobile):
        mobile_regex = r'^(04|03)\d{8}$'
        return re.match(mobile_regex, user_mobile) is not None

    @staticmethod
    def register_customer(user_name, user_password, user_email, user_mobile):
        if not CustomerOperation.validate_email(user_email) or not CustomerOperation.validate_mobile(user_mobile):
            return False
        
        from datetime import datetime
        current_time = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
        
        user_id = UserOperation.generate_unique_user_id()
        if UserOperation.check_username_exist(user_name):
            return False
        
        customer = Customer(user_id=user_id, user_name=user_name, user_password=user_password, 
                            user_register_time=current_time, user_role='customer', user_email=user_email, user_mobile=user_mobile)
        with open("data/users.txt", 'a') as file:
            file.write(str(customer) + '\n')
        
        return True

    @staticmethod
    def update_profile(attribute_name, value, customer_object):
        if attribute_name == 'user_email':
            if not CustomerOperation.validate_email(value):
                return False
        elif attribute_name == 'user_mobile':
            if not CustomerOperation.validate_mobile(value):
                return False
        
        customer_object.__setattr__(attribute_name, value)
        customers = CustomerOperation.get_all_customers()
        for i, customer in enumerate(customers):
            if customer.user_id == customer_object.user_id:
                customers[i] = customer_object
                break
        
        with open("data/users.txt", 'w') as file:
            for customer in customers:
                file.write(str(customer) + '\n')
        
        return True

    @staticmethod
    def delete_customer(customer_id):
        customers = CustomerOperation.get_all_customers()
        for i, customer in enumerate(customers):
            if customer.user_id == customer_id:
                del customers[i]
                with open("data/users.txt", 'w') as file:
                    for customer in customers:
                        file.write(str(customer) + '\n')
                return True
        
        return False

    @staticmethod
    def get_customer_list(page_number):
        customers = CustomerOperation.get_all_customers()
        total_pages = (len(customers) + 9) // 10
        start_index = (page_number - 1) * 10
        end_index = start_index + 10
        page_customers = customers[start_index:end_index]
        return page_customers, page_number, total_pages

    @staticmethod
    def delete_all_customers():
        with open("data/users.txt", 'w') as file:
            pass

    @staticmethod
    def get_all_customers():
        customers = []
        with open("data/users.txt", 'r') as file:
            for line in file:
                user_data = eval(line.strip())
                if user_data['user_role'] == 'customer':
                    customers.append(Customer(**user_data))
        return customers
