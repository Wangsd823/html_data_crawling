#! python3
# -*- encoding: utf-8 -*-

class Url():

    def __init__(self) -> None:
        self.classUrl = ''
        self.singBaseUrl = ''
        self.singeBaseDetailUrl = ''

    @property
    def getClassUrl(self):
        return self.classUrl
    
    @property
    def getSingleUrl(self, param):
        # TODO parse Url ?
        return self.singBaseUrl + param

    @property
    def getSingleUrl(self, param):
        # TODO parse Url ?
        return self.singeBaseDetailUrl + param