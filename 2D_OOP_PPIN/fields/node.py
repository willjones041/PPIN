#This is where the node class is stored, this is the container for 
# information on the state and behaviour of a node object

class Node:
    def __init__(self,x,y,temp,qv,ro,ws):
        self.x = x
        self.y = y
        self.temp = temp
        self.qv = qv
        self.ro = ro
        self.ws = ws
    def __repr__(self):
        return f"Node({self.x}, {self.y})"
    