import sys
import pymongo
from run import run
from register_login import register, login
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PyQt5.QtGui import QIcon, QPalette, QBrush, QPixmap   # 图标与字体
from PyQt5.QtWidgets import QDesktopWidget, QPushButton, QHBoxLayout, \
    QVBoxLayout, QDialog


class Start(QMainWindow):
    def __init__(self):
        super().__init__()  # Python2.7中super要有这两个实参，显示调用父类的变量
        self.initui()

    def initui(self):
        self.setWindowTitle('农产品物价分析')
        self.setWindowIcon(QIcon('timg.jpg'))
        self.resize(900, 600)     # 窗口大小。宽/高
        self.center()   # 移动到屏幕的中心

        # 点击按钮
        btnf = QPushButton('进入', self)
        btnq = QPushButton('注册', self)
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
        if text.text() == '注册':
            self.reg = register()
            self.reg.show()
        if text.text() == '进入':
            self.result = login()
            self.result.button.clicked.connect(self.login_buttonClick)
            self.result.show()

    def login_buttonClick(self):
        # client = pymongo.MongoClient(host='localhost', port=27017)  # 连接
        client = pymongo.MongoClient(host='106.54.129.73', port=27017, username='client', password='client',
                                     authSource='client', authMechanism='SCRAM-SHA-1')
        db = client['client']  # 数据库
        collection = db['client']
        name = self.result.nameEdit.text()
        password = self.result.passwordEdit.text()
        re = collection.find_one({'name': name})
        if re:
            if password == re['password']:
                self.result.close()
                run_main = run()
                self.windowList.append(run_main)  # 加入列表可以实现一个主窗口到另一个主窗口
                self.close()  # 登入窗口关闭
                run_main.show()  # 运行窗口显示
            else:
                QMessageBox.critical(self, '错误', '密码错误', QMessageBox.Yes)
        else:
            QMessageBox.critical(self, '错误', '用户不存在', QMessageBox.Yes)

    # 设置背景图片
    def resizeEvent(self, event):
        palette = QPalette()
        pix = QPixmap("bg.jpg")
        pix = pix.scaled(self.width(), self.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        self.setPalette(palette)

    # 让界面显示在屏幕中心
    def center(self):
        qr = self.frameGeometry()   # 获得窗口
        cp = QDesktopWidget().availableGeometry().center()  # 获取屏幕中心点
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    start = Start()
    start.show()
    sys.exit(app.exec_())
