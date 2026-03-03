from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    name: str
    email: EmailStr
    is_active: bool = True


class UserCreate(UserBase):
    password: str | None = None


class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    is_active: bool | None = None


class UserOut(UserBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}


class ProductBase(BaseModel):
    name: str
    description: str = ""
    price: float = Field(..., gt=0)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = Field(default=None, gt=0)


class ProductOut(ProductBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}


class InventoryBase(BaseModel):
    product_id: int
    quantity: int = Field(default=0, ge=0)


class InventoryCreate(InventoryBase):
    pass


class InventoryUpdate(BaseModel):
    quantity: int = Field(..., ge=0)


class InventoryOut(BaseModel):
    id: int
    product_id: int
    quantity: int
    updated_at: datetime
    product: ProductOut | None = None

    model_config = {"from_attributes": True}


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)


class OrderItemDirectCreate(OrderItemCreate):
    order_id: int


class OrderItemUpdate(BaseModel):
    quantity: int = Field(..., gt=0)


class OrderCreate(BaseModel):
    user_id: int
    items: list[OrderItemCreate]


class OrderStatusUpdate(BaseModel):
    status: str


class OrderItemOut(BaseModel):
    id: int
    product_id: int
    quantity: int
    unit_price: float
    line_total: float
    product: ProductOut | None = None

    model_config = {"from_attributes": True}


class OrderOut(BaseModel):
    id: int
    user_id: int
    status: str
    total_amount: float
    created_at: datetime
    items: list[OrderItemOut] = []

    model_config = {"from_attributes": True}


class ActivityLogCreate(BaseModel):
    action: str
    entity: str
    details: str


class ActivityLogOut(BaseModel):
    id: str
    action: str
    entity: str
    details: str
    timestamp: datetime


class AuthRegister(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(..., min_length=6)


class AuthLogin(BaseModel):
    email: EmailStr
    password: str


class AuthResponse(BaseModel):
    message: str
    user_id: int
    email: EmailStr
