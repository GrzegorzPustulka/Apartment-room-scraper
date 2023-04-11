from dataclasses import dataclass


"models - paczka"
"model"


@dataclass
class AdsApartment:
    link: str
    source: str
    area: str
    district: str
    room_type: str
    price: float
    rent: float
    bills: float
    total: float
    indicators: int
    date: str
    images: list[str]


@dataclass
class AdsRoom:
    link: str
    source: str
    district: str
    room_type: str
    price: float
    bills: float
    total: float
    date: str
    images: list[str]
