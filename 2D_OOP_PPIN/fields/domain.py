# here is the domain class where we store info on domains attributes and behaviours
from fields.grid import Grid
import random
from constants import *
from parcels.precip_parcels import *
class Domain:
    def __init__(self,x_extent,y_extent,origin,num_parcels):# Initiating attributes
        self.x_extent = x_extent
        self.y_extent = y_extent
        self.origin = origin #(x,y) tuple
        self.num_parcels = num_parcels
    #Now defining methods of a domain object
    def create_grid(self,num_x,num_y):
        """Creates a grid based on this domain"""
        return Grid(self, num_x, num_y)
    
    def create_parcels(self):
        """Creates parcels based on this domain"""
        for i in range(num_parcels):
            x = self.x_extent*0.5#random.random()*self.x_extent + self.origin[0]
            y = init_y_parcels#random.gauss(y_extent,std_dev_y_parcels)
            qr = qr0
            nr = nr0#nrlower + (nrupper - nrlower)*random.random()
            id = i
            PrecipParcel(x=x,y=y,qr=qr,nr=nr,id=id)

    def atmospheric_profile(self,x,y):
        ##Here I can change the atmospheric profile i.e options for isothermal
        ## or stratified etc.
        if isothermal ==True:
                    temp = T0
                    p = P0*math.e**(-(g*y)/(Rd*temp))
                    ws = 3.8/(p*math.e**(-17.2693882*(temp-273.15)/(temp-35.86))-6.109)
                    qv = RHenv*ws
                    ro = p/(Rd*temp)
                    #using smithsonian meteorological tables
                    diffus = ((temp/T_standard)**(1.81))*(P_standard/p)*(diffus_standard)
                    # using Sutherlands law
                    dyn_visc = (dyn_visc_standard*(temp/T_standard)**(3/2))*((T_standard/suth_const)/(temp+suth_const))
                    visc = dyn_visc/ro
                    #using watsons equation
                    Lv = Lv_standard*((T_critical-temp)/(T_critical-T_boil))
                    #print(f'pressure = {p},ro={ro}, (x,y)=({x},{y})')
        return temp,ws,qv,ro,diffus,visc,Lv
    