from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

class Product(BaseModel):
    name: str
    price: float
    category: str
    
products = []

@router.get("/")
def get_products():
    return {
        "products": products
    }

@router.get("/search")
def search_products(category: str):
    
    result = [
        product
        for product in products
        if product["category"].lower() == category.lower()
    ]
    
    return {
        "category": category,
        "products": result
    }
    
@router.get("/{product_id}")
def get_product(product_id: int):
    if product_id >= len(products):
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    return products[product_id]

@router.post("/")
def create_product(product: Product):
    products.append(product.model_dump())

    return {
        "message": "Product created successfully",
        "product": product
    }
    
@router.put("/{product_id}")
def update_product(product_id: int, product: Product):
    if product_id >= len(products):
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    products[product_id] = product.model_dump()
    
    return {
        "message": "Product updated successfully",
        "product": product
    }
    
@router.delete("/{product_id}")
def delete_product(product_id: int):

    if product_id >= len(products):
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    deleted_product = products.pop(product_id)

    return {
        "message": "Product deleted successfully",
        "product": deleted_product
    }