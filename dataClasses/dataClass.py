from dataclasses import dataclass


"models - paczka"
"model"


@dataclass
class AdsApartment:
    link: str
    area: str
    district: str
    type_room: str
    price: float
    rent: float
    bills: float
    total: float
    image: list[str]


@dataclass
class AdsRoom:
    link: str
    district: str
    room: str
    price: float
    bills: float
    total: float
    image: list[str]


@dataclass
class AdsNewApartment:
    link: str
    area: str
    district: str
    type_room: str
    price: float
    rent: float
    bills: float
    total: float

