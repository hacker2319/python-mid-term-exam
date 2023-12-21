class ECommercePlatform:
    def __init__(self):
        self.product_catalog = {}
        self.shopping_cart = []
        self.order_history = []

    def add_product(self, product_id, name, price, category, stock):
        self.product_catalog[product_id] = {
            'name': name,
            'price': price,
            'category': category,
            'stock': stock
        }

    def display_products(self, sort_by='price'):
        sorted_products = sorted(self.product_catalog.items(), key=lambda x: x[1][sort_by])
        for product_id, details in sorted_products:
            print(f"ID: {product_id}, Name: {details['name']}, Price: {details['price']}, Stock: {details['stock']}")

    def search_products(self, keyword):
        results = [(product_id, details) for product_id, details in self.product_catalog.items()
                   if keyword.lower() in details['name'].lower() or keyword.lower() in details['category'].lower()]
        for product_id, details in results:
            print(f"ID: {product_id}, Name: {details['name']}, Price: {details['price']}, Stock: {details['stock']}")

    def add_to_cart(self, product_id, quantity=1):
        product_id = str(product_id)
        if product_id in self.product_catalog:
            if self.product_catalog[product_id]['stock'] > 0:
                if self.product_catalog[product_id]['stock'] >= quantity:
                    self.shopping_cart.append((product_id, quantity))
                    self.product_catalog[product_id]['stock'] -= quantity
                    print(f"Added {quantity} {self.product_catalog[product_id]['name']} to the cart.")
                else:
                    print("Insufficient stock.")
            else:
                print("Product out of stock.")
        else:
            print("Product not found.")

    def view_cart(self):
        for product_id, quantity in self.shopping_cart:
            details = self.product_catalog[product_id]
            print(f"ID: {product_id}, Name: {details['name']}, Quantity: {quantity}, Price: {details['price']}")

    def checkout(self):
        total_cost = 0
        for product_id, quantity in self.shopping_cart:
            total_cost += self.product_catalog[product_id]['price'] * quantity


        tax_rate = 0.1
        discount = 0.05
        tax_amount = total_cost * tax_rate
        discount_amount = total_cost * discount

        final_cost = total_cost + tax_amount - discount_amount


        self.order_history.append({'cart': self.shopping_cart, 'total_cost': final_cost})


        self.shopping_cart = []

        print(f"Total Cost: {total_cost}, Tax: {tax_amount}, Discount: {discount_amount}, Final Cost: {final_cost}")
        print("Checkout successful.")

    def view_order_history(self):
        for order in self.order_history:
            print("Order:")
            for product_id, quantity in order['cart']:
                details = self.product_catalog[product_id]
                print(f"ID: {product_id}, Name: {details['name']}, Quantity: {quantity}")
            print(f"Total Cost: {order['total_cost']}")
            print("-------------")


def main():
    ecommerce_platform = ECommercePlatform()

    while True:
        print("\n===== E-Commerce Platform =====")
        print("1. Display Products")
        print("2. Search Products")
        print("3. Add to Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. View Order History")
        print("7. Add products")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            sort_by = input("Sort by (price/popularity): ")
            ecommerce_platform.display_products(sort_by)
        elif choice == '2':
            keyword = input("Enter keyword for search: ")
            ecommerce_platform.search_products(keyword)
        elif choice == '3':
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))
            ecommerce_platform.add_to_cart(product_id, quantity)
        elif choice == '4':
            ecommerce_platform.view_cart()
        elif choice == '5':
            ecommerce_platform.checkout()
        elif choice == '6':
            ecommerce_platform.view_order_history()
        elif choice == '7':
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            category = input("Enter product category: ")
            stock = int(input("Enter product stock: "))
            ecommerce_platform.add_product(product_id, name, price, category, stock)
        elif choice == '8':
            print("Exiting program. Thank you!")

            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
