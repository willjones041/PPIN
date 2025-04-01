from constants import *
import math
class Parcel:
    instances = []  # Class-level storage for all parcels

    def __init__(self, x, y,id):
        self.id = id
        self.x = x
        self.y = y
        self.dx = None
        self.dy = None
        Parcel.instances.append(self)  # Automatically add instance to storage

    def clear_parcel(self):
        """Remove this Parcel instance from storage"""
    
        Parcel.instances.remove(self)   
    
    @classmethod
    def get_all(cls):
        """Returns all stored Parcel instances"""
        return cls.instances

    @classmethod
    def clear_all(cls):
        """Removes all stored Parcel instances"""
        cls.instances.clear()
    






