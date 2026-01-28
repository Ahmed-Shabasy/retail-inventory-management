# Retail Inventory Management System

A CLI-based application for retail inventory management, built as an enhanced capstone project for "Building Applications with OOP in Python" track on DataCamp.

## Description

This Python application manages an inventory of products and allows for basic order placement functionality. The application uses object-oriented programming (OOP) principles including abstract base classes, inheritance, and exception handling. It includes sorting algorithms, binary search for product lookup, and input validation.

## Key Features

* Add, update, and delete products from inventory
* Place orders for products with automatic inventory quantity adjustment
* Reuses deleted product IDs when adding new products
* Binary search for finding products (O(log n) time complexity)
* Adaptive sorting: uses insertion sort for small arrays (<1000 items), merge sort for larger arrays
* Custom exceptions for different error types
* Input validation for all operations

## Class Structure

### Exceptions
* `InventoryException`: Base exception
* `InvalidProductDataException`: For invalid product data
* `InvalidOrderDataException`: For invalid order data
* `MoreThanOneProductException`: When customer tries to order more than one product

### Abstract Classes
* `ISort`: Interface for sorting algorithms
* `IProductRepository`: Interface for product repository
* `Order` (abstract): Base class for order functionality

### Implementation Classes
* `MergeSort`: Merge sort algorithm implementation
* `Sort`: Implements insertion sort and merge sort with adaptive selection
* `ProductRepository`: Manages product inventory (add, update, delete)
* `BinarySearch`: Binary search for finding products by ID
* `ProductInfo`: Stores product information
* `Order`: Handles order placement
* `OrderInfo`: Stores order information

## Key Learning Outcomes

* Implemented abstract base classes and inheritance
* Created custom exception classes
* Implemented sorting algorithms (insertion sort and merge sort)
* Implemented binary search algorithm
* Used type hints for function parameters
* Validated user inputs
* Separated data classes from logic classes

## Project Structure

```
retail-inventory-management/
├── application code/
│   └── main.py          # Complete application with all classes and demo code
└── README.md            # This file
```

## Algorithm Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Add Product | O(n log n) worst case* | O(n) |
| Update Product | O(log n) | O(log n) |
| Delete Product | O(log n) | O(log n) |
| Binary Search | O(log n) | O(log n) |
| Insertion Sort | O(n²) average | O(1) |
| Merge Sort | O(n log n) | O(n) |

## Usage Examples

### Adding Products
```python
product_repo = ProductRepository()
result = product_repo.add_product("Laptop", "Electronics", 55, 1000, "Supplier A")
# Output: "Product added successfully"
```

### Updating Products
```python
result = product_repo.update_product(1, quantity=45, price=950)
# Output: "Product information updated successfully"
```

### Deleting Products
```python
result = product_repo.delete_product(1)
# Output: "Product deleted successfully"
```

### Placing Orders
```python
order = Order(order_id=1, products=[])
result = order.place_order(1, 2, product_repo, customer_info="John Doe")
# Output: "Order placed successfully. Order ID: 1"
```

## Error Handling

The application validates:
* Data types (strings, integers)
* Non-negative values for quantity and price
* Non-empty strings for text fields
* Product existence before operations
* Sufficient quantity before placing orders
* One product limit per order

## Improvements from Original Version

* Added abstract base classes (`ISort`, `IProductRepository`, `Order`)
* Implemented custom exception classes for error handling
* Changed from class-level inventory to instance-level (`ProductRepository` class)
* Added binary search instead of linear search for finding products
* Implemented merge sort algorithm
* Added adaptive sorting (insertion sort for small arrays, merge sort for large arrays)
* Added ID reuse functionality for deleted products
* Added input validation with type checking
* Separated `ProductInfo` and `OrderInfo` as data classes
* Added docstrings to methods

## Known Limitations

* Orders are currently limited to one product per order
* Merge sort implementation is optimized for arrays (linked list version pending)
* No persistence layer (data is lost when application terminates)
* Application code can be designed better

## Future Enhancements

* Allow multiple products per order (currently limited to one)
* Modularize the application to be more readable, maintainable

## Acknowledgements

This project was created as an enhanced version of the capstone project for the "Building Applications with OOP in Python" track on DataCamp. The original project provided foundational knowledge, which was significantly expanded with SOLID principles, advanced algorithms, and professional software engineering practices.

## Contributing

Suggestions and feedback are welcome! Feel free to:
* Report issues or bugs
* Suggest new features
* Propose code improvements
* Share best practices

## Conclusion

This project demonstrates the evolution from a basic OOP application to a well-architected system. It showcases the importance of design principles, algorithm optimization, and robust error handling in creating maintainable and scalable software.
