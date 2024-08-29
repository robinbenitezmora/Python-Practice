import random, time, sys

MAX_NUM_SNAILS = 5
MAX_NAME_LENGTH = 10
MAX_SPEED = 10

class Snail:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def __str__(self):
        return self.name
    
    def __lt__(self, other):
        return self.speed < other.speed
    
    def __eq__(self, other):
        return self.speed == other.speed
    
    def __gt__(self, other):
        return self.speed > other.speed
    
    def __le__(self, other):
        return self.speed <= other.speed
    
    def __ge__(self, other):
        return self.speed >= other.speed
    
    def __ne__(self, other):
        return self.speed != other.speed
    
    def __hash__(self):
        return hash(self.name)
    
    def __repr__(self):
        return self.name
    
    def __eq__(self, other):
        return self.name == other.name and self.speed == other.speed
    
    def __ne__(self, other):
        return self.name != other.name or self.speed != other.speed
    
    def __hash__(self):
        return hash((self.name, self.speed))
    
    def __eq__(self, other):
        return self.name == other.name and self.speed == other.speed
    
    def __ne__(self, other):
        return self.name != other.name or self.speed != other.speed
    
    def __hash__(self):
        return hash((self.name, self.speed))
    
    def __eq__(self, other):
        return self.name == other.name and self.speed == other.speed
    
    def __ne__(self, other):
        return self.name != other.name or self.speed != other.speed
    
    def __hash__(self):
        return hash((self.name, self.speed))
    
    def __eq__(self, other):
        return self.name == other.name and self.speed == other.speed
    
    def __ne__(self, other):
        return self.name != other.name or self.speed != other.speed
    
    def __hash__(self):
        return hash((self.name, self.speed))
    
    def __eq__(self, other):
        return self.name == other.name and self.speed == other.speed
    
    def __ne__(self, other):
        return self.name != other.name or self.speed != other.speed
    
    def __hash__(self):
        return hash((self.name, self.speed))
    
    def __eq__(self, other):
        return self.name == other.name and self.speed == other.speed
    
    def __ne__(self, other):
        return self.name != other.name or self.speed != other.speed
    
    def __hash__(self):
        return hash((self.name, self.speed))
    
    def __eq__(self, other):
        return self.name == other.name and self.speed == other.speed
    
    def __ne__(self, other):
        return self.name != other.name or self.speed != other.speed
    
    def __hash__(self):
        return hash((self.name, self.speed))
    
    def __eq__(self, other):
        return self.name == other.name and self.speed == other.speed