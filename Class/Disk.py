from Schemes.Disk import DiskBase

class Disk:
    def __init__(self,base:DiskBase):
        self.Trotation=(60000/base.rpm)/2
        self.Tseek=base.average_seek

        self.random={"Ttransfer":4000/(1024*base.max_transfer) }
        self.random['Tio']=self.Trotation+self.Tseek+self.random['Ttransfer']
        self.random['Rio']=4/self.random['Tio']


        self.secuential={"Ttransfer":100000/base.max_transfer}
        self.secuential['Tio']=self.Trotation+self.Tseek+self.secuential['Ttransfer']
        self.secuential['Rio']=100*1024/self.secuential['Tio']