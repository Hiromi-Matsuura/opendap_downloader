class Longitude:

    MIN : float = 0.0
    MAX : float = 359.999

    def __init__(self, position :float) -> None:

        if position < Longitude.MIN or Longitude.MAX < position:

            raise Exception(f'You set unavailable range. You should put value from {Longitude.MIN} to {Longitude.MAX}')
            
        self._longitude : float = float(position)
    
    @property
    def longitude(self) -> float:

        return self._longitude
    
    def __str__(self) -> str:

        return str(self._longitude)
    
    def is_grater_than(self, longitude) -> bool :

        return longitude._longitude < self._longitude

    def is_less_than(self, longitude) -> bool :

        return self._longitude < longitude._longitude

if __name__ == '__main__':

    west = Longitude(40.0)
    east = Longitude(300.0)
    print(west, east) # Read Longtude class __str__

    error_lon = Longitude(360.0)


