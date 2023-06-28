import os

class Order:
    def __init__(self, order_id='', user_id='', pro_id='', order_time='00-00-0000_00:00:00'):
        self.order_id = order_id
        self.user_id = user_id
        self.pro_id = pro_id
        self.order_time = order_time

    def __str__(self):
        return f"{{'order_id': '{self.order_id}', 'user_id': '{self.user_id}', 'pro_id': '{self.pro_id}', 'order_time': '{self.order_time}'}}"

# Main program
if __name__ == "__main__":
    # Create an order object
    order = Order(order_id='o_54321', user_id='u_12345', pro_id='p_98765', order_time='12-06-2023_15:30:00')

    # Print order information
    print(order)

    # Save order to file
    orders_file = "data/orders.txt"
    with open(orders_file, 'a') as file:
        file.write(str(order) + '\n')

