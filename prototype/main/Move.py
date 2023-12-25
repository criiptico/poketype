from pydantic import BaseModel
from typing import Any, Dict, List

class Move(BaseModel): # Data structure for the standard info of a move
    name: str
    url: str
    # id: int
    # power: int
    type: str
    
    