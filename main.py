from PySide6.QtWidgets import QWidget, QApplication

from  Ui_main import Ui_Form


class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super(MyWindow, self).__init__()

        # 加载页面
        self.setupUi(self)

        # 设置keywordLineEdit提示，而不是默认字
        self.keywordLineEdit.setPlaceholderText('苹果,荔枝, , ,(多个关键字以英文逗号隔开)')
        # self.keywordLineEdit.setText(')


        # 绑定信号与槽
        self.savePathBtn.clicked.connect(self.choose_savePath)
        self.startBtn.clicked.connect(self.start_download)
        self.stopBtn.clicked.connect(self.stop_download)

    def choose_savePath(self):
        print('选择路径')

    def start_download(self):
        print('开始采集')

    def stop_download(self):
        print('停止采集')

if __name__ == '__main__':
    app = QApplication()
    window = MyWindow()
    window.show()
    app.exec()
