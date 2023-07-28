![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)
# E-Commerce System

## Overview

This project is an E-Commerce System designed to facilitate online shopping and order management. The system supports user registration, login, and authentication for both customers and administrators. Customers can browse products, place orders, and view their order history, while administrators have additional privileges like managing products, customers, and orders. The system also provides various statistical figures related to product sales and customer consumption.

## Features

- User Operations: User registration and login with encrypted passwords, role-based authentication, and user profile management.
- Product Operations: View products in a paginated list, search products by keyword, add and delete products (for administrators), and generate statistical figures related to product sales.
- Order Operations: Place orders with unique order IDs, view order history for customers, generate statistical figures related to customer consumption and top 10 best-selling products, and delete individual or all orders (for administrators).
- Interface: Simple and interactive command-line interface for user interaction with clear menu options for navigation.

## Getting Started

### Prerequisites

- Python 3.x
- matplotlib library (for generating statistical figures)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/e-commerce-system.git
   cd e-commerce-system
   ```
Install the required dependencies:

```bash
pip install matplotlib
```
## Usage
To start the E-Commerce System, run the following command in the project directory:

```bash
python main.py
```
Follow the on-screen instructions to navigate the menu and perform various operations.

## File Structure
The project consists of the following files and directories:

- **main.py**: The main program that interacts with the user and manages the application flow.
- **user.py**: Defines the **User**, **Customer**, and **Admin** classes for user-related operations.
- **useroperation.py**: Contains the **UserOperation** class for user-related functionalities like login, registration, and password encryption.
- **product.py**: Defines the **Product** class for representing product information.
- **productoperation.py**: Contains the **ProductOperation** class for product-related functionalities like listing, adding, and generating statistical figures.
- **order.py**: Defines the Order class for representing order information.
- **orderoperation.py**: Contains the OrderOperation class for order-related functionalities like placing orders, listing, and generating statistical figures.
- **interface.py**: Defines the InterfaceClass class for displaying menus and user interactions.
- **data**: Directory containing text files to store user, product, and order data.
- data/figure: Directory for storing generated statistical figures.

## Functionality
The E-Commerce System offers the following functionalities:

- User Operations: Registration, login, and profile management for both customers and administrators.
- Product Operations: Listing, search, add, and delete products (for administrators), and generate statistical figures related to products.
- Order Operations: Place orders, view order history, and generate statistical figures for customer consumption and best-selling products.
- Interface: A user-friendly command-line interface for easy navigation and interaction.

## Contributing
Contributions to this project are welcome. Feel free to create pull requests for bug fixes, new features, or improvements.

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute it as per the terms of the license.
# Features
```
User Manual for Application XYZ

1. Introduction
   The Application XYZ is a system that allows users to perform various operations such as
  login, registration, managing products, handling orders, and generating reports.
  This user manual provides instructions on how to use the application effectively.

2. Getting Started
   To begin using the application, follow these steps:
   - Launch the application on your device.
   - You will be presented with the main menu options: Login, Register, and Quit.

3. Login
   To log in to the application, follow these steps:
   - Select the Login option from the main menu.
   - Enter your username and password when prompted.
   - If the credentials are correct, you will be redirected to the appropriate user menu based on your role (admin or customer).
   - If the credentials are incorrect, an error message will be displayed.

4. Register
   To create a new user account, follow these steps:
   - Select the Register option from the main menu.
   - Enter a username and password when prompted.
   - If the registration is successful, a confirmation message will be displayed.
   - If the registration fails (e.g., username already exists), an error message will be displayed.

5. Admin Menu
   The admin menu provides the following options:
   - Show Products: Displays a list of products.
   - Add Customers: Allows adding new customers to the system.
   - Show Customers: Displays a list of customers.
   - Show Orders: Displays a list of orders.
   - Generate Test Data: Automatically generates test data for customers and orders.
   - Generate All Statistical Figures: Generates various statistical figures.
   - Delete All Data: Deletes all data in the system.
   - Logout: Logs out from the admin account and returns to the main menu.

6. Customer Menu
   The customer menu provides the following options:
   - Show Profile: Displays the customer's profile information.
   - Update Profile: Allows the customer to update their profile information.
   - Show Products: Displays a list of products.
   - Show History Orders: Displays a list of previous orders.
   - Generate All Consumption Figures: Generates consumption figures for the customer.
   - Logout: Logs out from the customer account and returns to the main menu.

7. Conclusion
   This user manual provides a basic guide on using the Application XYZ effectively. Please refer to the on-screen instructions and error messages for detailed information during the application's usage.


```
 
for more refer **[Specification](https://github.com/Kool-Cool/E-commerce_System_Design/blob/main/Specification.docx%20(1).pdf)**

## 
If you want to contribute to this project, you are more than welcome! You can fork this repository, make your changes, and submit a pull request. I will review your code and merge it if it meets the quality standards. You can also open an issue if you have any questions, suggestions, or feedback. I appreciate your help and support!

This project is open for contribution from anyone who wants to help improve it. Whether you have a bug fix, a new feature, a documentation update, or anything else, you are welcome to submit a pull request or an issue.


To contribute, please follow these steps:

- Fork this repository and clone it to your local machine.
- Create a new branch with a descriptive name for your changes.
- Make your changes and commit them with clear and concise messages.
- Push your branch to your forked repository and create a pull request to the main branch of this repository.
- Wait for feedback and approval from the maintainers.

Please make sure to follow the code style and conventions of this project, and to test your changes before submitting them.

Thank you for your interest and support!
