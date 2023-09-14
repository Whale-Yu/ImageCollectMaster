import os
import threading
import time
import datetime
import requests
import random

from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QCursor, QCloseEvent, QIcon
from PySide6.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox, QProgressDialog

from Ui_main import Ui_Form


class DownloadThread(QThread):
    """
    图片下载线程类
    """
    progress_signal = Signal(int, str)  # 下载进度信号，用于更新进度对话框和状态栏
    finished_signal = Signal()  # 下载结束信号，用于通知主线程下载已经结束

    def __init__(self, keywords, num, save_path):
        super(DownloadThread, self).__init__()
        self.keywords = keywords
        self.num = num
        self.save_path = save_path
        self._stop_flag = False  # 停止标志，用于控制下载进程的终止

    def run(self):
        """
        线程主函数，用于执行图片下载操作
        """
        print(self.keywords)
        for keyword in self.keywords:
            if keyword != '':
                print(keyword)
                # 创建保存图片的文件夹
                dir_name = os.path.join(self.save_path, 'outputs', keyword)
                if not os.path.exists(dir_name):
                    os.makedirs(dir_name)

                count = 0
                page_num = 0

                # 持续爬取图片，直到达到指定数量
                user_agent_pool = [
                    'Mozilla/5.0 (iPod; U; CPU iPhone OS 3_3 like Mac OS X; mg-MG) AppleWebKit/534.48.5 (KHTML, like Gecko) Version/3.0.5 Mobile/8B111 Safari/6534.48.5',
                    'Mozilla/5.0 (Android 2.3.4; Mobile; rv:11.0) Gecko/11.0 Firefox/11.0',
                    'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/531.19.1 (KHTML, like Gecko) Version/5.0.1 Safari/531.19.1',
                    'Mozilla/5.0 (compatible; MSIE 8.0; Windows 95; Trident/3.1)',
                    'Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.0; Trident/3.1)',
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
                    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 10.0; Trident/5.0)',
                    'Opera/9.94.(Windows CE; hr-HR) Presto/2.9.186 Version/12.00',
                    'Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/533.13.6 (KHTML, like Gecko) Version/5.0.4 Safari/533.13.6',
                    'Mozilla/5.0 (Android 2.2.1; Mobile; rv:63.0) Gecko/63.0 Firefox/63.0',
                    'Mozilla/5.0 (X11; Linux i686; rv:1.9.5.20) Gecko/6654-03-18 09:42:33 Firefox/8.0',
                    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/4.0)',
                    'Opera/8.53.(X11; Linux x86_64; ha-NG) Presto/2.9.166 Version/10.00',
                    'Opera/9.24.(X11; Linux x86_64; br-FR) Presto/2.9.165 Version/11.00',
                    'Mozilla/5.0 (iPad; CPU iPad OS 4_2_1 like Mac OS X) AppleWebKit/531.2 (KHTML, like Gecko) CriOS/26.0.874.0 Mobile/87C362 Safari/531.2',
                    'Mozilla/5.0 (Windows NT 6.2; lg-UG; rv:1.9.0.20) Gecko/2872-07-08 10:41:11 Firefox/3.8',
                    'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_8 like Mac OS X) AppleWebKit/532.0 (KHTML, like Gecko) FxiOS/16.8k9247.0 Mobile/86E239 Safari/532.0',
                    'Opera/9.19.(Windows NT 5.1; lb-LU) Presto/2.9.189 Version/12.00',
                    'Mozilla/5.0 (Linux; Android 2.0.1) AppleWebKit/536.0 (KHTML, like Gecko) Chrome/21.0.898.0 Safari/536.0',
                    'Opera/9.37.(Windows NT 6.0; iu-CA) Presto/2.9.170 Version/10.00',
                    'Opera/9.16.(X11; Linux i686; tl-PH) Presto/2.9.180 Version/11.00',
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/15.0.808.0 Safari/532.0',
                    'Mozilla/5.0 (compatible; MSIE 6.0; Windows 95; Trident/4.1)',
                    'Opera/8.94.(X11; Linux x86_64; pap-AW) Presto/2.9.170 Version/11.00',
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
                    'Opera/9.67.(Windows NT 5.2; an-ES) Presto/2.9.160 Version/12.00',
                    'Opera/8.88.(X11; Linux i686; dz-BT) Presto/2.9.160 Version/11.00',
                    'Opera/8.74.(Windows NT 6.0; quz-PE) Presto/2.9.174 Version/11.00',
                    'Mozilla/5.0 (X11; Linux i686; rv:1.9.7.20) Gecko/6637-09-23 01:08:14 Firefox/3.8']

                while count < self.num and not self._stop_flag:
                    # 待请求URL
                    url = f'https://image.baidu.com/search/acjson?tn=resultjs' \
                          f'on_com&logid=11513145951136847483&ipn=rj&ct=20132659' \
                          f'2&is=&fp=result&fr=&word={keyword}&queryWord={keyword}&' \
                          f'cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&late' \
                          f'st=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&' \
                          f'nc=1&expermode=&nojc=&isAsync=&pn={page_num * 30}&rn=30&gsm=5a&1683422786613='

                    # 模拟请求头
                    headers = {
                        'User-Agent': random.choice(user_agent_pool)
                    }

                    # 发送 HTTP 请求，获取响应结果并解析 JSON 数据
                    try:
                        response = requests.get(url, headers=headers)
                        response.raise_for_status()
                        response_data = response.json()
                        # 遍历所有图片信息
                        for image_info in response_data['data']:
                            if count >= self.num or self._stop_flag:
                                break

                            try:
                                # 下载图片并保存到本地文件夹
                                print(image_info['thumbURL'])
                                image_data = requests.get(image_info['thumbURL'], headers=headers)
                                with open(os.path.join(dir_name, f'{keyword}_{count}.jpg'), 'wb') as f:
                                    f.write(image_data.content)

                                count += 1

                                # 发送进度信号，更新进度对话框和状态栏显示
                                progress_text = f'正在下载【{keyword}】：第{count}张图片'
                                self.progress_signal.emit(count, progress_text)
                            except:
                                pass
                    except:
                        pass

                    # 增加页数，以爬取下一页的图片
                    page_num += 1

        # 发送结束信号，通知主线程下载已经结束
        self.finished_signal.emit()

    def stop(self):
        """
        停止图片下载操作
        """
        self._stop_flag = True


