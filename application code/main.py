from abc import ABC, abstractmethod
from random import randint



class InventoryException(Exception):
    """Base exception for inventory management system"""
    pass

class InvalidProductDataException(InventoryException):
    """Raised when product data is invalid"""
    pass

class InvalidOrderDataException(InventoryException):
    """"Raised when order data is invalid"""
    pass

class MoreThanOneProductException(InventoryException):
    """Raised when the customer orders more than one product"""
    pass

# TODO: add NotImplementedError error for abstract methods



class ISort(ABC):
    """
    Abstract base class defining the interface for sorting algorithms.
    
    This interface requires implementations of insertion sort and merge sort
    algorithms for sorting collections of objects.
    """
    
    @staticmethod
    @abstractmethod
    def insertion_sort(A):
        """
        Sort an array in-place using the insertion sort algorithm.
        
        Args:
            A: Array-like collection to be sorted. Elements must have a 
               'product_id' attribute for comparison.
        
        Returns:
            None. Sorts the array in-place.
        """
        pass

    @staticmethod
    @abstractmethod
    def merge_sort(arr, l, r):
        """
        Sort an array in-place using the merge sort algorithm.
        
        Args:
            arr: Array-like collection to be sorted. Elements must have a
                 'product_id' attribute for comparison.
            l (int): Left index (starting position) of the subarray to sort.
            r (int): Right index (ending position) of the subarray to sort.
        
        Returns:
            None. Sorts the array in-place.
        """
        
        pass


class MergeSort:
    """
    Implementation of the merge sort algorithm optimized for linked lists
    and arrays of objects with product_id attributes.
    
    Merge sort is a divide-and-conquer algorithm with O(n log n) time complexity
    and is particularly efficient for linked lists due to its sequential access pattern.
    """
    
    @staticmethod
    def merge(arr, l, m, r):
        """
        Merge two sorted subarrays into a single sorted subarray,
        based on product_id
        
        Args:
            arr: The array containing the subarrays to merge.
            l (int): Starting index of the left subarray.
            m (int): Ending index of the left subarray (middle point).
            r (int): Ending index of the right subarray.
        
        Returns:
            None. Merges the subarrays in-place within arr.
        
        Algorithm:
            1. Creates temporary arrays L and R for the two halves
            2. Copies data to temporary arrays
            3. Merges the temporary arrays back into arr in sorted order
            4. Handles any remaining elements from either subarray
        """
        
        n1 = m - l + 1  # Size of left subarray
        n2 = r - m      # Size of right subarray

        # Create temporary arrays
        L = [0] * n1
        R = [0] * n2

        # Copy data to temporary arrays
        for i in range(n1):
            L[i] = arr[l + i]
        for j in range(n2):
            R[j] = arr[m + 1 + j]

        # Merge the temporary arrays back into arr[l..r]
        i = j = 0  # Initial indexes for L and R
        k = l      # Initial index for merged subarray

        # Merge while both arrays have elements
        while i < n1 and j < n2:
            if L[i].product_id <= R[j].product_id:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy remaining elements of L, if any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
            
        # Copy remaining elements of R, if any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    @staticmethod
    def merge_sort(arr, l, r):
        """
        Recursively sort an array using the merge sort algorithm.
        
        Args:
            arr: Array to be sorted. Elements must have a 'product_id' attribute.
            l (int): Left index (starting position) of the portion to sort.
            r (int): Right index (ending position) of the portion to sort.
        
        Returns:
            None. Sorts the array in-place.
        
        Time Complexity: O(n log n)
        Space Complexity: O(n) for temporary arrays during merging
        
        Algorithm:
            1. Divides array into two halves
            2. Recursively sorts each half
            3. Merges the sorted halves
        """
        if l < r:
            m = l + (r - l) // 2  # Find middle point, avoiding overflow
            MergeSort.merge_sort(arr, l, m)      # Sort first half
            MergeSort.merge_sort(arr, m + 1, r)  # Sort second half
            MergeSort.merge(arr, l, m, r)        # Merge the sorted halves


