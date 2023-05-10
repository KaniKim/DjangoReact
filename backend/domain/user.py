import datetime
from dataclasses import dataclass


@dataclass
class User:
    id: str
    email: str
    nickname: str
    name: str
    is_active: bool
    is_staff: bool
    joined_date: datetime.datetime
    expired_date: datetime.datetime
    password: str
    ethereum_address: str
