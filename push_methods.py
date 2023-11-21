# Membuat Kelas Order 
class Order:
    def __init__(self, order_id, customer_name, order_date, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.total_amount = total_amount

    def calculate_tax(self, tax_rate):
        return self.total_amount * tax_rate
    
    def display_order(self):
        print(f"Order ID: {self.order_id}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Order Date: {self.order_date}")
        print(f"Total Amount: RP{self.total_amount}")

# Membuat Kelas Order Processor
class OrderProcessor:
    def __init__(self):
        self.orders = []
    
    def add_order(self, order):
        self.orders.append(order)

    def calculate_total_revenue(self):
        return sum(order.total_amount for order in self.orders)

    def calculate_total_tax(self, tax_rate):
        return sum(order.calculate_tax(tax_rate) for order in self.orders)

    def display_orders(self):
        for order in self.orders:
            order.display_order()
            print(" ")

#Program Utama
if __name__ == "__main__":

    #Membuat Objek Order
    order_1 = Order("01", "Satriyo Wisnu", "24-08-2023", 500000)
    order_2 = Order("02", "Nahdiyah", "26-11-2023", 300000)
    order_3 = Order("03", "Budi", "20-11-2023", 140000)
    order_4 = Order("04", "Tiki", "24-11-2023", 220000)

    #Membuat Objek Order Processor
    order_processor = OrderProcessor()

    #Menambah Order kedalam objek order processor
    order_processor.add_order(order_1)
    order_processor.add_order(order_2)
    order_processor.add_order(order_3)
    order_processor.add_order(order_4)

    order_processor.display_orders()

    # Menghitung Total Pendapatan dan Pajak
    total_revenue = order_processor.calculate_total_revenue()
    total_tax = order_processor.calculate_total_tax(0.2)

    print("\nTotal Pendapatan : RP{:.2f}\n".format(total_revenue))
    print("\nTotal Pajak : RP{:.2f}".format(total_tax)) 