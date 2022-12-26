from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int]


class NameTechnic(BaseModelModify):
    video_card: str
    cooler: str
    motherboard: str


class LotOfGood(BaseModelModify):
    supplier_id: int
    time_date: str


class Technic(BaseModelModify):
    manifacture_id: int
    tech_name_id: int
    batch_id: int
    model: str
    warranty: str
    price: int


class Buyer(BaseModelModify):
    surname: str
    name: str
    patronymic: str
    phone: str


class Account(BaseModelModify):
    buyer_id: int
    discount: str
    date_time: str
    amount: int


class Sale(BaseModelModify):
    account_id: int
    tech_id: int
    quantity: str
    discount: str
