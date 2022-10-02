from tkinter import W
from opendap.position import Position

class Latitude:

    MIN : float = -89.875
    MAX : float = 89.875

    def __init__(self, position :Position) -> None:

        if position.position < Latitude.MIN or Latitude.MAX < position.position:

            raise Exception(f'You set unavailable range. You should put value from {Latitude.MIN} to {Latitude.MAX}')
            
        self._latitude : Position = position
    
    @property
    def latitude(self) -> Position:

        return self._latitude
    
    def __str__(self) -> str:

        return str(self._latitude)
    
    def is_greater_than(self, latitude):

        return latitude.latitude.position < self.latitude.position

    def is_less_than(self, latitude):

        return self.latitude.position < latitude.latitude.position

if __name__ == '__main__':

    from position import Position
    RESOLUTION = 0.125
    p1 = Position(50, RESOLUTION)
    p2 = Position(80, RESOLUTION)
    p3 = Position(2000, RESOLUTION)

    south = Latitude(p1)
    north = Latitude(p2)
    print(south, north) # Read Latitude class __str__
    print(south.latitude, north.latitude) # Read Position class __str__

    error_lat = Latitude(p3)


