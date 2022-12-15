from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from src import crud, models, schemas
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():

    db = SessionLocal() # pragma: no cover
    try:# pragma: no cover
        yield db# pragma: no cover
    finally:# pragma: no cover
        db.close()# pragma: no cover

@app.get("/brands/", response_model=list[schemas.Brand])
def read_brands(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    brands = crud.get_brands(db, skip=skip, limit=limit)
    return brands

@app.get("/brands/{brand_id}", response_model=schemas.Brand)
def read_brand_by_id(brand_id: int, db: Session = Depends(get_db)):

    db_brand = crud.get_brand_by_id(db, brand_id=brand_id)
    if db_brand is None:
        raise HTTPException(status_code=404, detail="Такого бренда нет")
    return db_brand

@app.post("/brands/", response_model=schemas.Brand)
def create_brand(brand: schemas.BrandCreate, db: Session = Depends(get_db)):

    db_brand = crud.get_brand_by_name(db, name=brand.name)
    if db_brand:
        raise HTTPException(status_code=400, detail="Такой бренд уже есть")
    return crud.create_brand(db=db, brand=brand)


@app.get("/enterprises/", response_model=list[schemas.Enterprise])
def read_enterprises(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    enterprises = crud.get_enterprises(db, skip=skip, limit=limit)
    return enterprises

@app.get("/enterprises/{enterprise_id}", response_model=schemas.Enterprise)
def read_enterprise_by_id(enterprise_id: int, db: Session = Depends(get_db)):

    db_enterprise = crud.get_enterprise_by_id(db, enterprise_id=enterprise_id)
    if db_enterprise is None:
        raise HTTPException(status_code=404, detail="Такого предприятия нет")
    return db_enterprise

@app.post("/enterprises/", response_model=schemas.Enterprise)
def create_enterprise(enterprise: schemas.EnterpriseCreate, db: Session = Depends(get_db)):

    db_enterprise = crud.get_enterprise_by_name(db, name=enterprise.name)
    if db_enterprise:
        raise HTTPException(status_code=400, detail="Такое предприятие уже есть")
    return crud.create_enterprise(db=db, enterprise=enterprise)



@app.post("/products/brand/{brand_id}/", response_model=schemas.Product)
def create_product(brand_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    
    return crud.create_product(db=db, product=product, brand_id=brand_id)

@app.get("/products/", response_model=list[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    products = crud.get_products(db, skip=skip, limit=limit)
    return products

@app.get("/products/{product_id}", response_model=schemas.Product)
def read_product_by_id(product_id: int, db: Session = Depends(get_db)):

    db_product = crud.get_product_by_id(db, product_id=product_id)
    
    return db_product




@app.post("/deliveries/order/{order_id}/", response_model=schemas.Delivery)
def create_delivery(order_id: int, delivery: schemas.DeliveryCreate, db: Session = Depends(get_db)):
    
    return crud.create_delivery(db=db, delivery=delivery, order_id=order_id)

@app.get("/deliveries/", response_model=list[schemas.Delivery])
def read_deliveries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    deliveries = crud.get_deliveries(db, skip=skip, limit=limit)
    return deliveries

@app.get("/deliveries/{delivery_id}", response_model=schemas.Delivery)
def read_delivery_by_id(delivery_id: int, db: Session = Depends(get_db)):

    db_delivery = crud.get_delivery_by_id(db, delivery_id=delivery_id)
    if db_delivery is None:
        raise HTTPException(status_code=404, detail="Такого ещё не присходило")
    return db_delivery

@app.post("/orders/{product_id}/{enterprise_id}/", response_model=schemas.Order)
def create_order(product_id: int, enterprise_id: int, order: schemas.OrderCreate, db: Session = Depends(get_db)):
    
    return crud.create_order(db=db, order=order, product_id=product_id, enterprise_id=enterprise_id)

@app.get("/orders/", response_model=list[schemas.Order])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    orders = crud.get_orders(db, skip=skip, limit=limit)
    return orders

@app.get("/orders/{order_id}", response_model=schemas.Order)
def read_order_by_id(order_id: int, db: Session = Depends(get_db)):

    db_order = crud.get_order_by_id(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Такого заказа нет")
    return db_order

