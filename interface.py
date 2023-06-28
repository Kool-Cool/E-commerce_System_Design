class InterfaceClass:
    @staticmethod
    def get_user_input(message, num_of_args):
        user_input = input(message).split()
        user_args = user_input[:num_of_args]
        user_args += [""] * (num_of_args - len(user_args))
        return user_args

    @staticmethod
    def main_menu():
        print("=== Login Menu ===")
        print("1. Login")
        print("2. Register")
        print("3. Quit")

    @staticmethod
    def admin_menu():
        print("=== Admin Menu ===")
        print("1. Show products")
        print("2. Add customers")
        print("3. Show customers")
        print("4. Show orders")
        print("5. Generate test data")
        print("6. Generate all statistical figures")
        print("7. Delete all data")
        print("8. Logout")

    @staticmethod
    def customer_menu():
        print("=== Customer Menu ===")
        print("1. Show profile")
        print("2. Update profile")
        print("3. Show products")
        print("4. Show history orders")
        print("5. Generate all consumption figures")
        print("6. Logout")

    @staticmethod
    def show_list(user_role, list_type, object_list):
        print("=== {} List ===".format(list_type.capitalize()))
        if user_role == "admin" or list_type in ["product", "order"]:
            objects = object_list[0]
            page_number = object_list[1]
            total_page = object_list[2]
            for i, obj in enumerate(objects):
                print("{}. {}".format(i + 1, str(obj)))
            print("--- Page {} of {} ---".format(page_number, total_page))
        else:
            print("Access Denied")

    @staticmethod
    def print_error_message(error_source, error_message):
        print("Error occurred in {}: {}".format(error_source, error_message))

    @staticmethod
    def print_message(message):
        print(message)

    @staticmethod
    def print_object(target_object):
        print(str(target_object))
