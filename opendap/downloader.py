from abc import ABCMeta, abstractmethod

class Downloader(metaclass=ABCMeta):

    @abstractmethod
    def make_download_command(self):

        raise NotImplementedError()
