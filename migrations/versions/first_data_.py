"""empty message

Revision ID: first_data
Revises: a5f82400bb06
Create Date: 2022-12-14 02:17:41.978402

"""
from alembic import op
from sqlalchemy import orm
from src.models import Brand, Product, Enterprise, Order, Delivery
from datetime import date
# revision identifiers, used by Alembic.
revision = 'first_data'
down_revision = 'a5f82400bb06'
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    brand1 = Brand(name='Dior')
    brand2 = Brand(name='Nike')
    
    session.add_all([brand1, brand2])
    session.flush()


    enterprise1 = Enterprise(name='OOO Perfect', address='Улица Гоголя 11', phone="111-222")
    enterprise2 = Enterprise(name='ЗАО Карман', address='Улица Пушкина д. 12', phone="123-321")
    
    session.add_all([enterprise1, enterprise2])
    session.flush()

    product1 = Product(name="Кроссовки", amount=1, price=10000, brand_id=brand2.id)
    product2 = Product(name="Духи", amount=2, price=20000, brand_id=brand1.id)
    
    session.add_all([product1, product2])
    session.commit()

    order1 = Order(amount=1, date=date(2022, 12, 1), date_execute=date(2023, 1, 20), enterprise_id=enterprise1.id, product_id=product1.id)
    order2 = Order(amount=2, date=date(2022, 4, 1), date_execute=date(2022, 5, 1), enterprise_id=enterprise2.id, product_id=product2.id)
    
    session.add_all([order1,order2])
    session.commit()

    delivery = Delivery(amount=1, date_delivery=date(2022, 12, 30), order_id = order1.id)
    delivery1 = Delivery(amount=2, date_delivery=date(2022, 6, 30), order_id = order2.id)

    session.add_all([delivery,delivery1])
    session.commit()


def downgrade() -> None:
    pass
