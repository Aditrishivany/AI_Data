import time

from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session

from src.db.models import Inventory, Product, User
from src.db.mysql import SessionLocal, engine
from src.db.models import Base


def seed_users(db: Session) -> None:
    if db.query(User).count() > 0:
        return

    users = [
        User(name="Asha Kumar", email="asha@example.com", is_active=True),
        User(name="Rahul Verma", email="rahul@example.com", is_active=True),
        User(name="Sara Ali", email="sara@example.com", is_active=True),
    ]
    db.add_all(users)
    db.commit()


def seed_products_and_inventory(db: Session) -> None:
    if db.query(Product).count() > 0:
        return

    products = [
        Product(name="Wireless Mouse", description="2.4G ergonomic mouse", price=799.0),
        Product(name="Mechanical Keyboard", description="Blue switch keyboard", price=2499.0),
        Product(name="USB-C Hub", description="6-in-1 multiport hub", price=1799.0),
    ]
    db.add_all(products)
    db.commit()

    for product in products:
        db.refresh(product)
        db.add(Inventory(product_id=product.id, quantity=25))

    db.commit()


def run_seed() -> None:
    # MySQL container may need a few seconds before accepting connections.
    attempts = 10
    for attempt in range(1, attempts + 1):
        try:
            Base.metadata.create_all(bind=engine)
            db = SessionLocal()
            try:
                seed_users(db)
                seed_products_and_inventory(db)
            finally:
                db.close()
            return
        except OperationalError:
            if attempt == attempts:
                raise
            time.sleep(3)


if __name__ == "__main__":
    run_seed()
    print("Seed data inserted successfully.")
