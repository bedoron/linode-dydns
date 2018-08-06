from abc import ABCMeta, abstractmethod
import requests


class IPProvider(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self):
        pass


class RemoteIPProvider(IPProvider):
    def __init__(self, server_address):
        super(RemoteIPProvider, self).__init__()
        self._server_address = server_address

    def get(self):
        return requests.get(self._server_address).text.strip("\n")
