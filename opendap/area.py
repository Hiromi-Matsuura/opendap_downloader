from opendap.latitude import Latitude
from opendap.longitude import Longitude

class Area:

    def __init__(self, west, east, south, north) -> None:

        if not (isinstance(west, Longitude) and isinstance(east, Longitude)):

            raise Exception('1th and 2nd argument should be Longitude class')
        
        if not (isinstance(south, Latitude) and isinstance(north, Latitude)):

            raise Exception('3rd and 4th argumetn should be Latitude class')
        
        if  east.is_less_than(west):

            raise Exception('2nd Argument should be greater than 1th Argument')

        if  north.is_less_than(south):

            raise Exception('4th Argument should be greater than 3rd Argument')
        
        self._west  = west
        self._east  = east
        self._south = south
        self._north = north

    def parse_longitude(self) -> str:

        return f'{self._west},{self._east}'

    def parse_latitude(self) -> str:

        return f'{self._south},{self._north}'
        
if __name__ == '__main__':

    west = Longitude(40.125)
    east = Longitude(80.125)

    south = Latitude(-70.125)
    north = Latitude(20.875)

    area = Area(west, east, south, north)

    parsedtxt_lon = area.parse_longitude()
    parsedtxt_lat = area.parse_latitude()

    print(parsedtxt_lon)
    print(parsedtxt_lat)


