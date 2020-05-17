import pymongo
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFormLayout, QLineEdit, QLabel, QMessageBox
from PyQt5.QtGui import QIcon, QPalette, QBrush, QPixmap, QRegExpValidator  # 图标与字体
from PyQt5.QtWidgets import QDesktopWidget, QPushButton, QHBoxLayout, \
    QVBoxLayout, QDialog

client = pymongo.MongoClient(host='106.54.129.73', port=27017, username='client', password='client',
                             authSource='client', authMechanism='SCRAM-SHA-1')
db = client['client']   # 数据库
collection = db['client']   # 集合


class register(QDialog):
    def __init__(self):
        super(register, self).__init__()  # 显示调用父类的变量

        formLayout = QFormLayout()
        self.nameEdit = QLineEdit()
        self.nameEdit.setPlaceholderText('仅接受字母和数字')   # 输入提示
        self.passwordEdit = QLineEdit()
        self.passwordEdit.setPlaceholderText('6-16位数')  # 输入提示
        button = QPushButton('提交')

        formLayout.addRow('name', self.nameEdit)
        self.nameEdit.setEchoMode(QLineEdit.Normal)

        formLayout.addRow('password', self.passwordEdit)
        self.passwordEdit.setEchoMode(QLineEdit.Password)

        formLayout.addRow('', button)
        button.clicked.connect(self.buttonClick)

        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)
        self.nameEdit.setValidator(validator)
        self.passwordEdit.setValidator(validator)

        self.setLayout(formLayout)
        self.setWindowTitle('注册账户')
        self.setWindowModality(Qt.ApplicationModal)

    def buttonClick(self):
        name = self.nameEdit.text()
        password = self.passwordEdit.text()
        result = collection.find_one({'name': name})
        if result == None and (len(password)>=6 and len(password)<=16):
            collection.insert_one({'name': name, 'password': password})
            QMessageBox.information(self, '成功', '用户创建成功', QMessageBox.Yes)
            self.close()
        else:
            QMessageBox.critical(self, '错误', '用户名已存在或者密码位数错误', QMessageBox.Yes)


class login(QDialog):
    def __init__(self):
        super(login, self).__init__()  # 显示调用父类的变量

        formLayout = QFormLayout()
        self.nameEdit = QLineEdit()
        self.nameEdit.setPlaceholderText('仅接受字母和数字')  # 输入提示
        self.passwordEdit = QLineEdit()
        self.passwordEdit.setPlaceholderText('6-16位数')  # 输入提示
        self.button = QPushButton('提交')

        formLayout.addRow('name', self.nameEdit)
        self.nameEdit.setEchoMode(QLineEdit.Normal)

        formLayout.addRow('password', self.passwordEdit)
        self.passwordEdit.setEchoMode(QLineEdit.Password)

        formLayout.addRow('', self.button)

        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)
        self.nameEdit.setValidator(validator)
        self.passwordEdit.setValidator(validator)

        self.setLayout(formLayout)
        self.setWindowTitle('登入账户')
        self.setWindowModality(Qt.ApplicationModal)
