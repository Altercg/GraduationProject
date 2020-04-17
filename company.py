from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox, \
    QDialog, QWidget, QTreeWidget, QTreeWidgetItem


class run_company(QMainWindow):
    def __init__(self):
        super().__init__()  # 显示调用父类的变量
        self.setWindowTitle('农产品物价_企业版版')
        self.setWindowIcon(QIcon('timg.jpg'))
        self.resize(900, 600)  # 窗口大小。宽/高

        self.tree = QTreeWidget()
        self.tree.setColumnCount(1)
        self.tree.setHeaderLabels(['keys'])
        root1 = QTreeWidgetItem(self.tree)
        root1.setText(0, '农产品物价信息')

        root2 = QTreeWidgetItem(self.tree)
        root2.setText(0, '农产品产量信息')

        self.text = QLabel('现在已经打开企业版的界面了')

    def closeEvent(self, event):  # 默认函数名，关闭应用弹出提示
        reply = QMessageBox.question(self, '退出提示', "你确定要退出吗？",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  # 默认为no
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
