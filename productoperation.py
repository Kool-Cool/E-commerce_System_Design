import csv
import os
import matplotlib.pyplot as plt
import numpy as np

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
                file.write(str(product) + "\n")

    @staticmethod
    def get_product_list(page_number):
        products_per_page = 10
        total_pages = 0
        product_list = []

        with open("data/products.txt", "r") as file:
            lines = file.readlines()
            total_products = len(lines)
            total_pages = (total_products // products_per_page) + (total_products % products_per_page > 0)

            start_index = (page_number - 1) * products_per_page
            end_index = start_index + products_per_page
            for line in lines[start_index:end_index]:
                product = eval(line)
                product_list.append(Product(**product))

        return product_list, page_number, total_pages

    @staticmethod
    def delete_product(product_id):
        deleted = False

        with open("data/products.txt", "r") as file:
            lines = file.readlines()

        with open("data/products.txt", "w") as file:
            for line in lines:
                product = eval(line)
                if product["pro_id"] != product_id:
                    file.write(line)
                else:
                    deleted = True

        return deleted

    @staticmethod
    def get_product_list_by_keyword(keyword):
        products = []

        with open("data/products.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            product = eval(line)
            if keyword.lower() in product["pro_name"].lower():
                products.append(Product(**product))

        return products

    @staticmethod
    def get_product_by_id(product_id):
        product = None

        with open("data/products.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            p = eval(line)
            if p["pro_id"] == product_id:
                product = Product(**p)
                break

        return product

    @staticmethod
    def generate_category_figure():
        categories = {}
        with open("data/products.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            product = eval(line)
            category = product["pro_category"]
            if category in categories:
                categories[category] += 1
            else:
                categories[category] = 1

        sorted_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)
        x = [category[0] for category in sorted_categories]
        y = [category[1] for category in sorted_categories]

        plt.bar(x, y)
        plt.xlabel("Category")
        plt.ylabel("Number of Products")
        plt.xticks(rotation=45)
        plt.savefig("data/figure/category_figure.png")
        plt.close()

    @staticmethod
    def generate_discount_figure():
        discount_ranges = {"<30%": 0, "30-60%": 0, ">60%": 0}
        with open("data/products.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            product = eval(line)
            discount = float(product["pro_discount"])
            if discount < 30:
                discount_ranges["<30%"] += 1
            elif 30 <= discount <= 60:
                discount_ranges["30-60%"] += 1
            else:
                discount_ranges[">60%"] += 1

        labels = list(discount_ranges.keys())
        sizes = list(discount_ranges.values())

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
        ax.axis("equal")
        plt.savefig("data/figure/discount_figure.png")
        plt.close()

    @staticmethod
    def generate_likes_count_figure():
        categories = {}
        with open("data/products.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            product = eval(line)
            category = product["pro_category"]
            likes_count = int(product["pro_likes_count"])
            if category in categories:
                categories[category] += likes_count
            else:
                categories[category] = likes_count

        sorted_categories = sorted(categories.items(), key=lambda x: x[1])
        x = [category[0] for category in sorted_categories]
        y = [category[1] for category in sorted_categories]

        plt.bar(x, y)
        plt.xlabel("Category")
        plt.ylabel("Sum of Likes Count")
        plt.xticks(rotation=45)
        plt.savefig("data/figure/likes_count_figure.png")
        plt.close()

    @staticmethod
    def generate_discount_likes_count_figure():
        discount_values = []
        likes_counts = []
        with open("data/products.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            product = eval(line)
            discount = float(product["pro_discount"])
            likes_count = int(product["pro_likes_count"])
            discount_values.append(discount)
            likes_counts.append(likes_count)

        plt.scatter(discount_values, likes_counts)
        plt.xlabel("Discount")
        plt.ylabel("Likes Count")
        plt.savefig("data/figure/discount_likes_count_figure.png")
        plt.close()

    @staticmethod
    def delete_all_products():
        with open("data/products.txt", "w") as file:
            pass
