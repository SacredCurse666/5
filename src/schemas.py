from pydantic import BaseModel
from datetime import date

class DeliveryBase(BaseModel):
    amount: int
    date_delivery: date

class DeliveryCreate(DeliveryBase):

    pass

class Delivery(DeliveryBase):

    id: int
    order_id: int

    class Config:
        orm_mode = True



class OrderBase(BaseModel):
    amount: int
    date: date
    date_execute: date


class OrderCreate(OrderBase):

    pass

class Order(OrderBase):

    id: int
    enterprise_id: int
    product_id: int
    delivery: list[Delivery] = []

    class Config:
        orm_mode = True


    
class ProductBase(BaseModel):
    name: str
    amount: int
    price: int


class ProductCreate(ProductBase):

    pass

class Product(ProductBase):

    id: int
    brand_id: int
    order: list[Order] = []

    class Config:
        orm_mode = True




class EnterpriseBase(BaseModel):
    name: str
    address: str
    phone: str


class EnterpriseCreate(EnterpriseBase):

    pass

class Enterprise(EnterpriseBase):

    id: int
    order: list[Order] = []

    class Config:
        orm_mode = True



class BrandBase(BaseModel):
    name: str
    
class BrandCreate(BrandBase):

    pass

class Brand(BrandBase):

    id: int
    product: list[Product] = []

    class Config:
        orm_mode = True



