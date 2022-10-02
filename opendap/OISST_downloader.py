from typing import List
from opendap.downloader import Downloader
import datetime

class OISST_downloader(Downloader):

    MIN_TIME = datetime.datetime(1981, 9, 1)
    MAX_TIME = datetime.datetime(2015, 12 ,31)

    def __init__(self, url, area, span) -> None:

        if not (OISST_downloader.MIN_TIME <= span.start and span.end <= OISST_downloader.MAX_TIME):

            raise Exception(f'This downloader only be able to accsess the time from {OISST_downloader.MIN_TIME} to {OISST_downloader.MAX_TIME}')

        self._url  = url
        self._area = area
        self._span = span
    
    def make_download_command(self) -> List[str]:

        command   = self.__ncks()
        save_name = self.__save_name()
        command.append(save_name)
        
        return command

    def __ncks(self) -> List[str]:

        parsed_txt_time = self._span.parse()
        parsed_txt_lon  = self._area.parse_longitude()
        parsed_txt_lat  = self._area.parse_latitude()

        command = ['ncks', '--netcdf4', '-D1', '-d', 'time,'+parsed_txt_time, \
                                               '-d', 'lon,'+parsed_txt_lon,  \
                                               '-d', 'lat,'+parsed_txt_lat,  \
                                               f'{self._url.url}', '-O']
        return command
    
    def __save_name(self) -> str:

        start = self._span.start.strftime('%Y-%m-%d')
        end   = self._span.end.strftime('%Y-%m-%d')

        return f'{start}_{end}.nc'

class OISST_nearest_downloader(Downloader):

    MIN_TIME = datetime.datetime(2016, 1, 1)
    MAX_TIME = datetime.datetime.now()

    def __init__(self, url, area, span) -> None:

        if not (OISST_nearest_downloader.MIN_TIME <= span.start and span.end <= OISST_nearest_downloader.MAX_TIME):

            raise Exception(f'This downloader only be able to accsess the time from {OISST_nearest_downloader.MIN_TIME} to {OISST_nearest_downloader.MAX_TIME}')

        self._url  = url
        self._area = area
        self._span = span
    
    def make_download_command(self) -> List[str]:

        command   = self.__ncks()
        save_name = self.__save_name()
        command.append(save_name)
        
        return command

    def __ncks(self) -> List[str]:

        parsed_txt_time = self._span.parse()
        parsed_txt_lon  = self._area.parse_longitude()
        parsed_txt_lat  = self._area.parse_latitude()

        command = ['ncks', '--netcdf4', '-D1', '-d', 'time,'+parsed_txt_time, \
                                               '-d', 'lon,'+parsed_txt_lon,  \
                                               '-d', 'lat,'+parsed_txt_lat,  \
                                               f'{self._url.url}', '-O']
        return command
    
    def __save_name(self) -> str:

        start = self._span.start.strftime('%Y-%m-%d')
        end   = self._span.end.strftime('%Y-%m-%d')

        return f'{start}_{end}.nc'

if __name__ == '__main__':

    from longitude import Longitude
    from latitude import Latitude
    from area import Area
    from span import Span
    from url import URL
    import datetime

    url   = URL('http://apdrc.soest.hawaii.edu:80/dods/public_data/NOAA_SST/OISST_AVHRR/daily_v2.1_1981-2015')

    RESOLUTION = 0.125
    west  = Longitude(118.125)
    east  = Longitude(240.125)
    south = Latitude(20.125)
    north = Latitude(50.250)
    area  = Area(west, east, south, north)

    start  = datetime.datetime(1993, 1, 1)
    end    = datetime.datetime(2015, 12, 31)
    span   = Span(start, end)

    url_s = URL('http://apdrc.soest.hawaii.edu:80/dods/public_data/NOAA_SST/OISST_AVHRR/daily_v2.1_2016-near_present')
    start_s  = datetime.datetime(2016, 1, 1)
    end_s    = datetime.datetime(2019, 12, 31)
    short_span = Span(start_s, end_s)

    downloader         = OISST_downloader(url, area, span)
    nearest_downloader = OISST_nearest_downloader(url_s, area, short_span)
    command = downloader.make_download_command()
    print(command)

    command_s = nearest_downloader.make_download_command()
    print(command_s)
