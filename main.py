from opendap import *
import datetime

def main():

    west  = Longitude(118.125)
    east  = Longitude(240.125)
    south = Latitude(20.125)
    north = Latitude(50.250)
    area  = Area(west, east, south, north)

    start = datetime.datetime(1993, 1, 1)
    end   = datetime.datetime(1993, 12, 31)
    span  = Span(start, end)

    start_near = datetime.datetime(2016, 1, 1)
    end_near   = datetime.datetime(2019, 12, 31)
    short_span = Span(start_near, end_near)

    url      = URL('http://apdrc.soest.hawaii.edu:80/dods/public_data/NOAA_SST/OISST_AVHRR/daily_v2.1_1981-2015')
    url_near = URL('http://apdrc.soest.hawaii.edu:80/dods/public_data/NOAA_SST/OISST_AVHRR/daily_v2.1_2016-near_present')

    downloader         = OISST_downloader(url, area, span)
    nearset_downloader = OISST_nearest_downloader(url_near, area, short_span)

    excecuter = Excecuter()
    excecuter.append(downloader)
    #excecuter.append(nearset_downloader)
    excecuter.dryrun_downloads()
    #excecuter.excecute_downloads()

if __name__ == '__main__':

    main()
