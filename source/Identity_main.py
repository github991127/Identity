from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon

from Identity import *
from list_themes import *


class Stats:
    def __init__(self):
        # 从ui文件中加载UI定义,从UI定义中动态创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了.比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('Identity.ui')
        self.ui.pushButton_0.clicked.connect(self.handleCalc0)
        self.ui.pushButton_1.clicked.connect(self.handleCalc1)
        self.ui.pushButton_2.clicked.connect(self.handleCalc2)
        self.ui.pushButton_3.clicked.connect(self.handleCalc3)
        self.ui.pushButton_4.clicked.connect(self.handleCalc4)
        self.ui.pushButton_5.clicked.connect(self.handleCalc5)
        self.ui.pushButton_6.clicked.connect(self.handleCalc6)
        self.ui.pushButton_7.clicked.connect(self.handleCalc7)
        self.ui.pushButton_8.clicked.connect(self.handleCalc8)
        self.ui.pushButton_9.clicked.connect(self.handleCalc9)
        self.ui.pushButton_X.clicked.connect(self.handleCalcX)
        self.ui.pushButton_D.clicked.connect(self.handleCalcD)
        self.ui.pushButton_E.clicked.connect(self.handleCalcE)
        self.ui.textEdit.returnPressed.connect(self.handleCalcE)  # 单行文本框回车消息

    def handleCalc0(self):  # 数字按钮对应文本框追加输入
        self.ui.textEdit.insert("0")

    def handleCalc1(self):  # 数字按钮对应文本框追加输入
        self.ui.textEdit.insert("1")

    def handleCalc2(self):
        self.ui.textEdit.insert("2")

    def handleCalc3(self):
        self.ui.textEdit.insert("3")

    def handleCalc4(self):
        self.ui.textEdit.insert("4")

    def handleCalc5(self):
        self.ui.textEdit.insert("5")

    def handleCalc6(self):
        self.ui.textEdit.insert("6")

    def handleCalc7(self):
        self.ui.textEdit.insert("7")

    def handleCalc8(self):
        self.ui.textEdit.insert("8")

    def handleCalc9(self):
        self.ui.textEdit.insert("9")

    def handleCalcX(self):  # 数字按钮对应文本框追加输入
        self.ui.textEdit.insert("X")

    def handleCalcE(self):  # ENTER按钮，将输入内容转换为int列表，传给cal计算
        self.ui.textBrowser.clear()
        str = self.ui.textEdit.text()
        lose = self.ui.textEdit_2.text()
        for i in range(1, 10):
            str = str.replace('  ', ' ')  # 清空多余空格
        str = str.strip(' ')  # 清空首尾空格
        if lose == '':
            lose = 18
        else:
            lose = int(lose)

        identity = identityCheck(str, lose)
        if identity == "FA":
            self.ui.textBrowser.append("输入位数不为17或18")
        elif identity == "FB":
            self.ui.textBrowser.append("缺少位数不在1-18内")
        else:
            self.ui.textBrowser.append('身份证{0}'.format(identity))
            if type(identity) != bool:
                self.ui.textBrowser.append('缺少的第{0}位为{1}'.format(lose, identity[lose - 1]))

    def handleCalcD(self):  # DELETE按钮，将所有文本框清空
        self.ui.textBrowser.clear()
        self.ui.textEdit.setText("")


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('image.png'))
    apply_stylesheet(app, theme[10], extra=extra, invert_secondary=True)  # 默认dark-False
    w = QWidget()
    w.setWindowIcon(QIcon('image.png'))
    stats = Stats()
    stats.ui.show()
    app.exec_()
