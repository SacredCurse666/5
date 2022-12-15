from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main import app, get_db
from src.models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite_base.db"  # Тестовая БД

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)  # Удалем таблицы из БД
Base.metadata.create_all(bind=engine)  # Создаем таблицы в БД


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db  # Делаем подмену

client = TestClient(app)  # создаем тестовый клиент к нашему приложению



def test_create_brand():
    response = client.post(
        "/brands/",
        json={"name": "Тестовый бренд"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Тестовый бренд"

def test_create_exist_brand():
    response = client.post(
        "/brands/",
        json={"name": "Тестовый бренд"}
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Такой бренд уже есть"

def test_read_brands():
    response = client.get("/brands/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["name"] == "Тестовый бренд"

def test_get_brand_by_id():
    response = client.get("/brands/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Тестовый бренд"

def test_brand_not_found():
    response = client.get("/brands/2")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Такого бренда нет"





def test_create_enterprise():
    response = client.post(
        "/enterprises/",
        json={"name": "test1","address":"test address", "phone": "phone" }
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "test1"
    assert data["address"] == "test address"
    assert data["phone"] == "phone"

def test_create_exist_enterprise():
    response = client.post(
        "/enterprises/",
        json={"name": "test1","address":"test address", "phone": "phone" }
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Такое предприятие уже есть"

def test_read_enterprises():
    response = client.get("/enterprises/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["name"] == "test1"

def test_get_enterprise_by_id():
    response = client.get("/enterprises/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "test1"

def test_enterprise_not_found():
    response = client.get("/enterprises/2")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Такого предприятия нет"



def test_create_product():
    response = client.post(
        "/products/brand/1/",
        json={"name": "tested", "amount": 100, "price": 1}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "tested"
    assert data["amount"] == 100
    assert data["price"] == 1
    assert data["brand_id"] == 1


def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["name"] == "tested"
    assert data[0]["amount"] == 100
    assert data[0]["price"] == 1
    assert data[0]["brand_id"] == 1

def test_get_product_by_id():
    response = client.get("/products/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "tested"



def test_create_order():
    response = client.post(
        "/orders/1/1/",
        json={"amount": 1, "date": "2020-10-10", "date_execute": "2020-10-20"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["amount"] == 1
    assert data["date"] == "2020-10-10"
    assert data["date_execute"] == "2020-10-20"
    assert data["product_id"] == 1
    assert data["enterprise_id"] == 1


def test_get_orders():
    response = client.get("/orders/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["amount"] == 1
    assert data[0]["date"] == "2020-10-10"
    assert data[0]["date_execute"] == "2020-10-20"
    assert data[0]["product_id"] == 1
    assert data[0]["enterprise_id"] == 1


def test_get_order_by_id():
    response = client.get("/orders/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["amount"] == 1

def test_product_not_found():
    response = client.get("/orders/3")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Такого заказа нет"


def test_create_delivery():
    response = client.post(
        "/deliveries/order/1/",
        json={"amount": 1, "date_delivery": "2020-11-10"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["amount"] == 1
    assert data["date_delivery"] == "2020-11-10"
    assert data["order_id"] == 1


def test_get_deliveries():
    response = client.get("/deliveries/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["amount"] == 1
    assert data[0]["date_delivery"] == "2020-11-10"
    assert data[0]["order_id"] == 1



def test_get_delivery_by_id():
    response = client.get("/deliveries/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["amount"] == 1

def test_delivery_not_found():
    response = client.get("/deliveries/3")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Такого ещё не присходило"