class Sort(ISort):
    """
    Concrete implementation of the ISort interface with adaptive sorting strategy.
    
    All sorting is performed on objects with 'product_id' attributes in ascending order.
    """
    
    @staticmethod
    def insertion_sort(A):
        """
        Sort an array in-place using insertion sort algorithm.
        
        Insertion sort is efficient for small datasets and nearly sorted data.
        
        Args:
            A: Array of objects to sort. Each object must have a 'product_id' attribute.
        
        Returns:
            None. Sorts the array in-place.
        
        Time Complexity: 
            - Best case: O(n) when array is already sorted
            - Average/Worst case: O(n²)
        Space Complexity: O(1)
        """
        
        n = len(A)
        for i in range(1, n):
            Hand = A[i]  # Element to be inserted into sorted portion
            j = i - 1
            # Move elements greater than Hand one position ahead
            while j >= 0 and A[j].product_id > Hand.product_id:  # FIXED: Now compares with Hand
                A[j+1] = A[j]
                j -= 1
            A[j+1] = Hand  # Insert Hand at correct position

    @staticmethod
    def merge_sort(arr, l, r):
        """
        Sort an array using merge sort (delegates to MergeSort class).
        
        Args:
            arr: Array to be sorted.
            l (int): Left index of the portion to sort.
            r (int): Right index of the portion to sort.
        
        Returns:
            None. Sorts the array in-place.
        """
        MergeSort.merge_sort(arr, l, r)

    @staticmethod 
    def sort(A):
        """
        Adaptively sort an array using the most appropriate algorithm.
        
        This method selects the optimal sorting algorithm based on array size:
        - Arrays with fewer than 1000 elements use insertion sort
        - Larger arrays use merge sort for better performance
        
        Args:
            A: Array of objects to sort. Each object must have a 'product_id' attribute.
        
        Returns:
            None. Sorts the array in-place in ascending order by product_id.
        
        Time Complexity:
            - Small arrays (< 1000): O(n²) average case
            - Large arrays (>= 1000): O(n log n)
        """
        
        if len(A) < 1000:
            Sort.insertion_sort(A)
        else:
            r = len(A) - 1
            Sort.merge_sort(A, 0, r)



class IProductRepository(ABC):
    """
    Abstract base class defining methods for ProductRepository class.
    """
    @abstractmethod
    def add_product(self):
        pass
    
    @abstractmethod
    def update_product(self):
        pass
    
    @abstractmethod
    def delete_product(self):
        pass
        


