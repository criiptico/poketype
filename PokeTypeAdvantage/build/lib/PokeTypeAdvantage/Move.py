from typing import Optional

class Move: # Data structure for the standard info of a move
    def __init__(self):
        self.name: str
        self.id: int
        self.power: Optional[int]
        self.type: str
    
    