import sys
from free import run_free
from company import run_company
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QIcon, QPalette, QBrush, QPixmap   # 图标与字体
from PyQt5.QtWidgets import QDesktopWidget, QMessageBox, QPushButton, QHBoxLayout, \
    QVBoxLayout, QDialog


class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()  # 显示调用父类的变量
        self.initui()

    def initui(self):
        self.setWindowTitle('农产品物价系统')
        self.setWindowIcon(QIcon('timg.jpg'))
        self.resize(900, 600)     # 窗口大小。宽/高
        self.center()   # 移动到屏幕的中心

        # 点击按钮
        btnf = QPushButton('免费版', self)
        btnq = QPushButton('企业版', self)
        # 点击事件
        btnf.clicked.connect(self.buttonclicked)
        btnq.clicked.connect(self.buttonclicked)

        # 主界面显示比例
        hbox = QHBoxLayout()

        hbox.addStretch(1)  # 空白处按照比例分配1：1：1
        hbox.addWidget(btnf)
        hbox.addWidget(btnq)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.setLayout(vbox)

    windowList = []

    def buttonclicked(self):
        text = self.sender()
        print(text.text())
        if text.text() == '免费版':
            free_main = run_free(self)
            self.windowList.append(free_main)
            self.close()
            free_main.show()

        if text.text() == '企业版':
            company_main = run_company(self)
            self.windowList.append(company_main)
            self.close()
            company_main.show()

    def resizeEvent(self, event):
        palette = QPalette()
        pix = QPixmap("bg.jpg")
        pix = pix.scaled(self.width(), self.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        self.setPalette(palette)

    def center(self):   # 让界面显示在屏幕中心
        qr = self.frameGeometry()   # 获得窗口
        cp = QDesktopWidget().availableGeometry().center()  # 获取屏幕中心点
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())
