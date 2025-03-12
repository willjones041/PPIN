from parcels.parcels import Parcel
from constants import *
import math
from fields.grid import Grid
class PrecipParcel(Parcel):

    def __init__(self, x, y, qr, nr):
        super().__init__(x, y)
        self.qr = qr
        self.nr = nr
        self.dqr = None
        self.dnr = None

    def term_func(self):
        """Calculates the velocity of the parcel."""
        #Abel and Shipway rain
        term = ((a1*D**b1)*(math.e**(g1*D)))\
            + (a2*(D**b2)*(math.e**(g2*D)))\
                *(ro_air_p/ro_air_p)**(f)
        return term
    
    def evaporation(self,temp,qv,ro,ws):
        """Calculates the evaporation of the parcel."""
        #Slope calculation
        slope = ((math.pi*self.nr*ro_r*math.gamma(4+shape))/(6*self.qr*math.gamma(1+shape)))**(1/3)
        #Ventilation coefficient
        vent_r = 2*math.pi*self.nr*ro* \
            (0.78*((1+shape)/(slope)) \
                    +  0.31*((a1*ro/visc)**(0.5))*(Sc**(1/3))*((ro0/ro)**(1/4))  \
                    * (math.gamma((0.5*b1 +shape +2.5))/math.gamma((1+shape))) \
                    *((1 + (0.5*f)/slope)**(-(0.5*b1 + shape + 2.5))) \
                    *((slope)**(-0.5*b1 -1.5)))
        #This will be a call to get the grid temperatures and humidities!! Call 2 par2grid
        ABliq = ((Lv**2)/(Ka*Rv* (temp**2))) + (1/(ro*ws*diffus))
        qr_dot = (((qv/ws)-1)/(ro*ABliq))*vent_r

        if homog == True:
            nr_dot = qr_dot*(self.nr/self.qr) 
        elif homog == False:
            nr_dot = 0   
        return qr_dot,nr_dot
        


    def RK4(self,delt,t,xdot,ydot,nr_dot,qr_dot):
        """Calculates the new position of the parcel using the Runge-Kutta method."""
        
        for j in range(5):
        
            if j ==0:
                #x position
                self.dx= xdot
                self.x=self.x + cb[j]*self.dx*delt
                #y position
                self.dy= ydot
                self.y=self.y + cb[j]*self.dy*delt
                #number concentration
                self.dnr= nr_dot
                self.nr=self.nr + cb[j]*self.dnr*delt
                # mixing ratio
                self.dqr= qr_dot
                self.qr=self.qr + cb[j]*self.dqr*delt

            else:
                # internal time stepper
                t= t + cc[j]*delt

                # x position
                self.dx= ca[j]*self.dx + xdot 
                self.x= self.x + cb[j]*self.dx*delt

                # y position
                self.dy= ca[j]*self.dy + ydot
                self.y= self.y + cb[j]*self.dy*delt
                #number concentration
                self.dnr= ca[j]*self.dnr + nr_dot
                self.nr= self.nr + cb[j]*self.dnr*delt
                #mixing ratio
                self.dqr= ca[j]*self.dqr + qr_dot
                self.qr= self.qr + cb[j]*self.dqr*delt

    
    def move(self,grid,t,delt):
        """Moves the parcel to a new position after a time step."""
        #Interpolate values from grid
        temp, qv, ro ,ws = grid.grid2par(x=self.x,y=self.y)
        #First calculate the velocity of the parcel
        y_dot = self.term_func()
        x_dot = 0
        #Evaporation step 
        nr_dot,qr_dot = self.evaporation(temp,qv,ro,ws)
        #Now perfrom the Runge-Kutta method to update parcel attributes
        self.RK4(delt=delt,t=t,xdot=x_dot,ydot=y_dot,nr_dot=nr_dot,qr_dot=qr_dot)