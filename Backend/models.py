from pydantic import BaseModel
from typing import List
from typing import List

class ProductModel(BaseModel):
    name: str
    price: float
    available_quantity: int

class OrderItemModel(BaseModel):
    productId: str
    boughtQuantity: int
    total_amount: float

class UserAddressModel(BaseModel):
    city: str
    country: str
    zip_code: str

class OrderModel(BaseModel):
    items: List[OrderItemModel]
    user_address: UserAddressModel
