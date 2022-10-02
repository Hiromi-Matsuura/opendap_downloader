from abc import ABCMeta, abstractmethod
from typing import List

class Downloader(metaclass=ABCMeta):

    @abstractmethod
    def make_download_command(self):

        raise NotImplementedError()
