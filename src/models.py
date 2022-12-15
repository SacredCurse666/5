from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()

class BaseModel(Base):
    """
    Абстартный базовый класс, где описаны все поля и методы по умолчанию
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    def __repr__(self):
        return f"<{type(self).__name__}(id={self.id})>" # pragma: no cover


class Product(BaseModel):
    __tablename__ = "products"

    name = Column(String)
    amount = Column(Integer)
    price = Column(Integer)


    brand_id = Column(Integer, ForeignKey("brands.id"))

    brand = relationship("Brand", back_populates="product")
    order = relationship("Order", back_populates="product")

class Brand(BaseModel):
    __tablename__ = "brands"

    name = Column(String)

    product = relationship("Product", back_populates="brand")
    
class Enterprise(BaseModel):
    __tablename__ = "enterprises"

    name = Column(String)
    address = Column(String)
    phone = Column(String)

    order = relationship("Order", back_populates="enterprise")


class Order(BaseModel):
    __tablename__ = "orders"

    amount = Column(Integer)
    date = Column(DateTime)
    date_execute = Column(DateTime)

    enterprise_id = Column(Integer, ForeignKey("enterprises.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    product = relationship("Product", back_populates="order")
    enterprise = relationship("Enterprise", back_populates="order")
    delivery = relationship("Delivery", back_populates="order")


class Delivery(BaseModel):
    __tablename__ = "deliveries"

    amount = Column(Integer)
    date_delivery = Column(DateTime)


    order_id = Column(Integer, ForeignKey("orders.id"))

    order = relationship("Order", back_populates="delivery")