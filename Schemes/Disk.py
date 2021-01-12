from pydantic import BaseModel, Field
from typing import Optional


class DiskBase(BaseModel):
    name: str
    capacity: float
    rpm:float= Field(..., gt=0, description="The rpm must be greater than zero")
    average_seek: float= Field(..., gt=0, description="The average seek must be greater than zero")
    max_transfer: float= Field(..., gt=0, description="The max transfer must be greater than zero")
    platters: int
    cache: int