class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super(MyWindow, self).__init__()

        # 加载页面
        self.setupUi(self)
        # 窗口大小固定
        self.setFixedSize(self.width(), self.height())
        # 设置图标
        self.setWindowIcon(QIcon('assets/title.ico'))

        # 设置keywordLineEdit提示
        # self.keywordLineEdit.setText('苹果，香蕉')
        self.keywordLineEdit.setPlaceholderText('苹果，荔枝，(多个关键字以中文逗号隔开)')
        # 设置numSpinBox的范围
        self.numSpinBox.setRange(1, 9999)
        # 设置numSpinBox默认值
        self.numSpinBox.setValue(50)
        # 设置outputLineEdit只读
        self.outputLineEdit.setReadOnly(True)

        # 初始化
        self.save_path = None  # 保存路径
        self.download_thread = None  # 图片下载线程
        self.progress_dialog = None  # 进度对话框

        # 绑定信号与槽
        self.savePathBtn.clicked.connect(self.choose_savePath)
        self.startBtn.clicked.connect(self.start_download)

    def choose_savePath(self):
        print('选择路径')
        self.save_path = QFileDialog.getExistingDirectory(self, '选择保存路径', '.')
        # 弹窗表示选择路径成功
        QMessageBox.information(self, '提示', '已设置保存路径')
        self.outputLineEdit.append('【{}】- 保存路径：{}'.format(self.now_time(), self.save_path))

    def start_download(self):
        print('开始采集')
        # 获取到keywordLineEdit的文本内容
        keyword = self.keywordLineEdit.text()
        # 获取到numSpinBox的值
        num = self.numSpinBox.value()
        # 获取图片保存路径
        save_path = self.save_path
        # print(keyword, num, save_path)

        if len(keyword) == 0 or save_path == None:
            # 弹出警告
            QMessageBox.warning(self, '警告', '请输入关键字或选择路径')
        else:
            # 向ouputLineEdit追加文本内容
            self.outputLineEdit.append(
                '【{}】- 正在采集！当前采集信息：\n关键字：{}\n数量：{}\n保存路径：{}'.format(self.now_time(), keyword.split(','), num, save_path))
            # keyword转列表
            keyword_list = keyword.split('，')

            # 创建图片下载线程，并启动线程
            self.download_thread = DownloadThread(keyword_list, num, save_path)
            self.download_thread.progress_signal.connect(self.show_progress_dialog)
            self.download_thread.finished_signal.connect(self.download_finished)
            self.download_thread.start()

            # 显示进度对话框
            self.progress_dialog = QProgressDialog(f'开始下载图片...', '取消', 0, num, self)
            self.progress_dialog.setWindowTitle('下载进度')
            self.progress_dialog.setWindowModality(Qt.WindowModal)
            self.progress_dialog.setRange(0, self.download_thread.num)
            self.progress_dialog.setCancelButton(None)
            self.progress_dialog.canceled.connect(self.stop_download)
            self.progress_dialog.show()

    def stop_download(self):
        print('停止采集')
        if self.download_thread is not None:
            self.download_thread.stop()
            self.download_thread.wait()

    def show_progress_dialog(self, count, progress_text):
        """
        显示进度对话框，更新下载进度和状态信息
        """
        if self.progress_dialog is not None:
            self.progress_dialog.setValue(count)
            self.progress_dialog.setLabelText(progress_text)
            QApplication.processEvents()

    def download_finished(self):
        """
        图片下载完成后的处理函数
        """
        if self.progress_dialog is not None:
            self.progress_dialog.close()

        if self.download_thread is not None:
            # 判断下载是否被终止
            if self.download_thread.isFinished():
                save_path = self.download_thread.save_path
                self.outputLineEdit.append(f'【{self.now_time()}】-下载成功！图片保存至{save_path}')
                # 弹框提示下载完成
                QMessageBox.information(self, '提示', '下载完成')
            else:
                save_path = self.download_thread.save_path
                self.outputLineEdit.append(f'【{self.now_time()}】-下载已完成！图片保存至{save_path}')
                # 弹框提示下载完成
                QMessageBox.information(self, '提示', '下载完成')

            self.download_thread = None

    def now_time(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    app = QApplication()
    window = MyWindow()
    window.show()
    app.exec()
