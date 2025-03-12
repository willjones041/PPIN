from constants import *
import math
class Parcel:
    instances = []  # Class-level storage for all parcels

    def __init__(self, x, y):
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

    @classmethod
    def find_by_coordinates(cls, x, y):
        """Find a Parcel with specific coordinates"""
        return next((parcel for parcel in cls.instances if parcel.x == x and parcel.y == y), None)
    

# Creating instances of Parcel
num_parcels = 100
import random




