from sqlalchemy.orm import Session

from src import models, schemas

def create_brand(db: Session, brand: schemas.BrandCreate):

    db_brand = models.Brand(**brand.dict())
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand

def create_enterprise(db: Session, enterprise: schemas.EnterpriseCreate):

    db_enterprise = models.Enterprise(**enterprise.dict())
    db.add(db_enterprise)
    db.commit()
    db.refresh(db_enterprise)
    return db_enterprise


def create_delivery(db: Session, delivery: schemas.DeliveryCreate, order_id: int):
 
    db_delivery = models.Delivery(**delivery.dict(), order_id=order_id)
    db.add(db_delivery)
    db.commit()
    db.refresh(db_delivery)
    return db_delivery

def create_product(db: Session, product: schemas.ProductCreate, brand_id: int):
 
    db_product = models.Product(**product.dict(), brand_id=brand_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def create_order(db: Session, order: schemas.OrderCreate, enterprise_id: int, product_id: int):
 
    db_order = models.Order(**order.dict(), enterprise_id=enterprise_id, product_id=product_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def get_product_by_id(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_order_by_id(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

def get_brand_by_id(db: Session, brand_id: int):
    return db.query(models.Brand).filter(models.Brand.id == brand_id).first()

def get_delivery_by_id(db: Session, delivery_id: int):
    return db.query(models.Delivery).filter(models.Delivery.id == delivery_id).first()

def get_enterprise_by_id(db: Session, enterprise_id: int):
    return db.query(models.Enterprise).filter(models.Enterprise.id == enterprise_id).first()



def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Order).offset(skip).limit(limit).all()

def get_enterprises(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Enterprise).offset(skip).limit(limit).all()

def get_deliveries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Delivery).offset(skip).limit(limit).all()

def get_brands(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Brand).offset(skip).limit(limit).all()


def get_brand_by_name(db: Session, name: str):
    return db.query(models.Brand).filter(models.Brand.name == name).first()

def get_enterprise_by_name(db: Session, name: str):
    return db.query(models.Enterprise).filter(models.Enterprise.name == name).first()



