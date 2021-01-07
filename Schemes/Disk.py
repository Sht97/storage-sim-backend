from pydantic import BaseModel


class DiskBase(BaseModel):
    name: str
    capacity: float
    rpm: float
    average_seek: float
    max_transfer: float
    platters: int
    cache: int
