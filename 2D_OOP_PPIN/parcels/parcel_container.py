# The goal of this module is to define the precipitation parcel class

class Parcel:
    #here i want to initialise the parcel attributes
    def __init__(self,x,y,dx,dy):
        self.x = x
        self.y = y
        self.dx = dx 
        self.dy = dy
    def init_parcels(self):
        pass
    
class Precip_parcel(Parcel):
    def __init__(self,nr,qr,dnr,dqr):
        self.nr = nr
        self.qr = qr
        self.dnr=dnr
        self.dqr=dqr
    