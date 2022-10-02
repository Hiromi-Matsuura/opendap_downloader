from tkinter import W
import subprocess

class Excecuter:

    def __init__(self) -> None:

        self._downloders = []
    
    def excecute_downloads(self) -> None:

        if len(self._downloders) == 0:

            raise Exception ('You should put downloaders in the Excecuter class before excecuting download')
        
        for downloder in self._downloders:

            command = downloder.make_download_command()
            print(command)
            process = subprocess.run(command, encoding='utf-8', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            print(f'{process.stdout}')
            print()

    def dryrun_downloads(self) -> None:

        if len(self._downloders) == 0:

            raise Exception ('You should put downloaders in the Excecuter class before excecuting download')
        
        for downloder in self._downloders:

            command = downloder.make_download_command()
            print(command)

    def append(self, downloader) -> None:

        self._downloders.append(downloader)

if __name__ == '__main__':

    from opendap import *
    import datetime

    url = URL('http://apdrc.soest.hawaii.edu:80/dods/public_data/NOAA_SST/OISST_AVHRR/daily_v2.1_1981-2015')

    west  = Longitude(118.125)
    east  = Longitude(240.125)
    south = Latitude(20.125)
    north = Latitude(50.250)
    area  = Area(west, east, south, north)

    start = datetime.datetime(1993, 1, 1)
    end   = datetime.datetime(1994, 12, 31)
    span  = Span(start, end)

    url_s = URL('http://apdrc.soest.hawaii.edu:80/dods/public_data/NOAA_SST/OISST_AVHRR/daily_v2.1_2016-near_present')
    start_s  = datetime.datetime(2016, 1, 1)
    end_s    = datetime.datetime(2019, 12, 31)
    short_span = Span(start_s, end_s)

    downloader         = OISST_downloader(url, area, span)
    nearset_downloader = OISST_nearest_downloader(url_s, area, short_span)

    excecuter  = Excecuter()
    excecuter.append(downloader)
    excecuter.append(nearset_downloader)
    excecuter.excecute_download()