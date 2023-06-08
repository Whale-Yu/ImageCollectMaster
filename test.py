# -*- codeing = utf-8 -*-
# @Time :2023/6/8 19:13
# @Author :yujunyu
# @Site :
# @File :test.py
# @software: PyCharm
from faker import Faker

userli = []
for i in range(10):
    user_agent = Faker().user_agent()
    if user_agent not in userli:
        userli.append(user_agent)
print(userli)

li = ['Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_8_7) AppleWebKit/533.0 (KHTML, like Gecko) Chrome/27.0.855.0 Safari/533.0',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows 95; Trident/3.1)', 'Opera/9.65.(X11; Linux i686; pap-AN) Presto/2.9.169 Version/11.00',
      'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_11_8) AppleWebKit/535.0 (KHTML, like Gecko) Chrome/58.0.823.0 Safari/535.0',
      'Mozilla/5.0 (X11; Linux x86_64; rv:1.9.7.20) Gecko/9749-11-02 03:57:33 Firefox/3.6.7',
      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/533.0 (KHTML, like Gecko) Chrome/15.0.824.0 Safari/533.0',
      'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 10.0; Trident/5.1)',
      'Mozilla/5.0 (Linux; Android 7.1.2) AppleWebKit/531.1 (KHTML, like Gecko) Chrome/45.0.885.0 Safari/531.1',
      'Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/532.1.6 (KHTML, like Gecko) Version/4.0 Safari/532.1.6',
      'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 10.0; Trident/4.1)']
