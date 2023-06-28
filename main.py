from useroperation import UserOperation
from productoperation import ProductOperation
from orderoperation import OrderOperation
from interface import InterfaceClass

def main():
    user_operation = UserOperation()
    product_operation = ProductOperation()
    order_operation = OrderOperation()
    interface = InterfaceClass()

    while True:
        interface.main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # Login
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            success, user_role = user_operation.login(username, password)
            if success:
                if user_role == "admin":
                    admin_menu(interface, product_operation, user_operation, order_operation)
                else:
                    customer_menu(interface, product_operation, user_operation, order_operation)
            else:
                interface.print_error_message("UserOperation.login", "Username or password incorrect")

        elif choice == "2":
            # Register
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            success = user_operation.register(username, password)
            if success:
                interface.print_message("Registration successful")
            else:
                interface.print_error_message("UserOperation.register", "Registration failed")

        elif choice == "3":
            # Quit
            break

        else:
            interface.print_error_message("Main Menu", "Invalid choice")

def admin_menu(interface, product_operation, user_operation, order_operation):
    while True:
        interface.admin_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # Show products
            page_number = int(input("Enter the page number: "))
            product_list = product_operation.get_product_list(page_number)
            interface.show_list("admin", "product", product_list)

        elif choice == "2":
            # TODO
            # Add customers
            # ...

        elif choice == "3":
            # TODO
            # Show customers
            # ...

        elif choice == "4":
            # TODO
            # Show orders
            # ...

        elif choice == "5":
            # TODO
            # Generate test data
            # ...

        elif choice == "6":
            # TODO
            # Generate all statistical figures
            # ...

        elif choice == "7":
            # TODO
            # Delete all data
            # ...

        elif choice == "8":
            # TODO
            # Logout
            break

        else:
            interface.print_error_message("Admin Menu", "Invalid choice")

def customer_menu(interface, product_operation, user_operation, order_operation):
    while True:
        interface.customer_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # TODO
            # Show profile
            ...

        elif choice == "2":
            # TODO
            # Update profile
            # ...

        elif choice == "3":
            # TODO
            # Show products
            # ...

        elif choice == "4":
            # TODO
            # Show history orders
            # ...

        elif choice == "5":
            # TODO
            # Generate all consumption figures
            # ...

        elif choice == "6":
            # TODO
            # Logout
            break

        else:
            interface.print_error_message("Customer Menu", "Invalid choice")

if __name__ == "__main__":
    main()
