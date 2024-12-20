from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date

# Assuming other related schemas like Address, CustomerGroup, etc., are defined elsewhere

# Base schema for Customer
class CustomerBase(BaseModel):
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    billing_address_id: Optional[str] = None
    residential_address_id: Optional[str] = None
    phone: Optional[str] = None
    has_account: bool = False
    dob: Optional[date] = None
    ss_number: Optional[str] = None
    role: Optional[str] = None
    status: Optional[str] = None
    balance: Optional[float] = None
    metadata: Optional[dict] = None

# Schema for creating new Customer
class CustomerCreate(CustomerBase):
    password_hash: str  # Including password hash for customer creation

# Schema for full Customer details, including relationships
class Customer(CustomerBase):
    id: int
    billing_address: Optional["Address"] = None  # Reference to Address schema, assuming it's defined elsewhere
    shipping_addresses: List["Address"] = []  # List of addresses
    orders: List["Order"] = []  # List of orders, assuming Order schema is defined
    bankInfo: List["BankInfo"] = []  # List of bank info, assuming BankInfo schema is defined
    groups: List["CustomerGroup"] = []  # List of groups, assuming CustomerGroup schema is defined
    residentialAddress: Optional["ResidentialAddress"] = None  # Reference to ResidentialAddress schema
    shop: List["Shop"] = []  # List of shops
    businessDetails: List["BusinessDetails"] = []  # List of business details
    customerSupport: List["CustomerSupport"] = []  # List of customer support records
    ownerDetails: List["OwnerDetails"] = []  # List of owner details
    personalDetails: List["PersonalDetails"] = []  # List of personal details
    buckyyOrder: List["BuckyyOrder"] = []  # List of Buckyy orders

    class Config:
        orm_mode = True  # To handle ORM model serialization

# Schema for updating Customer details
class CustomerUpdate(BaseModel):
    id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    billing_address_id: Optional[str] = None
    residential_address_id: Optional[str] = None
    phone: Optional[str] = None
    dob: Optional[date] = None
    ss_number: Optional[str] = None
    role: Optional[str] = None
    status: Optional[str] = None
    balance: Optional[float] = None
    password_hash: Optional[str] = None  # Optional password update

    class Config:
        orm_mode = True