class ProductRepository(IProductRepository):
    """
     class for products repository
    
    Behaviors:
        add_product   : adds a product to the inventory
        update_product: update product's information
        delete_product: delete product from the inventory
    """
    
    def __init__(self) -> None:
        # Inventory is being put in the costructor be able to change its type anytime
        self.inventory = []
        self.deleted_ids = set()
    
    def add_product(self, name: str, category: str, quantity: int, price: int, supplier: str) -> str:
        """
        Add a new product to the inventory
        
        Args:
            name    : Product name       (non-empty string)
            category: Product category   (non-empty string)
            quantity: Available quantity (non-negative integer)
            price   : Product price      (non-negative integer)
            supplier: Supplier name      (non-empty string)
        
        Returns:
            Success message string
        
        Raises:
            InvalidProductDataException: if any parameter is invalid
            InventoryException         : it any other error happened
        """
        
        try:
            # Validation check and error handling
            # It checks for type, negative numbers, and empty strings
            if not name or not isinstance(name, str):
                raise InvalidProductDataException("Product name must be a non-empty string")
            if not category or not isinstance(category, str):
                raise InvalidProductDataException("Product category must be a non-empty string")
            if not isinstance(quantity, int) or quantity < 0:
                raise InvalidProductDataException("Product quantity must be an integer number")
            if not isinstance(price, int) or price < 0:
                raise InvalidProductDataException("Product price must be an integer number")
            if not supplier or not isinstance(supplier, str):
                raise InvalidProductDataException("Product supplier must be a non-empty string")
            
            # Make an easy-to-read reference for inventory
            inventory = self.inventory
            
            
            # Give the new product its proper id
            if self.deleted_ids:
                product_id = min(self.deleted_ids)
                # Make the product and add it to the inventory
                new_product = ProductInfo(product_id, name, category, quantity, price, supplier)
                inventory.append(new_product)
                # Sort the inventory according to product_id
                Sort.sort(inventory)
            else:
                # Make the id 1 if the inventoey is empty.
                # If not, or increase last id with 1
                product_id = 1 if len(inventory) == 0 else inventory[-1].product_id + 1
                # Make the product and add it to the inventory
                new_product = ProductInfo(product_id, name, category, quantity, price, supplier)
                inventory.append(new_product)
                # TODO: sort the inventory here, and modify delete_products
                # to add the deleted id to self.deleted_
            
            
            
            return "Product added successfully"
        
        except InvalidProductDataException:
            raise
        except InventoryException as e:
            raise InventoryException(f"Failed to add product: {str(e)}")
        
    
    def update_product(self, product_id: int, quantity: int = None, price: int = None, supplier: str = None) -> str:
        """
        Update product information in the inventory
        
        Args:
            product_id    : New Product id    (non-negative integer)
            quantity      : New quantity      (non-negative number)
            price         : New price         (non-negative number)
            supplier      : New supplier name (non-empty string)
        
        Returns:
            Success message string
        
        Raises:
            InvalidProductDataException: if any passed parameter is invalid
            InventoryException         : if any other error happened
        """
        
        try:
            # Search for the product index in O(log n) time
            idx = BinarySearch.id_search(self.inventory, product_id)
            # Check if the product is not exist
            if idx is None:
                raise InvalidProductDataException("Product not found.")
            
            # Make an easy-to-read reference for the product in the inventory
            product_in_inventory = self.inventory[idx]
            
            # Validation check and error handling
            # It checks for type, negative numbers, and empty strings
            if quantity is not None and (not isinstance(quantity, int) or quantity < 0):
                raise InvalidProductDataException("Product quantity must be a positive integer")
            if price is not None and (not isinstance(price, int) or price < 0):
                raise InvalidProductDataException("Product price must be an integer number")
            if supplier is not None and (not isinstance(supplier, str) or not supplier):
                raise InvalidProductDataException("Product supplier must be a non-empty string")
            
            # Update the quantity of the product if the user provided it
            if quantity is not None:
                product_in_inventory.quantity = quantity
            
            # Update the price of the product if the user provided it
            if price is not None:
                product_in_inventory.price = price
            
            # Update the supplier of the product if the user provided it
            if supplier is not None:
                product_in_inventory.supplier = supplier
                
            return "Product information updated successfully"
        
        except InvalidProductDataException:
            raise
        except InventoryException:
            raise
            
    
    def delete_product(self, product_id: int) -> str:
        """
        Delete a p3oduct from the inventory
        
        Args:
            product_id: Product id (non-negative integer)
        
        Returns:
            Success message string
        
        Raises:
            InvalidProductDataException: if any parameter is invalid
            InventoryException         : if any other error occured
        """
        
        try:
            # Search for the product index in O(log n) time
            idx = BinarySearch.id_search(self.inventory, product_id)
            # Check if the product is not exist
            if idx is None:
                raise InvalidProductDataException("Product not found.")
                
            # Add the id to deleted id's
            deleted_id = self.inventory[idx].product_id
            self.deleted_ids.add(deleted_id)
            
            # Remove the product from the inventory
            del self.inventory[idx]
            
            return "Product deleted successfully"
        
        except InvalidProductDataException:
            raise
        except InventoryException:
            raise



class BinarySearch:
    """
        Fast searching algorithm
        
        Time complexity : O(log n)
        Space complexity: O(n) due to recusrsion
    """
    
    @staticmethod
    def id_search(obj: ProductRepository, val: int, l: int = 0, r: int = None) -> int:
        """A method to search for product_id in O(log n) time instead of O(n)"""
        if r is None:
            r = len(obj) - 1
        if l > r:
            return None
        
        mid = (l + r) // 2
        mid_id = obj[mid].product_id
            
        if mid_id == val:
            return mid
        if mid_id < val:
            return BinarySearch.id_search(obj, val, mid+1, r)
        if mid_id > val:
            return BinarySearch.id_search(obj, val, l, mid-1)

        
# Being put here to not facing
# an error in BinarySearch type hints
class ProductInfo:
    """
     Class for setting product info
    
    Attributes:
        product_id: Product's id       (positive integer)
        name      : Product name       (non-empty string)
        category  : Product category   (non-empty string)
        quantity  : Available quantity (non-negative integer)
        price     : Product price      (non-negative integer)
        supplier  : Supplier name      (non-empty string)
    """
    
    def __init__(self, product_id: int, name: str, category: str, quantity: int, price: int, supplier: int) -> None:
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier
        


