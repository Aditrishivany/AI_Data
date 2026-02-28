from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload

from src.db.models import Inventory, Order, OrderItem, Product, User
from src.dependencies import get_db
from src.schemas import OrderCreate, OrderOut, OrderStatusUpdate
from src.services.activity_logger import log_activity

router = APIRouter(prefix="/api/orders", tags=["Orders"])


@router.get("/", response_model=list[OrderOut])
def get_orders(db: Session = Depends(get_db)):
    return (
        db.query(Order)
        .options(joinedload(Order.items).joinedload(OrderItem.product))
        .order_by(Order.id.desc())
        .all()
    )


@router.get("/{order_id}", response_model=OrderOut)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = (
        db.query(Order)
        .options(joinedload(Order.items).joinedload(OrderItem.product))
        .filter(Order.id == order_id)
        .first()
    )
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return order


@router.post("/", response_model=OrderOut, status_code=status.HTTP_201_CREATED)
async def create_order(payload: OrderCreate, db: Session = Depends(get_db)):
    user = db.get(User, payload.user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if not payload.items:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Order must contain items")

    order = Order(user_id=payload.user_id, status="created", total_amount=0.0)
    db.add(order)
    db.flush()

    total = 0.0
    for item in payload.items:
        product = db.get(Product, item.product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product id {item.product_id} not found",
            )

        inventory_item = db.query(Inventory).filter(Inventory.product_id == item.product_id).first()
        if not inventory_item or inventory_item.quantity < item.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Insufficient stock for product id {item.product_id}",
            )

        line_total = product.price * item.quantity
        total += line_total
        inventory_item.quantity -= item.quantity

        db.add(
            OrderItem(
                order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                unit_price=product.price,
                line_total=line_total,
            )
        )

    order.total_amount = total
    db.commit()
    db.refresh(order)

    await log_activity("CREATE", "ORDER", f"Created order id: {order.id} for user id: {order.user_id}")

    return (
        db.query(Order)
        .options(joinedload(Order.items).joinedload(OrderItem.product))
        .filter(Order.id == order.id)
        .first()
    )


@router.patch("/{order_id}/status", response_model=OrderOut)
async def update_order_status(order_id: int, payload: OrderStatusUpdate, db: Session = Depends(get_db)):
    order = db.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")

    order.status = payload.status
    db.commit()
    db.refresh(order)

    await log_activity("UPDATE", "ORDER", f"Updated order id: {order.id} to status: {order.status}")

    return (
        db.query(Order)
        .options(joinedload(Order.items).joinedload(OrderItem.product))
        .filter(Order.id == order.id)
        .first()
    )


@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = db.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")

    db.delete(order)
    db.commit()
    await log_activity("DELETE", "ORDER", f"Deleted order id: {order_id}")

