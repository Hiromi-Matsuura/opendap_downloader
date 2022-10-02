from opendap.position import Position

class Longitude:

    MIN : float = 0.125
    MAX : float = 359.875

    def __init__(self, position :Position) -> None:

        if position.position < Longitude.MIN or Longitude.MAX < position.position:

            raise Exception(f'You set unavailable range. You should put value from {Longitude.MIN} to {Longitude.MAX}')
            
        self._longitude : Position = position
    
    @property
    def longitude(self) -> Position:

        return self._longitude
    
    def __str__(self) -> str:

        return str(self._longitude)
    
    def is_grater_than(self, longitude) -> bool :

        return longitude.longitude.position < self.longitude.position

    def is_less_than(self, longitude) -> bool :

        return self.longitude.position < longitude.longitude.position

if __name__ == '__main__':

    RESOLUTION = 0.125
    p1 = Position(50, RESOLUTION)
    p2 = Position(250, RESOLUTION)
    p3 = Position(-2000, RESOLUTION)

    west = Longitude(p1)
    east = Longitude(p2)
    print(west, east) # Read Longtude class __str__
    print(west.longitude, east.longitude) # Read Position class __str__

    error_lon = Longitude(p3)


