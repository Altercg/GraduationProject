from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QIcon, QPalette, QBrush, QPixmap   # 图标与字体
from PyQt5.QtWidgets import QDesktopWidget, QPushButton, QHBoxLayout, \
    QVBoxLayout, QDialog


class register(QDialog):
    def __init__(self):
        super(register, self).__init__()  # 显示调用父类的变量
