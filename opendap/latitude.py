class Latitude:

    MIN : float = -90.000
    MAX : float = 90.000

    def __init__(self, position :float) -> None:

        if position < Latitude.MIN or Latitude.MAX < position:

            raise Exception(f'You set unavailable range. You should put value from {Latitude.MIN} to {Latitude.MAX}')
            
        self._latitude : float = float(position)
    
    @property
    def latitude(self) -> float:

        return self._latitude
    
    def __str__(self) -> str:

        return str(self._latitude)
    
    def is_greater_than(self, latitude):

        return latitude._latitude < self._latitude

    def is_less_than(self, latitude):

        return self._latitude < latitude._latitude

if __name__ == '__main__':

    RESOLUTION = 0.125

    south = Latitude(50.0)
    north = Latitude(80.0)
    print(south, north) 

    err_point = 300.0
    error_lat = Latitude(err_point)


