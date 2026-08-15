from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    price: float = Field(..., gt=0)
    category: str
    stock: int = Field(default=0, ge=0)

class ProductResponse(BaseModel):
    id: int 
    name: str
    price: float
    category: str
    stock: int