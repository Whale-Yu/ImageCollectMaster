# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(405, 538)
        self.keywordLabel = QLabel(Form)
        self.keywordLabel.setObjectName(u"keywordLabel")
        self.keywordLabel.setGeometry(QRect(30, 30, 111, 41))
        self.startBtn = QPushButton(Form)
        self.startBtn.setObjectName(u"startBtn")
        self.startBtn.setGeometry(QRect(30, 210, 151, 41))
        self.numSpinBox = QSpinBox(Form)
        self.numSpinBox.setObjectName(u"numSpinBox")
        self.numSpinBox.setGeometry(QRect(140, 90, 241, 21))
        self.keywordLineEdit = QLineEdit(Form)
        self.keywordLineEdit.setObjectName(u"keywordLineEdit")
        self.keywordLineEdit.setGeometry(QRect(140, 30, 241, 31))
        self.keywordLineEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.keywordLineEdit.setClearButtonEnabled(False)
        self.numLabel = QLabel(Form)
        self.numLabel.setObjectName(u"numLabel")
        self.numLabel.setGeometry(QRect(30, 80, 101, 41))
        self.savePathLabel = QLabel(Form)
        self.savePathLabel.setObjectName(u"savePathLabel")
        self.savePathLabel.setGeometry(QRect(30, 130, 101, 41))
        self.savePathBtn = QPushButton(Form)
        self.savePathBtn.setObjectName(u"savePathBtn")
        self.savePathBtn.setGeometry(QRect(140, 140, 241, 24))
        self.stopBtn = QPushButton(Form)
        self.stopBtn.setObjectName(u"stopBtn")
        self.stopBtn.setGeometry(QRect(230, 210, 151, 41))
        self.ouputLineEdit = QPlainTextEdit(Form)
        self.ouputLineEdit.setObjectName(u"ouputLineEdit")
        self.ouputLineEdit.setGeometry(QRect(30, 280, 351, 241))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u767e\u5ea6\u56fe\u5e93\u91c7\u96c6\u5668", None))
        self.keywordLabel.setText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u56fe\u7247\u5173\u952e\u5b57\uff1a", None))
        self.startBtn.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u91c7\u96c6", None))
        self.numLabel.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u722c\u53d6\u6570\u91cf\uff1a", None))
        self.savePathLabel.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u4fdd\u5b58\u8def\u5f84\uff1a", None))
        self.savePathBtn.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u56fe\u7247\u4fdd\u5b58\u8def\u5f84", None))
        self.stopBtn.setText(QCoreApplication.translate("Form", u"\u505c\u6b62\u91c7\u96c6", None))
    # retranslateUi

