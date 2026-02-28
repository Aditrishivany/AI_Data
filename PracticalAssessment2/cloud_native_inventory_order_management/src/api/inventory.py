from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload

from src.db.models import Inventory, Product
from src.dependencies import get_db
from src.schemas import InventoryCreate, InventoryOut, InventoryUpdate
from src.services.activity_logger import log_activity

router = APIRouter(prefix="/api/inventory", tags=["Inventory"])


@router.get("/", response_model=list[InventoryOut])
def get_inventory(db: Session = Depends(get_db)):
    return (
        db.query(Inventory)
        .options(joinedload(Inventory.product))
        .order_by(Inventory.id.desc())
        .all()
    )


@router.get("/{inventory_id}", response_model=InventoryOut)
def get_inventory_item(inventory_id: int, db: Session = Depends(get_db)):
    item = (
        db.query(Inventory)
        .options(joinedload(Inventory.product))
        .filter(Inventory.id == inventory_id)
        .first()
    )
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inventory item not found")
    return item


@router.post("/", response_model=InventoryOut, status_code=status.HTTP_201_CREATED)
async def create_inventory(payload: InventoryCreate, db: Session = Depends(get_db)):
    product = db.get(Product, payload.product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    if db.query(Inventory).filter(Inventory.product_id == payload.product_id).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inventory already exists for this product",
        )

    item = Inventory(**payload.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)

    await log_activity("CREATE", "INVENTORY", f"Added inventory for product id: {payload.product_id}")
    return (
        db.query(Inventory)
        .options(joinedload(Inventory.product))
        .filter(Inventory.id == item.id)
        .first()
    )


@router.put("/{inventory_id}", response_model=InventoryOut)
async def update_inventory(inventory_id: int, payload: InventoryUpdate, db: Session = Depends(get_db)):
    item = db.get(Inventory, inventory_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inventory item not found")

    item.quantity = payload.quantity
    db.commit()
    db.refresh(item)

    await log_activity("UPDATE", "INVENTORY", f"Updated inventory id: {inventory_id}")
    return (
        db.query(Inventory)
        .options(joinedload(Inventory.product))
        .filter(Inventory.id == item.id)
        .first()
    )


@router.delete("/{inventory_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_inventory(inventory_id: int, db: Session = Depends(get_db)):
    item = db.get(Inventory, inventory_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inventory item not found")

    db.delete(item)
    db.commit()
    await log_activity("DELETE", "INVENTORY", f"Deleted inventory id: {inventory_id}")
