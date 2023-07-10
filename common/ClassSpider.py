#! python3
# -*- encoding: utf-8 -*-
import requests
from common.Config import Url
from bs4 import BeautifulSoup

_url = Url()

class ClassificationSpider(object):

    def __init__(self) -> None:
        self._result = []
    
    def start(self):
        # 获取HTML
        doc_html = requests.get(_url.getClassUrl).text
        print('正在爬取全部分类信息...')
        self.parse_html_doc(doc_html)
    
    def parse_html_doc(self, doc_html):
        html_data = BeautifulSoup(doc_html)
        result = []
        left_box_panel = html_data.select('div.mainbox div.panel')[0]
        for i in range(len(left_box_panel.select('h3'))):
            item_result = []
            for j in range(len(left_box_panel.select('ul')[i].select('li a'))):
                item_result.append({
                    'name': left_box_panel.select('ul')[i].select('li a')[j].string,
                    'href': left_box_panel.select('ul')[i].select('li a')[j]['href']
                })
            result.append({
                'name': left_box_panel.select('h3')[i].string,
                'sub_list': item_result
            })
        self._result = result

    @property
    def getResult(self):
        return self._result

class SecondFlSpider(object):

    def __init__(self, first_result) -> None:
        self._first_result = first_result
        self._result = []

    def start(self):
        # 轮流查询分类信息
        for ind in range(len(self._first_result)):
            cur_fl_data = self._first_result[ind]
            result_list = []
            if cur_fl_data['sub_list']:
                for sub_ind in range(len(cur_fl_data['sub_list'])):
                    sub_data = cur_fl_data['sub_list'][sub_ind]
                    if sub_data['href']:
                        print('正在爬取 -> ', cur_fl_data['name'], '_', sub_data['name'], '...')
                        html_doc = requests.get(_url.singBaseUrl + sub_data['href']).text
                        parse_html_doc_result = self.parse_html_doc(html_doc)
                        result_list.append({
                            'name': sub_data['name'],
                            'result_list': parse_html_doc_result
                        })
            self._result.append({
                'name' : cur_fl_data['name'],
                'result_list': result_list
            })
    
    def parse_html_doc(self, html_doc):
        _result = []
        html_data = BeautifulSoup(html_doc)
        if html_data is None:
            # 爬取失败。。。
            pass
        # 第一位 div.panel 是导航路由忽略
        main_box_data = html_data.select('div.mainbox > div.leftbox > div.panel')
        for ind in range(len(main_box_data)):
            if ind != 0:
                panel_data = main_box_data[ind]
                panel_result = {}
                if panel_data.select('span.f24 a'):
                    panel_result['name'] = panel_data.select('span.f24 a')[0].string
                if panel_data.select('div.l250 > p'):
                    panel_result['note'] = panel_data.select('div.l250 > p')[0].string
                if panel_data.select('div.l250 > div.dh')[0]:
                    panel_result['cn_name'] = panel_data.select('div.l250 > div.dh')[0].select('span.mr')[0].string
                if panel_data.select('div.l250 > div.dh')[1]:
                    panel_result['alia_name'] = panel_data.select('div.l250 > div.dh')[1].select('span.mr')[0].string
                if panel_data.select('div.l250 > div.dh')[2]:
                    panel_result['fl_name'] = panel_data.select('div.l250 > div.dh')[2].select('span.mr')[0].string
                _result.append(panel_result)
        return _result

    @property
    def get_result(self):
        return self._result