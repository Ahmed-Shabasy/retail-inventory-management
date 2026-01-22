class Product:
    inventory = []
    
    def __init__(self, product_id, name, category, quantity, price, supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier
        Product.inventory.append(self)
        
    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        product_id = 1 if len(cls.inventory) == 0 else cls.inventory[-1].product_id + 1
        new_product = cls(product_id, name, category, quantity, price, supplier)
        return "Product added successfully"
    
    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
        idx = -1
        for Product in cls.inventory:
            idx += 1
            if Product.product_id == product_id: break
        else:
            return "Product not found"
        if quantity is not None: cls.inventory[idx].quantity = quantity
        if price is not None: cls.inventory[idx].price = price
        if supplier is not None: cls.inventory[idx].supplier = supplier
        return "Product information updated successfully"
    
    @classmethod
    def delete_product(cls, product_id):
        idx = -1
        for Product in cls.inventory:
            idx += 1
            if Product.product_id == product_id:
                del cls.inventory[idx]
                return "Product deleted successfully"
        else:
            return "Product not found"
        

class Order:
    def __init__(self, order_id, products, customer_info=None):
        self.order_id = order_id
        self.products = products
        self.customer_info = customer_info
    
    def place_order(self, product_id, quantity, customer_info=None):
        if not self.products:
            self.products.append((product_id, quantity))
            for product in Product.inventory:
                if product.product_id == product_id:
                    product.quantity -= quantity
            if customer_info: self.customer_info = customer_info
            return f"Order placed successfully. Order ID: {self.order_id}"
        else:
            return "You can only order ONE product"


if __name__ = "__main__":
    p1 = Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A")
    
    update_p1 = Product.update_product(1, quantity=45, price=950)
    
    delete_p1 = Product.delete_product(1)
    
    p2 = Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A")
    print(p2)
    
    order = Order(order_id=1, products=[])
    order_placement = order.place_order(1, 2, customer_info="John Doe")
    print(order_placement)