class Order(ABC):
    @abstractmethod
    def place_order(self):
        pass



class Order(Order):
    """
    A class the order products from the inventory
    
    Attributes:
        order_id     : The order id          (positive integer)
        products     : Order's products list (list)
        customer_info: Customer info         (non-empty string)
    
    Behaviors:
        place_order: places a new order
    """
    
    def __init__(self, order_id: int, products: list, customer_info: str = None) -> str: # I recomment to make it tuple only
        # Validation check and error handling
        # It checks for type, negative numbers, and empty strings
        if not isinstance(order_id, int) or order_id < 1:
            raise InvalidOrderDataException("Order id must be a positive integer")
        if not isinstance(products, list):
            raise InvalidOrderDataException("Products must be in a list")
        if customer_info is not None and (not isinstance(customer_info, str) or not customer_info):
            raise InvalidOrderDataException("Customer info must be a non-empty string")
        
        # Make a new order
        self.order = OrderInfo(order_id, products, customer_info)
        
        
    def place_order(self, product_id: int, quantity: int, repo: ProductRepository, customer_info: str = None) -> str:
        """
        Place a new order
        
        Args:
            product_id   : Ordered product's id                          (positive integer)
            quantity     : Quantity of the ordered product               (positive integer)
            repo         : The repository which the product ordered from (ProductRepository object)
            customer_info: Customer info                                 (non-empty string)
        
        Returns:
            Success message string
        
        Raises:
            InvalidOrderDataException  : If any passed parameter is invalid
            MoreThanOneProductException: If the customer ordered more than one product
            InventoryException         : If any other error occured
            
        """
        
        try:
            # An easy-to-read reference to the order info
            order = self.order
            
            # Check if the customer order more than one product
            # TODO: Make the customer able to order more than one product!
            if order.products:
                raise MoreThanOneProductException("You can only order ONE product")
            
            # Validation check and error handling
            # It checks for type, negative numbers, and empty strings
            if not isinstance(quantity, int) or quantity < 0:
                raise InvalidOrderDataException("Product quantity must be an integer number")
            if not isinstance(repo, ProductRepository):
                raise InvalidOrderDataException("Product repository must be a ProductRepository object")
            if customer_info is not None and (not (customer_info, str) or not customer_info):
                raise InvalidOrderDataException("Customer info must be a non-empty string")
            
            # Add customer info (if it is provided)
            if customer_info:
                order.customer_info = customer_info
            
            
            # Search for the product index in O(log n) time
            idx = BinarySearch.id_search(repo.inventory, product_id)
            # Check if the product is not exist
            if idx is None:
                raise InvalidProductDataException("Product not found.")
            
            # An easy-to-read reference to the product in the inventory
            product_in_inventory = repo.inventory[idx]
            
            # Check if the customer ordered more than the available quantity
            if product_in_inventory.quantity < quantity:
                raise InvalidOrderDataException(f"There is no enough quantity of this product to order.\nYou can order up to {product_in_inventory.quantity} copies.")
            
            # Add the order to the products list (products which the customer oredered)
            order.products.append((product_id, quantity))
            
            # Decrememt the quantity of the product
            product_in_inventory.quantity -= quantity
            
            return f"Order placed successfully. Order ID: {order.order_id}"
        
        except (InvalidOrderDataException, MoreThanOneProductException):
            raise
        except Exception as e:
            raise InventoryException(f"Order not done successfully {str(e)}")

class OrderInfo:
    """
    A class for setting order info
    
    Attributes:
        order_id: Order's id (positive integer)
        products: List of products ordered (list)
        customer_info: Customer info (non-empty string)
    """
    
    def __init__(self, order_id: str, products: list or tuple, customer_info: str = None):
        self.order_id = order_id
        self.products = products
        self.customer_info = customer_info



product = ProductRepository()

p1 = product.add_product("Laptop", "Electronics", 55, 1000, "Supplier A")
print(p1)

update_p1 = product.update_product(1, quantity=45, price=950)
print(update_p1)

delete_p1 = product.delete_product(1)
print(delete_p1)

p2 = product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A")
print(p2)

order = Order(order_id=1, products=[])
order_placement = order.place_order(1, 2, product, customer_info="John Doe")
print(order_placement)
