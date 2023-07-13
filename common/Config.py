#! python3
# -*- encoding: utf-8 -*-

_isOpenProxy = False

class Url():

    def __init__(self) -> None:
        self._classUrl = 'http://zhongyi.alcxw.com/zhongyao/zyc.html'
        self._singBaseUrl = 'http://zhongyi.alcxw.com'
        self._singeBaseDetailUrl = ''
        self._userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        self._proxies = {
            'http': 'http://xxxx'
        }

    @property
    def get_proxies(self):
        return self._proxies if _isOpenProxy else None

    @property
    def get_class_url(self):
        return self._classUrl
    
    def get_single_url(self, param):
        # TODO parse Url ?
        return self._singBaseUrl + param

    def get_single_detail_url(self, param):
        # TODO parse Url ?
        return self._singeBaseDetailUrl + param
