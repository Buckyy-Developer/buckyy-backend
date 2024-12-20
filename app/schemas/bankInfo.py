from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Base schema for BankInfo
class BankInfoBase(BaseModel):
    customer_id: Optional[str] = None
    signatory_number: Optional[int] = None
    bank_name: Optional[str] = None
    bank_branch: Optional[str] = None
    acc_name: Optional[str] = None
    bank_ac: Optional[str] = None
    sig_name: Optional[str] = None
    email: Optional[str] = None

# Schema for creating new BankInfo
class BankInfoCreate(BankInfoBase):
    pass

# Schema for representing BankInfo with full details (id, relationships)
class BankInfo(BankInfoBase):
    id: int
    customer: Optional["Customer"] = None  # Placeholder for customer relationship, to be defined later
    merchantReg: Optional[list] = None  # Placeholder for merchantReg relationship, to be defined later

    class Config:
        orm_mode = True  # To handle ORM model serialization

# Schema for updating BankInfo
class BankInfoUpdate(BaseModel):
    id: int
    signatory_number: Optional[int] = None
    bank_name: Optional[str] = None
    bank_branch: Optional[str] = None
    acc_name: Optional[str] = None
    bank_ac: Optional[str] = None
    sig_name: Optional[str] = None
    email: Optional[str] = None

    class Config:
        orm_mode = True
