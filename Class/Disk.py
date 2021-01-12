from Schemes.Disk import DiskBase

class Disk:
    def __init__(self,base:DiskBase):
        self.Trotation=round((60000/base.rpm)/2,2)
        self.Tseek=base.average_seek

        self.random={"Ttransfer":round(4000/(1024*base.max_transfer),4)}
        self.random['Tio']=self.Trotation+self.Tseek+self.random['Ttransfer']
        self.random['Rio']=round(4/self.random['Tio'],4)


        self.secuential={"Ttransfer":round(100000/base.max_transfer,4)}
        self.secuential['Tio']=round(self.Trotation+self.Tseek+self.secuential['Ttransfer'],4)
        self.secuential['Rio']=round(100*1024/self.secuential['Tio'],3)