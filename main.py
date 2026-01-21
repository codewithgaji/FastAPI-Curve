from fastapi import FastAPI, Depends
from models import Product
from database import  session, engine
import database_models
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



# ENABLE CORS
app.add_middleware(
  CORSMiddleware,
  allow_origins=["http://localhost:3000"],
  allow_methods = ["*"]
)


database_models.Base.metadata.create_all(bind=engine) # This is what creates the tables in the database, using "metadata" it assigns each attribute their own properties

# Defining Function to Dump Data

def init_db():
  db = session()
  count = db.query(database_models.Product).count() # This is used to check the db and count if there are data items already

  if count == 0:
    for product in products:
      db.add(database_models.Product(**product.model_dump())) # This is used to dump the pydantic model data to sqlalchemy while (**) unpacking it so it can be easily used.
    db.commit()

init_db()


def get_db_session():
  try:
    db = session()
    yield db
  finally:
    db.close()









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
def get_all_products(db: Session = Depends(get_db_session)):
  db_products = db.query(database_models.Product).all()
  if not db_products:
    return "No Products found"  
  return db_products  
  # # Connect to database
  # db = session()

  # # Query Database
  # db.query()

 
  return products



@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db_session)): 
  db_products = db.query(database_models.Product).filter(database_models.Product.id == id).first()
  if not db_products:
    return f"Product with Id: {id} Not found"
  return db_products
  # for product in products:
  #   if product.id == id:
  #     return product
  
  # return "Product {id} Not Found"


@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db_session)):
  db_products = db.query(database_models.Product).filter(database_models.Product.id == id).first()
  if not db_products:
    return f"Product {id} Does Not Exist, Update Failed!"
  db_products.name = product.name
  db_products.description = product.description
  db_products.price = product.price
  db_products.quantity = product.quantity
  db.commit()
  return f"Product {id} Successfully Updated!"
  # for i in range(len(products)):
  #   if products[i].id == id:
  #     product[i] = product
  #     return "Product Updated Successfully"


@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db_session)):
  db_product = db.query(database_models.Product).filter(database_models.Product.id == product.id).first()
  if not db_product:
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return f"{product.name} Added Successfully"
  return f"Product with Id: {db_product.id} already Exists"






@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db_session)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if not db_product:
      return f"Product with id:{id} Not Found"
    db.delete(db_product)
    db.commit()
    return f"{db_product.name} Deleted Successfully"
    

  # for i in range(len(products)):
  #   if products[i].id == id:
  #     del products[i]
  #     return "Product {Id} Deleted Successfully"
  
  # return "Product {id} Not Found"



