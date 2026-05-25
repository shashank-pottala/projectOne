from fastapi import FastAPI
from models import Products

app = FastAPI()

products = [

Products(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
Products(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
Products(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
Products(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]

@app.get("/")
async def home():
    return("home page")

@app.get("/products")
async def products_list():
    return(products)

@app.get("/products/{id}")
async def products_list(id: int):
    return(products[id])

@app.put("/products/{id}")
async def products_update(id: int, updated_product: Products):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = updated_product
            return"successful"
    return " not successful "

@app.post("/products")
async def new_product(new_pro: Products):
    products.append(new_pro)
    return"succesful"

@app.delete("/products/{id}")
async def del_product(id: int, d_product: Products):
    for i in range(len(products)):
        if products[i].id==id:
            del products[i]
            return"successful"
    return "id not found"