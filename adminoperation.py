class AdminOperation:
    @staticmethod
    def register_admin():
        admin_id = UserOperation.generate_unique_user_id()
        admin_name = "admin"
        admin_password = "admin123"
        admin_register_time = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
        admin_role = "admin"

        admin = Admin(admin_id=admin_id, user_name=admin_name, user_password=admin_password,
                      user_register_time=admin_register_time, user_role=admin_role)

        with open("data/users.txt", "a") as file:
            file.write(str(admin) + "\n")
