# Author:yujunyu
# -*- codeing = utf-8 -*-
# @Time :2022/7/6 19:32
# @Author :yujunyu
# @Site :
# @File :baidu.py
# @software: PyCharm

"""
在baidu_img.py的基础上，增加多个关键字图片的获取
"""


import requests
import re
import os
import time
import getpass
from faker import Faker
import csv


def mkdirs():
    # 获取计算机的用户名
    user_name = getpass.getuser()
    # 保存至桌面
    outputs = f'C:/Users/{user_name}/Desktop/outputs'
    data_dir_name = outputs + r'/' + 'data'
    log_dir_name = outputs + r'/' + 'log'
    error_dir_name = outputs + r'/' + 'error'
    try:  # 如果没有文件夹就创建
        os.mkdir(outputs)
        os.mkdir(data_dir_name)
        os.mkdir(log_dir_name)
        os.mkdir(error_dir_name)
    except:
        pass

    return data_dir_name, log_dir_name, error_dir_name


def download_pic(keyword, nums):
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        "User-Agent": Faker().user_agent(),
        'Host': 'image.baidu.com',
        'Referer': 'https://image.baidu'
                   '.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=&st=-1&fm=result&fr=&sf=1&fmq=1610952036123_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E6%98%9F%E9%99%85',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'X-Requested-With': 'XMLHttpRequest'
    }

    url = 'http://image.baidu.com/search/index?tn=baiduimage&fm=result&ie=utf-8&word='  # 百度链接

    keyword = keyword
    countmax = nums
    url = url + keyword + "&pn="

    # 获取初始时间
    time_start = time.time()

    # get方式获取数据
    strhtml = requests.get(url, headers=headers, timeout=20)
    string = str(strhtml.text)

    # 正则表达式取得图片总数量
    totalnum = re.findall('<div id="resultInfo" style="font-size: 13px;">(.*?)</div>', string)
    print("百度图片" + totalnum[0])

    img_url_regex = '"thumbURL":"(.*?)",'  # 正则匹配式
    count = 0  # 总共下载的图片数
    index = 0  # 链接后面的序号
    page = 0  # 当前搜集的页

    path_file_name = f'{log_dir_name}' + r'/' + f'{keyword}_log.csv'
    csvfile = open(path_file_name, "a", encoding='utf_8_sig', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(['pic_path', 'pic_url'])

    while (1):
        strhtml = requests.get(url + str(index), headers=headers)  # get方式获取数据
        string = str(strhtml.text)
        print("已爬取网页")
        pic_url = re.findall(img_url_regex, string)  # 先利用正则表达式找到图片url
        print("第" + str(page + 1) + "页共收集到" + str(len(pic_url)) + "张图片")
        index += len(pic_url)  # 网址索引向后，跳到下一页继续搜刮图片
        try:  # 如果没有文件夹就创建
            os.mkdir(f'{data_dir_name}' + r'/' + keyword)
        except:
            pass

        li = []
        for each in pic_url:
            print('正在下载第' + str(count + 1) + '张图片，图片地址:' + str(each))
            try:
                if each is not None:
                    if each not in li:
                        pic = requests.get(each, timeout=5)
                        li.append(each)
                    else:
                        continue
                else:
                    continue
            except BaseException:
                print('错误，当前图片无法下载')
                continue

            else:
                # 保存图片
                string = f'{data_dir_name}' + r'/' + keyword + r'/' + keyword + '_' + str(count + 1) + '.jpg'
                fp = open(string, 'wb')
                fp.write(pic.content)
                fp.close()
                count += 1
                # 保存图片路径、url
                writer.writerow([string, each])

            if countmax == count:
                break
        li.clear()

        if countmax == count:
            break
    time_end = time.time()  # 获取结束时间
    print('处理完毕，共耗时:' + str(time_end - time_start) + "秒")


if __name__ == '__main__':
    print('------0:指定单个关键字\t模式1：指定多个关键字------')
    model = eval(input('请选择模式(0或1): '))

    # 单个关键字模式
    if model == 0:
        keyword = input('请输入图片关键字:')
        nums = eval(input('请输入图片数量：'))
        data_dir_name, log_dir_name, error_dir_name = mkdirs()
        download_pic(keyword, nums)

    # 多个关键字模式
    elif model == 1:
        # 获取关键字并遍历
        path = input('请输入关键字文件的绝对路径(为txt文件，一个关键字为一行)：')
        nums = eval(input('请输入图片数量：'))
        data_dir_name, log_dir_name, error_dir_name = mkdirs()
        f = open(rf'{path}', 'r', encoding='utf-8')
        kw_list = f.readlines()
        for kw in kw_list:
            keyword = kw.strip('\n')
            try:
                print('-' * 50 + f'正在爬取：{keyword}' + '-' * 50)
                # 下载图片函数
                download_pic(keyword, nums)
                print('-' * 50 + f'爬取完成' + '-' * 50)
                print()
            except:
                print(f'error：关键字【{keyword}】爬取失败 ！')
                # 记录报错、报错的keyword
                error_log = open(f'{error_dir_name}' + r'/' + 'error_log.txt', 'a', encoding='utf-8')
                error_log.write(f'error：关键字【{keyword}】爬取失败 ！\n')
                error_keyword = open(f'{error_dir_name}' + r'/' + 'error_keyword.txt', 'a', encoding='utf-8')
                error_keyword.write(f'{keyword}\n')

    else:
        print('无效输入')
