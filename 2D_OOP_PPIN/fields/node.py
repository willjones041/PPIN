#This is where the node class is stored, this is the container for 
# information on the state and behaviour of a node object

class Node:
    instances = []

    def __init__(self, x, y, temp, qv, ro, ws,diffus,visc,Lv):
        """""Initializes a Node object with the given parameters."""
        self.x = x
        self.y = y
        self.temp = temp
        self.qv = qv
        self.ro = ro
        self.ws = ws
        self.diffus = diffus
        self.visc = visc
        self.Lv = Lv
        Node.instances.append(self)

    def __repr__(self):
        """Returns a string representation of the Node object."""
        return f"Node({self.x}, {self.y},{self.temp},{self.qv},{self.ro},{self.ws})"

    @classmethod
    def get_all_instances(cls):
        """Returns a list of all Node instances."""
        return cls.instances