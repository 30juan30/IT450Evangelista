#Class objective: supports two kinds of operations: attribute references and instantiation.
#attribute reference: use the standard syntax used for all attribute references in python
#Instantiation: uses function notation. parameterless function that returns an instance of the class
#creates a new instance of the class and assigns this object to the local variable
# __init__ method is used, instantiation automatically invokes "init" for the newly created class instance.
class Building:
#self: is used to refer to the instance attributes. it helps pass the instances automatically, but not received.
#not special to the code, just another object, helps distinguish normal names from attributes or function vs class method.
#functions float free, a class instance methos has to be aware of its parent.
    def __init__(self, south, west, width_WE, width_NS, height=10):
#def: is a block function of organized, reusable code that is used to perform a single, related action.    
        self.south = south
        self.west = west
        self.WE = width_WE
        self.NS = width_NS
        self.height = height
    def corners(self):
#"{}" is a literal character works by echoing back the literal itself. replacment fields below
        return {"north-west": [self.south + self.NS, self.west],
                "north-east": [self.south + self.NS, self.west + self.WE],
                "south-west": [self.south, self.west],
                "south-east": [self.south, self.west + self.WE]} 

    def area(self):
        return self.WE * self.NS

    def volume(self):
        return self.WE * self.NS * self.height
#format takes a format string an abitrary set of positional and keyword arguments. basically calls vformat.
#vformat does the actual work, separated to pass predefined dictionary arguments
#rather than unpacking and repacking the dictionart as an individual argument. format string into character data
    def __repr__(self):
        return 'Building({}, {}, {}, {}, {})'.format(self.south, self.west, self.WE, self.NS, self.height)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"

