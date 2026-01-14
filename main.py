from fastapi import FastAPI
from models import Product

app = FastAPI()




products = [
  Product(id=1, name="Bottle", description="Bottle For Jogging", price=150.0, quantity=20),
  Product(id=2, name="Running Shoes", description="Lightweight Running Shoes", price=89.99, quantity=15),
  Product(id=3, name="Water Flask", description="Insulated Water Flask", price=45.50, quantity=30),
  Product(id=4, name="Sports Watch", description="Digital Sports Watch", price=199.99, quantity=10),
  Product(id=5, name="Headphones", description="Wireless Bluetooth Headphones", price=79.99, quantity=25),
  Product(id=6, name="Gym Bag", description="Large Capacity Gym Bag", price=65.00, quantity=18),
  Product(id=7, name="Yoga Mat", description="Non-slip Yoga Mat", price=35.99, quantity=40),
  Product(id=8, name="Protein Powder", description="Whey Protein Powder", price=55.00, quantity=50),
  Product(id=9, name="Resistance Bands", description="Set of 5 Resistance Bands", price=29.99, quantity=35),
  Product(id=10, name="Smartwatch", description="Fitness Tracking Smartwatch", price=249.99, quantity=12)
]


@app.get("/products")
def get_products():
  return products

@app.get("/product/{id}")
def get_product_by_id(id: int): 
  for product in products:
    if product.id == id:
      return product
  
  return "Product {id} Not Found"


@app.put("/product")
def update_product(id: int, product: Product):
  for i in range(len(products)):
    if products[i].id == id:
      product[i] = product
      return "Product Updated Successfully"


@app.post("/product")
def add_product(product: Product):
  products.append(product)
  return "Product Added Successfully"

@app.delete("/product")
def delete_product(id: int):
  for i in range(len(products)):
    if products[i].id == id:
      del products[i]
      return "Product {Id} Deleted Successfully"
  
  return "Product {id} Not Found"