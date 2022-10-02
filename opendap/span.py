class Span:

    def __init__(self, start: 'datetime', end: 'datetime'):

        if end < start:

            raise Exception(f' First argument Time {start} should be before Second argument Time {end}')
        
        self._start: 'datetime' = start
        self._end: 'datetime'   = end

    @property
    def start(self) -> 'datetime':

        return self._start
    
    @property
    def end(self) -> 'datetime':

        return self._end
    
    def parse(self):

        return f'{self.start.strftime("%Y-%m-%d %H:%M:%S")},{self.end.strftime("%Y-%m-%d %H:%M:%S")}'


if __name__ == '__main__':

    import datetime

    start = datetime.datetime(1982, 1, 1)
    end   = datetime.datetime(2015, 1, 1)

    span  = Span(start, end)
    #span  = Span(end, start) # Raise Exception

    print(span.start)
    print(span.end)
    txt = span.parse()
    print(txt)

