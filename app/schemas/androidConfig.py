from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# ANDROID CONFIG SCHEMAS
class AndroidConfigBase(BaseModel):
    is_active: bool

class AndroidConfigCreate(AndroidConfigBase):
    pass

class AndroidConfig(AndroidConfigBase):
    id: str
    created_at: datetime
    updated_at: datetime | None = None
    deleted_at: datetime | None = None

    class Config:
        orm_mode = True

class AndroidConfigUpdate(BaseModel):
    is_active: Optional[bool] = None
