from fastapi import APIRouter, HTTPException
from datetime import datetime
from models import Product, ProductUpdate
from storage import read_data, write_data, generate_id, PRODUCTS_FILE

router= APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("/")
def get_products():
    return read_data(PRODUCTS_FILE)

@router.get("/{product_id}")
def get_product(product_id:int):
    products= read_data(PRODUCTS_FILE)
    for product in products:
        if product["id"]==product_id:
            return product
    raise HTTPException(status_code=404, detail=f"Product wih id {product_id} not found")

@router.post("/")
def create_product(product: Product):
    products= read_data(PRODUCTS_FILE)
    new_product = {
        "id": generate_id(products),
        "name":product.name,
        "price": product.price,
        "category": product.category,
        "stock": product.stock,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }
    products.append(new_product)
    write_data(PRODUCTS_FILE, products)
    return new_product

@router.put("/{product_id}")
def update_product(product_id : int , updated: ProductUpdate):
    products= read_data(PRODUCTS_FILE)
    for product in products:
        if product["id"]==product_id:
            if updated.name is not None:
                product["name"] = updated.name
            if updated.price is not None:
                product["price"] = updated.price
            if updated.category is not None:
                product["catgeory"]=updated.category
            if updated.stock is not None:
                product["stock"]=updated.stock
            product["updated_at"]=datetime.now().isoformat()
            write_data(PRODUCTS_FILE , products)
            return product
    raise HTTPException(status_code=404 , detail=f"Product with id { product_id} is not found")

@router.delete("/{product_id}")
def delete_product(product_id: int):
    products= read_data(PRODUCTS_FILE)
    for product in products:
        if product["id"]==product_id:
            products.remove(product)
            write_data(PRODUCTS_FILE , products)
            return {"message": f"Product '{product['name']}' deleted successfully"}
    raise HTTPException(status_code=404 , detail=f"Product with id{product_id} not found")