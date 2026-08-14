from fastapi import FastAPI
from routers import user, product, auth

app = FastAPI(
    title="FastAPI Practice",
    description="FastAPI learning project for AI Engineer interviews",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "FastAPI is running!"
    }
    
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
    
app.include_router(user.router)
app.include_router(product.router)
app.include_router(auth.router)