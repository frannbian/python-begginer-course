from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
    
State.ACTIVE
State.INACTIVE

State(0) #gonna print INACTIVE

list(State) # gonna show enums value