import os
import threading
import time
import datetime
import requests
from faker import Faker

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
                        'User-Agent': Faker().user_agent()
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
        self.setWindowIcon(QIcon('bug.ico'))

        # 设置keywordLineEdit提示
        # self.keywordLineEdit.setText('苹果，香蕉')
        self.keywordLineEdit.setPlaceholderText('苹果，荔枝，(多个关键字以中文逗号隔开)')
        # 设置numSpinBox的范围
        self.numSpinBox.setRange(1, 1000)
        # 设置numSpinBox默认值
        self.numSpinBox.setValue(100)
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
            self.outputLineEdit.append('【{}】-采集信息如下:\n关键字:{}\n数量:{}\n保存路径:{}'.format(self.now_time(), keyword.split(','), num, save_path))
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
                self.outputLineEdit.append(f'【{self.now_time()}】-下载成功，图片保存至{save_path}')
            else:
                save_path = self.download_thread.save_path
                self.outputLineEdit.append(f'【{self.now_time()}】-下载已完成，图片保存至{save_path}')

            self.download_thread = None

    def now_time(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    app = QApplication()
    window = MyWindow()
    window.show()
    app.exec()
