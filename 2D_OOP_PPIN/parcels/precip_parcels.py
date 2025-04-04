from parcels.parcels import Parcel
from constants import *
from math import pi,gamma,e
from fields.grid import Grid
class PrecipParcel(Parcel):

    def __init__(self, x, y, qr, nr, id):
        ##inheritance from the parcel Class
        super().__init__(x, y, id)
        self.qr = qr
        self.nr = nr
        self.dqr = None
        self.dnr = None

    def term_func(self,ro,D):
        """Calculates the velocity of the parcel."""
        if abel_shipway == True:
        
            #Abel and Shipway rain
            term = ((a1*D**b1)*(e**(g1*D)))\
                + (a2*(D**b2)*(e**(g2*D)))\
                    *(ro0/ro)**(f)
            
        else:
        
            term = ((a1*D**b1)*(e**(g1*D)))*(ro0/ro)**(f)
        return term
    
    def x_teleport(self):
        """Teleports the parcel to the other side of the domain if it goes out of bounds."""
        if self.x > x_extent:
            self.x = 0 +(self.x - x_extent)
            print('teleporting')
        elif self.x < 0:
            self.x = x_extent + self.x
            print('teleporting')

    def impinge(self,ro):
        """Returns the rainfall mass of an impinged parcel."""
        D = self.diameter(ro)
        return 522*(D**2.5)*self.nr


    def evaporation(self,temp,qv,ro,ws,diffus,visc,Lv):
        """Calculates the evaporation of the parcel."""
        #Slope calculation
        #Schmits number
        Sc = visc/diffus
        #Slope of the size distribution
        slope = ((pi/6)*(ro_r/ro)*(self.nr/self.qr)*(shape+1)*(shape+2)*(shape+3))**((1/3))
        
        #Ventilation coefficient
        vent_r = 2*pi*(self.nr)*ro* \
            (0.78*((1+shape)/(slope)) \
                    +  0.31*((a1*ro/visc)**(0.5))*(Sc**(1/3))*((ro0/ro)**(1/4))  \
                    * (gamma((0.5*b1 +shape +2.5))/gamma((1+shape))) \
                    *((1 + (0.5*f)/slope)**(-(0.5*b1 + shape + 2.5))) \
                    *((slope)**(-0.5*b1 -1.5)))
        #Thermodiffusion coefficient
        ABliq = ((Lv**2)/(Ka*Rv* (temp**2))) + (1/(ro*ws*diffus))
        ##Sink term for rainwater mass mixing ratio due to evaporation
        Prevp = (((qv/ws)-1)/(ro*ABliq))*vent_r
        ##Sink term for rainwater number concentration due to evaporation
        Nrevp = Prevp*((self.nr/ro)/self.qr)
        #Sink term for rainwater number concentration due to rain on rain aggregation
        Nracr = 8*(self.nr/ro)*self.qr*ro_r
        #Total sink of rainwater mass mixing ratio
        qr_dot =Prevp
        #Conditional logic to determine the relationship bettwen sink of mixing ratio and number concentration
    
        if inhomog == True:
            nr_dot = Nrevp -Nracr
            #Here the number concentration decreases by evaporation and aggregation
        elif inhomog == False:
            nr_dot = 0  - Nracr
            #Here aggregation is the only number concentration sink term
        return qr_dot,nr_dot
        


    def RK4(self,delt,t,xdot,ydot,nr_dot,qr_dot):
        """Calculates the new position of the parcel using the Runge-Kutta method."""
        
        for j in range(4):
        
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
    
    def diameter(self,ro):
        """Calculates the diameter of the parcel."""
        return ((ro/ro_r)*(self.qr/self.nr))**((1/3))

    def stats(self,D):
        """Returns the attributes of the parcel."""
        return f"Parcel 0: x={self.x}, y={self.y},qr={self.qr},nr={self.nr},D = {D})" 
    
    def move(self,grid,t,delt):
        """Moves the parcel to a new position after a time step, and updates its values."""
    
        #Interpolate values from grid
        temp, qv, ro ,ws,diffus,visc,Lv = grid.grid2par(x=self.x,y=self.y)
        
        #Calculate the average droplet diameter
        D = self.diameter(ro)
         
            

        #Calculate the velocity of the parcel
        y_dot = -self.term_func(ro,D)
        x_dot = 0
        
        
        #Evaporation step 
        qr_dot,nr_dot = self.evaporation(temp,qv,ro,ws,diffus,visc,Lv)
        
        
        #Now perfrom the Runge-Kutta method to update parcel attributes
        self.RK4(delt=delt,t=t,xdot=x_dot,ydot=y_dot,nr_dot=nr_dot,qr_dot=qr_dot)
        