import time

from PySide6.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox

from Ui_main import Ui_Form

import requests
import os


class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super(MyWindow, self).__init__()

        # 加载页面
        self.setupUi(self)

        # 设置keywordLineEdit提示
        self.keywordLineEdit.setText('苹果，香蕉')
        # self.keywordLineEdit.setPlaceholderText('苹果，荔枝，(多个关键字以中文逗号隔开)')
        # 设置numSpinBox的范围
        self.numSpinBox.setRange(1, 1000)
        # 设置numSpinBox默认值
        self.numSpinBox.setValue(100)

        # 绑定信号与槽
        self.savePathBtn.clicked.connect(self.choose_savePath)
        self.startBtn.clicked.connect(self.start_download)
        self.stopBtn.clicked.connect(self.stop_download)

        # 初始化
        self.save_path = 'dataset'

    def choose_savePath(self):
        print('选择路径')
        self.save_path = QFileDialog.getExistingDirectory(self, '选择保存路径', '.')

    def start_download(self):
        print('开始采集')
        # 获取到keywordLineEdit的文本内容
        keyword = self.keywordLineEdit.text()
        # 获取到numSpinBox的值
        num = self.numSpinBox.value()
        # 获取图片保存路径
        save_path = self.save_path
        # print(keyword, num, save_path)

        if len(keyword) == 0 or save_path == '':
            # 弹出警告
            QMessageBox.warning(self, '警告', '请输入关键字或选择路径')
        else:
            # 向ouputLineEdit追加文本内容
            self.outputLineEdit.append('采集信息如下:\n关键字:{}\n数量{}\n保存路径:{}'.format(keyword.split(','), num, save_path))
            # keyword转列表
            keyword_list = keyword.split('，')
            for keyword in keyword_list:
                self.hide()
                MyWindow.download_images(keyword, num, save_path)
            self.show()
            self.outputLineEdit.append(f'爬取成功,图片保存至{save_path}')


    def stop_download(self):
        print('停止采集')
        # 让整个程序终止运行即可
        QApplication.quit()

    @staticmethod
    def download_images(keyword: str, num: int, save_path: str):
        """
        爬取百度图片搜索结果中指定关键词keyword的前 num 张图片，并下载到指定文件夹。
        :param keyword: 搜索关键词
        :param num: 需要下载的图片数量
        :param save_path:保存路径
        """
        # 创建保存图片的文件夹
        dir_name = f'{save_path}/outputs/{keyword}'
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        count = 0
        page_num = 0

        # 持续爬取图片，直到达到指定数量
        while True:
            print(f'正在爬取第{page_num + 1}页...')
            # self.ouputLineEdit.appendPlainText(f'正在爬取第{page_num + 1}页...')

            # 待请求URL
            url = f'https://image.baidu.com/search/acjson?tn=resultjs' \
                  f'on_com&logid=11513145951136847483&ipn=rj&ct=20132659' \
                  f'2&is=&fp=result&fr=&word={keyword}&queryWord={keyword}&' \
                  f'cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&late' \
                  f'st=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&' \
                  f'nc=1&expermode=&nojc=&isAsync=&pn={page_num * 30}&rn=30&gsm=5a&1683422786613='

            # 模拟请求头
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50'
            }

            # 发送 HTTP 请求，获取响应结果并解析 JSON 数据
            response = requests.get(url, headers=headers).json()

            # 遍历所有图片信息
            for image_info in response['data']:
                try:
                    # 打印当前正在下载的图片的 URL
                    # time.sleep(2)
                    print(f'正在下载第 {count} 张图片')
                    print(image_info['thumbURL'])

                    # 下载图片并保存到本地文件夹
                    image_data = requests.get(image_info['thumbURL'], headers=headers)
                    with open(os.path.join(dir_name, f'{keyword}_{count}.jpg'), 'wb') as f:
                        f.write(image_data.content)

                    count += 1

                    # 如果已经下载了足够数量的图片，则退出爬虫程序
                    if count >= num:
                        print(f'一共下载了 {num} 张图片！！！！！！')
                        print(f'图片已保存至:{dir_name}')
                        return

                except:
                    pass
            # 增加页数，以爬取下一页的图片
            page_num += 1


if __name__ == '__main__':
    app = QApplication()
    window = MyWindow()
    window.show()
    app.exec()
