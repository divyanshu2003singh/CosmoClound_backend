from main import app

from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from models import ProductModel, OrderItemModel, UserAddressModel, OrderModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    if token != "your_valid_token":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return token

@app.post("/createproducts", response_model=dict)
async def create_product(product: ProductModel, current_user: str = Depends(get_current_user)):
    try:
        inserted_product = products_collection.insert_one(product.dict())
        return {"message": "Product created successfully", "product_id": str(inserted_product.inserted_id)}
    except Exception as e:
        print("Error:", e)  # Correct indentation
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.get("/products", response_model=List[ProductModel])
async def list_products(skip: int = 0, limit: int = 10):
    try:
        products = list(products_collection.find().skip(skip).limit(limit))
        return products
    except Exception as e:
        print("Error:", e)  # Correct indentation
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.post("/orders", response_model=dict)
async def create_order(order: OrderModel, current_user: str = Depends(get_current_user)):
    try:
        total_order_amount = sum(item.total_amount for item in order.items)
        order_data = {
            "timestamp": datetime.now(),
            "items": order.items,
            "total_amount": total_order_amount,
            "user_address": order.user_address.dict(),
        }
        inserted_order = orders_collection.insert_one(order_data)
        return {"message": "Order created successfully", "order_id": str(inserted_order.inserted_id)}
    except Exception as e:
        print("Error:", e)  # Correct indentation
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.get("/orders", response_model=List[OrderModel])
async def list_orders(skip: int = 0, limit: int = 10):
    try:
        orders = list(orders_collection.find().skip(skip).limit(limit))
        return orders
    except Exception as e:
        print("Error:", e)  # Correct indentation
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.get("/orders/{order_id}", response_model=OrderModel)
async def get_order(order_id: str):
    try:
        order = orders_collection.find_one({"_id": ObjectId(order_id)})
        if order:
            return order
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    except Exception as e:
        print("Error:", e)  # Correct indentation
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.put("/products/{product_id}", response_model=dict)
async def update_product(product_id: str, updated_quantity: int, current_user: str = Depends(get_current_user)):
    try:
        result = products_collection.update_one({"_id": ObjectId(product_id)}, {"$set": {"available_quantity": updated_quantity}})
        if result.modified_count == 1:
            return {"message": "Product updated successfully"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    except Exception as e:
        print("Error:", e)  # Correct indentation
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
