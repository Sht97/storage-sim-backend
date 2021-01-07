from fastapi import APIRouter
from typing import List
from Schemes.Disk import DiskBase
from Class.Calcule import Calcule

router = APIRouter()


@router.post("/compare/")
async def compare_disks(disks: List[DiskBase]):
    calcule=Calcule(disks)
    return {"result": calcule.getCalcules()}
