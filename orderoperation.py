import os
import csv
import random
import time
import matplotlib.pyplot as plt

class OrderOperation:
    @staticmethod
    def generate_unique_order_id():
        order_id = "o_" + str(random.randint(10000, 99999))
        while OrderOperation.check_duplicate_order_id(order_id):
            order_id = "o_" + str(random.randint(10000, 99999))
        return order_id

    @staticmethod
    def check_duplicate_order_id(order_id):
        with open("data/orders.txt", "r") as file:
            lines = file.readlines()
        for line in lines:
            order = eval(line)
            if order["order_id"] == order_id:
                return True
        return False

    @staticmethod
    def create_an_order(customer_id, product_id, create_time=None):
        if create_time is None:
            create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        order_id = OrderOperation.generate_unique_order_id()
        order_data = {"order_id": order_id, "customer_id": customer_id, "product_id": product_id, "create_time": create_time}

        with open("data/orders.txt", "a") as file:
            file.write(str(order_data) + "\n")

        return True

    @staticmethod
    def delete_order(order_id):
        with open("data/orders.txt", "r") as file:
            lines = file.readlines()

        found = False
        with open("data/orders.txt", "w") as file:
            for line in lines:
                order = eval(line)
                if order["order_id"] != order_id:
                    file.write(line)
                else:
                    found = True

        return found

    @staticmethod
    def get_order_list(customer_id, page_number):
        orders_per_page = 10
        with open("data/orders.txt", "r") as file:
            lines = file.readlines()

        customer_orders = []
        for line in lines:
            order = eval(line)
            if order["customer_id"] == customer_id:
                customer_orders.append(order)

        total_pages = (len(customer_orders) + orders_per_page - 1) // orders_per_page
        start_index = (page_number - 1) * orders_per_page
        end_index = min(start_index + orders_per_page, len(customer_orders))
        customer_orders = customer_orders[start_index:end_index]

        return customer_orders, page_number, total_pages

    @staticmethod
    def generate_test_order_data():
        customer_ids = []
        with open("data/customers.txt", "r") as file:
            lines = file.readlines()
        for line in lines:
            customer = eval(line)
            customer_ids.append(customer["customer_id"])

        product_ids = []
        with open("data/products.txt", "r") as file:
            lines = file.readlines()
        for line in lines:
            product = eval(line)
            product_ids.append(product["pro_id"])

        for _ in range(10):
            customer_id = random.choice(customer_ids)
            num_orders = random.randint(50, 200)
            for _ in range(num_orders):
                product_id = random.choice(product_ids)
                OrderOperation.create_an_order(customer_id, product_id)

    @staticmethod
    def generate_single_customer_consumption_figure(customer_id):
        consumption_per_month = {i: 0 for i in range(1, 13)}

        with open("data/orders.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            order = eval(line)
            if order["customer_id"] == customer_id:
                month = int(order["create_time"].split("-")[1])
                consumption_per_month[month] += OrderOperation.get_product_price(order["product_id"])

        months = list(consumption_per_month.keys())
        consumption = list(consumption_per_month.values())

        plt.plot(months, consumption)
        plt.xlabel("Month")
        plt.ylabel("Consumption")
        plt.title("Customer {} Consumption".format(customer_id))
        plt.savefig("data/figure/single_customer_consumption.png")
        plt.close()

    @staticmethod
    def generate_all_customers_consumption_figure():
        consumption_per_month = {i: 0 for i in range(1, 13)}

        with open("data/orders.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            order = eval(line)
            month = int(order["create_time"].split("-")[1])
            consumption_per_month[month] += OrderOperation.get_product_price(order["product_id"])

        months = list(consumption_per_month.keys())
        consumption = list(consumption_per_month.values())

        plt.plot(months, consumption)
        plt.xlabel("Month")
        plt.ylabel("Consumption")
        plt.title("All Customers Consumption")
        plt.savefig("data/figure/all_customers_consumption.png")
        plt.close()

    @staticmethod
    def generate_all_top_10_best_sellers_figure():
        product_sales = {}

        with open("data/orders.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            order = eval(line)
            product_id = order["product_id"]
            if product_id in product_sales:
                product_sales[product_id] += 1
            else:
                product_sales[product_id] = 1

        sorted_sales = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)
        top_10_products = sorted_sales[:10]

        products = []
        sales = []
        for product, sale in top_10_products:
            products.append(product)
            sales.append(sale)

        plt.bar(products, sales)
        plt.xlabel("Product ID")
        plt.ylabel("Sales")
        plt.title("Top 10 Best-Selling Products")
        plt.savefig("data/figure/top_10_best_sellers.png")
        plt.close()

    @staticmethod
    def delete_all_orders():
        with open("data/orders.txt", "w") as file:
            pass

    @staticmethod
    def get_product_price(product_id):
        with open("data/products.txt", "r") as file:
            lines = file.readlines()
        for line in lines:
            product = eval(line)
            if product["pro_id"] == product_id:
                return float(product["pro_current_price"])
        return 0.0
