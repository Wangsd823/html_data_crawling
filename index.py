#! python3
# -*- encoding: utf-8 -*-
import json, os
from common.ClassSpider import ClassificationSpider, SecondFlSpider

def save_file(folder, file_name, file_data):
    file_data_json = json.dumps(file_data, ensure_ascii=False)
    file_path = folder + file_name
    if os.path.exists(file_path):
        os.remove(file_path)
    with open(file_path, 'w') as f:
        f.write(file_data_json)
        f.close()

def make_dir(folder_path):
    folder = os.path.exists(folder_path)
    if not folder:
        os.makedirs(folder_path)

def init():
    classSpider = ClassificationSpider()
    classSpider.start()
    print('class result json: ', classSpider.getResult)
    # 总分类数据存储文件
    data_folder = './data'
    make_dir(data_folder)
    save_file(data_folder, '/fl_data.json', classSpider.getResult)

    secondFlSpider = SecondFlSpider(classSpider.getResult)
    secondFlSpider.start()
    # print('二级分类数据爬取结果： ', secondFlSpider.get_result)
    # 二级分类数据爬取结果 保存， 根据一级 区分文件夹
    for i in range(len(secondFlSpider.get_result)):
        first_fl_data = secondFlSpider.get_result[i]
        # 创建一级分类文件夹
        make_dir('./data/' + first_fl_data['name'])
        for j in range(len(first_fl_data['result_list'])):
            second_fl_data = first_fl_data['result_list'][j]
            # 创建二级分类文件, 保存数据
            save_file('./data/' + first_fl_data['name'], '/' + second_fl_data['name'] + '.json', second_fl_data['result_list'])





if __name__ == '__main__':
    init();