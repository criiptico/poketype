class Move:
    name = ""
    id = 0
    power = 0
    type = ""
    
    def superEffective(self):
        return int(self.power * 2) # Make sure it returns an int

    def notVeryEffective(self):
        return int(self.power / 2) # Make sure it returns an int
    
    def notEffective(self):
        return 0
    