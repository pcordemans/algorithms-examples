class Robot:
    def __init__(self, name):
        self.__name = name

    def __eq__(self, other):
        return isinstance(other, Robot) and self.get_name() == other.get_name()
    
    def get_name(self):
        return self.__name

    def __repr__(self):
        return self.get_name()

ro = Robot("ro")
print(str(ro))