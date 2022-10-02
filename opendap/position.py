class Position:

    def __init__(self, position :float, resolution: float) -> None:

        assert self.__is_comletly_divided_by(position, resolution), f' position({position}) is not comlety divided by resolution({resolution})'

        self._position : float = position
    
    def __is_comletly_divided_by(self, position :float, resolution : float) -> bool :

        return (position % resolution) == 0
    
    @property
    def position(self) -> float:

        return self._position
    
    def __str__(self) -> str:

        return str(self._position)


if __name__ == '__main__':

    RESOLUTION = 0.125
    p1 = Position(50, RESOLUTION)
    p2 = Position(250.125, RESOLUTION)
    p3 = Position(250.625, RESOLUTION)
    print(p1.position, p2.position, p3.position)
    p4 = Position(340.2, RESOLUTION)

