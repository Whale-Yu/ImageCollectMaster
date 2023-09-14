# -*- codeing = utf-8 -*-
# @Time :2023/6/8 19:13
# @Author :yujunyu
# @Site :
# @File :test.py
# @software: PyCharm
from faker import Faker

userli = []
for i in range(50):
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

ls2 = [
    'Mozilla/5.0 (iPod; U; CPU iPhone OS 3_3 like Mac OS X; mg-MG) AppleWebKit/534.48.5 (KHTML, like Gecko) Version/3.0.5 Mobile/8B111 Safari/6534.48.5',
    'Mozilla/5.0 (Android 2.3.4; Mobile; rv:11.0) Gecko/11.0 Firefox/11.0',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/531.19.1 (KHTML, like Gecko) Version/5.0.1 Safari/531.19.1',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows 95; Trident/3.1)', 'Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.0; Trident/3.1)',
    'Opera/9.57.(Windows NT 5.01; so-ET) Presto/2.9.172 Version/12.00',
    'Mozilla/5.0 (X11; Linux i686; rv:1.9.5.20) Gecko/5885-04-26 19:05:42 Firefox/3.6.3',
    'Mozilla/5.0 (compatible; MSIE 5.0; Windows 98; Trident/5.0)',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8_1 rv:6.0; ckb-IQ) AppleWebKit/535.33.6 (KHTML, like Gecko) Version/4.1 Safari/535.33.6',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_8 like Mac OS X) AppleWebKit/533.2 (KHTML, like Gecko) CriOS/15.0.898.0 Mobile/66N503 Safari/533.2',
    'Opera/8.56.(X11; Linux x86_64; ig-NG) Presto/2.9.185 Version/11.00',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/531.1 (KHTML, like Gecko) Chrome/55.0.895.0 Safari/531.1',
    'Mozilla/5.0 (Android 4.0.1; Mobile; rv:21.0) Gecko/21.0 Firefox/21.0',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/5.0)',
    'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/534.2 (KHTML, like Gecko) Chrome/32.0.800.0 Safari/534.2',
    'Opera/8.41.(X11; Linux i686; ky-KG) Presto/2.9.178 Version/11.00',
    'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/40.0.888.0 Safari/535.1',
    'Mozilla/5.0 (iPod; U; CPU iPhone OS 3_3 like Mac OS X; byn-ER) AppleWebKit/532.9.4 (KHTML, like Gecko) Version/3.0.5 Mobile/8B113 Safari/6532.9.4',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 10.0; Trident/5.0)', 'Opera/9.94.(Windows CE; hr-HR) Presto/2.9.186 Version/12.00',
    'Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/533.13.6 (KHTML, like Gecko) Version/5.0.4 Safari/533.13.6',
    'Mozilla/5.0 (Android 2.2.1; Mobile; rv:63.0) Gecko/63.0 Firefox/63.0',
    'Mozilla/5.0 (X11; Linux i686; rv:1.9.5.20) Gecko/6654-03-18 09:42:33 Firefox/8.0',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/4.0)', 'Opera/8.53.(X11; Linux x86_64; ha-NG) Presto/2.9.166 Version/10.00',
    'Opera/9.24.(X11; Linux x86_64; br-FR) Presto/2.9.165 Version/11.00',
    'Mozilla/5.0 (iPad; CPU iPad OS 4_2_1 like Mac OS X) AppleWebKit/531.2 (KHTML, like Gecko) CriOS/26.0.874.0 Mobile/87C362 Safari/531.2',
    'Mozilla/5.0 (Windows NT 6.2; lg-UG; rv:1.9.0.20) Gecko/2872-07-08 10:41:11 Firefox/3.8',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_8 like Mac OS X) AppleWebKit/532.0 (KHTML, like Gecko) FxiOS/16.8k9247.0 Mobile/86E239 Safari/532.0',
    'Opera/9.19.(Windows NT 5.1; lb-LU) Presto/2.9.189 Version/12.00',
    'Mozilla/5.0 (Linux; Android 2.0.1) AppleWebKit/536.0 (KHTML, like Gecko) Chrome/21.0.898.0 Safari/536.0',
    'Opera/9.37.(Windows NT 6.0; iu-CA) Presto/2.9.170 Version/10.00', 'Opera/9.16.(X11; Linux i686; tl-PH) Presto/2.9.180 Version/11.00',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/15.0.808.0 Safari/532.0',
    'Mozilla/5.0 (compatible; MSIE 6.0; Windows 95; Trident/4.1)', 'Opera/8.94.(X11; Linux x86_64; pap-AW) Presto/2.9.170 Version/11.00',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.01; Trident/5.0)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_7; rv:1.9.4.20) Gecko/4761-07-03 12:43:47 Firefox/6.0',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/5.1)',
    'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/27.0.881.0 Safari/535.2',
    'Mozilla/5.0 (compatible; MSIE 6.0; Windows 98; Win 9x 4.90; Trident/3.1)',
    'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_11_5) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/52.0.845.0 Safari/535.2',
    'Mozilla/5.0 (Linux; Android 3.2.6) AppleWebKit/533.0 (KHTML, like Gecko) Chrome/13.0.826.0 Safari/533.0',
    'Mozilla/5.0 (Macintosh; PPC Mac OS X 10_12_8 rv:2.0; dv-MV) AppleWebKit/532.39.1 (KHTML, like Gecko) Version/5.0.1 Safari/532.39.1',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/532.27.1 (KHTML, like Gecko) Version/5.0.5 Safari/532.27.1',
    'Mozilla/5.0 (Android 4.4.1; Mobile; rv:33.0) Gecko/33.0 Firefox/33.0',
    'Opera/9.67.(Windows NT 5.2; an-ES) Presto/2.9.160 Version/12.00', 'Opera/8.88.(X11; Linux i686; dz-BT) Presto/2.9.160 Version/11.00',
    'Opera/8.74.(Windows NT 6.0; quz-PE) Presto/2.9.174 Version/11.00',
    'Mozilla/5.0 (X11; Linux i686; rv:1.9.7.20) Gecko/6637-09-23 01:08:14 Firefox/3.8']
