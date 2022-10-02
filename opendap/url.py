import urllib.request
import urllib.error

class URL:

    def __init__(self, url :str) -> None:

        try:
            request = urllib.request.urlopen(url)
        except urllib.error.URLError as e:
            print(e)
            print('You might set wrong url.')
            exit()
        
        if self.__is_disconnected(request):

            raise Exception(f'You can not connect OpenDap Server. Given URL might be wrong or Server is down now. Please Check -> {url}, responce {request.getcode()}')

        self._url : str = request.geturl()
    
    def __is_disconnected(self, request) -> bool:

        return request.getcode() != 200
    
    @property
    def url(self) -> str:

        return self._url
    
    def __str__(self) -> str:

        return str(self._url)


if __name__ == '__main__':

    oisst_avhrr_url = URL('http://aprc.soest.hawaii.edu:80/dods/public_data/NOAA_SST/OISST_AVHRR/daily_v2.1_1981-2015') # wrong url
    #oisst_avhrr_url = URL('http://apdrc.soest.hawaii.edu:80/dods/public_data/NOAA_SST/OISST_AVHRR/daily_v2.1_1981-2015') # correct url
    print(oisst_avhrr_url)
