#Assignment-5
class Product:
    def __init__(self,productid,Name,Quantity,price):
        self.productid = productid
        self.name = Name
        self.quantity = Quantity
        self.price = price
        self.next = None

    def __repr__(self):
        return f"ID:{self.productid}, Name:{self.name}, Quantity:{self.quantity}, price:${self.price:.2f}"

    class InventoryManager:
        
        def __init__(self) :
            self.head = None
        
        def addproduct(self,productid,Name,Quantity,price):
            new_product = Product(productid,Name,Quantity,price)
            new_product.next = self.head
            self.head = new_product
        
        def updateqty(self,productid,Name,Quantity):
            current = self.head
            while current:
                if current.productid == productid:
                    current.quantity == Quantity
                    return
                current = current.next
                print(f"Product with Id{productid}not found")
        
        def cal_total_val(self):
            total_value = 0.0
            while current:
                total_value += current.quantity * current.price
                current = current.next
            return total_value

        def dispaly(self):
            current = self.head
            if current is None :
                print("No product in inventory")
            else:
                while current:
                    print(current)
                    current = current.next
        
        def __del___(self):
            pass

        def main():
            manager = InventoryManager()

            while True:
                print("1) Add product")
                print("2) Update product qty")
                print("3) cal. totalvalues of product")
                print("4) display product")
                print("5) Exit")

                choice = input("Enter your choice")

            if choice == '1':
             product_id = input("Enter product ID: ")
             name = input("Enter product name: ")
             quantity = int(input("Enter product quantity: "))
             price = float(input("Enter product price: "))
             manager.add_product(product_id, name, quantity, price)
             print("Product added successfully.")

            elif choice == '2':
             product_id = input("Enter product ID to update: ")
             new_quantity = int(input("Enter new quantity: "))
             manager.update_quantity(product_id, new_quantity)

            elif choice == '3':
             print("Current Inventory:")
             manager.display_products()

            elif choice == '4':
             total_value = inventory.calculate_total_value()
             print(f"\nTotal Inventory Value: ${total_value:.2f}")
        
            elif choice == '5':
             print("Exiting the system.")
             

            else:
             print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
   InventoryManager.main()




                
            



        
