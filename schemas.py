from pydantic import BaseModel, Field
from datetime import datetime

class WidgetBase(BaseModel):
    name: str = Field(..., max_length=64)
    number_of_parts: int

class WidgetCreate(WidgetBase):
    pass

class WidgetUpdate(WidgetBase):
    pass

class Widget(WidgetBase):
    id: int
    created_date: datetime
    updated_date: datetime

    class Config:
        orm_mode = True
