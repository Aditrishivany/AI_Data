from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload

from src.db.models import Order, OrderItem, Product
from src.dependencies import get_db
from src.schemas import OrderItemDirectCreate, OrderItemOut, OrderItemUpdate
from src.services.activity_logger import log_activity

router = APIRouter(prefix="/api/order-items", tags=["Order Items"])


@router.get("/", response_model=list[OrderItemOut])
def get_order_items(db: Session = Depends(get_db)):
    return (
        db.query(OrderItem)
        .options(joinedload(OrderItem.product))
        .order_by(OrderItem.id.desc())
        .all()
    )


@router.get("/{item_id}", response_model=OrderItemOut)
def get_order_item(item_id: int, db: Session = Depends(get_db)):
    item = (
        db.query(OrderItem)
        .options(joinedload(OrderItem.product))
        .filter(OrderItem.id == item_id)
        .first()
    )
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order item not found")
    return item


@router.post("/", response_model=OrderItemOut, status_code=status.HTTP_201_CREATED)
async def create_order_item(payload: OrderItemDirectCreate, db: Session = Depends(get_db)):
    order = db.get(Order, payload.order_id)
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")

    product = db.get(Product, payload.product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    line_total = product.price * payload.quantity
    item = OrderItem(
        order_id=payload.order_id,
        product_id=payload.product_id,
        quantity=payload.quantity,
        unit_price=product.price,
        line_total=line_total,
    )
    db.add(item)

    order.total_amount += line_total
    db.commit()
    db.refresh(item)

    await log_activity("CREATE", "ORDER_ITEM", f"Created order item id: {item.id}")
    return (
        db.query(OrderItem)
        .options(joinedload(OrderItem.product))
        .filter(OrderItem.id == item.id)
        .first()
    )


@router.put("/{item_id}", response_model=OrderItemOut)
async def update_order_item(item_id: int, payload: OrderItemUpdate, db: Session = Depends(get_db)):
    item = db.get(OrderItem, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order item not found")

    order = db.get(Order, item.order_id)
    old_total = item.line_total
    item.quantity = payload.quantity
    item.line_total = item.unit_price * payload.quantity

    if order:
        order.total_amount = order.total_amount - old_total + item.line_total

    db.commit()
    db.refresh(item)
    await log_activity("UPDATE", "ORDER_ITEM", f"Updated order item id: {item.id}")
    return (
        db.query(OrderItem)
        .options(joinedload(OrderItem.product))
        .filter(OrderItem.id == item.id)
        .first()
    )


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order_item(item_id: int, db: Session = Depends(get_db)):
    item = db.get(OrderItem, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order item not found")

    order = db.get(Order, item.order_id)
    if order:
        order.total_amount -= item.line_total

    db.delete(item)
    db.commit()
    await log_activity("DELETE", "ORDER_ITEM", f"Deleted order item id: {item_id}")

