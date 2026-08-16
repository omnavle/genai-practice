from sqlalchemy import Column, Integer, Float, String
from database.connection import Base

class Product(Base):
    __tablename__ = "products"
    
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    
    name = Column(
        String(100),
        nullable=False
    )
    
    price = Column(
        Float,
        nullable=False
    )
    
    category = Column(
        String(50),
        nullable=False
    )
    
    stock = Column(
        Integer, 
        default=0,
        nullable=False
    )