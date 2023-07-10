#! python3
# -*- encoding: utf-8 -*-

class Url():

    def __init__(self) -> None:
        self.classUrl = 'http://zhongyi.alcxw.com/zhongyao/zyc.html'
        self.singBaseUrl = 'http://zhongyi.alcxw.com'
        self.singeBaseDetailUrl = ''
        self.userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

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