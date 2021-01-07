from Schemes.Disk import DiskBase
from typing import List
from Class.Disk import Disk


class Calcule:
    def __init__(self, disks: List[DiskBase]):
        self.calcules=[]
        for i in disks:
            self.calcules.append(Disk(i))

    def getCalcules(self):
        return self.calcules

