from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox, \
    QDialog, QWidget, QTreeWidget, QTreeWidgetItem, QTextEdit, QGroupBox, QGridLayout
from matplot import MyFigure
import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)  # 连接
db = client['rept']
name = ['猪肉', '牛肉', '羊肉', '白条鸡', '鸡蛋']


class run_free(QMainWindow):
    def __init__(self, parent=None):
        super(run_free, self).__init__(parent)  # 显示调用父类的变量
        self.setWindowTitle('农产品物价_免费版')
        self.setWindowIcon(QIcon('timg.jpg'))
        self.resize(1800, 1000)  # 窗口大小,宽/高

        widget = QWidget()  # 为了布局添加widget窗口
        layout = QHBoxLayout()  # 最外层水平布局

        # 左侧的树控件
        self.tree = QTreeWidget()
        self.tree.setColumnCount(1)
        self.tree.setHeaderLabels(['keys'])

        # 设置农产品物价信息根节点
        root1 = QTreeWidgetItem(self.tree)
        root1.setText(0, '农产品物价信息')

        # 添加子节点
        child1 = QTreeWidgetItem(root1)
        child1.setText(0, '畜禽品')
        child1_1 = QTreeWidgetItem(child1)
        child1_1.setText(0,  "家畜")
        QTreeWidgetItem(child1_1).setText(0, "猪肉")
        QTreeWidgetItem(child1_1).setText(0, "牛肉")
        QTreeWidgetItem(child1_1).setText(0, "羊肉")
        child1_2 = QTreeWidgetItem(child1)
        child1_2.setText(0,  "禽蛋")
        QTreeWidgetItem(child1_2).setText(0, "白条鸡")
        QTreeWidgetItem(child1_2).setText(0,  "鸡蛋")

        child2 = QTreeWidgetItem(root1)
        child2.setText(0, '水产品')
        child2_1 = QTreeWidgetItem(child2)
        child2_1.setText(0,  "淡水鱼")
        QTreeWidgetItem(child2_1).setText(0, "大带鱼")
        QTreeWidgetItem(child2_1).setText(0, "大黄花鱼")
        child2_2 = QTreeWidgetItem(child2)
        child2_2.setText(0,  "海水鱼")
        QTreeWidgetItem(child2_2).setText(0, "活鲤鱼")
        QTreeWidgetItem(child2_2).setText(0, "活草鱼")
        QTreeWidgetItem(child2_2).setText(0, "白鲢活鱼")
        QTreeWidgetItem(child2_2).setText(0, "活鲫鱼")
        QTreeWidgetItem(child2_2).setText(0, "花鲢活鱼")

        child3 = QTreeWidgetItem(root1)
        child3.setText(0, '蔬菜')
        child3_1 = QTreeWidgetItem(child3)
        child3_1.setText(0, "叶菜类")
        QTreeWidgetItem(child3_1).setText(0, "菠菜")
        QTreeWidgetItem(child3_1).setText(0, "芹菜")
        QTreeWidgetItem(child3_1).setText(0, "油菜")
        child3_2 = QTreeWidgetItem(child3)
        child3_2.setText(0, "白菜类")
        QTreeWidgetItem(child3_2).setText(0, "大白菜")
        child3_3 = QTreeWidgetItem(child3)
        child3_3.setText(0, "瓜菜类")
        QTreeWidgetItem(child3_3).setText(0, "冬瓜")
        QTreeWidgetItem(child3_3).setText(0, "黄瓜")
        QTreeWidgetItem(child3_3).setText(0, "南瓜")
        QTreeWidgetItem(child3_3).setText(0, "西葫芦")
        child3_4 = QTreeWidgetItem(child3)
        child3_4.setText(0,  "根茎类")
        QTreeWidgetItem(child3_4).setText(0, "白萝卜")
        QTreeWidgetItem(child3_4).setText(0, "胡萝卜")
        QTreeWidgetItem(child3_4).setText(0, "生姜")
        QTreeWidgetItem(child3_4).setText(0, "土豆")
        child3_5 = QTreeWidgetItem(child3)
        child3_5.setText(0, "茄果类")
        QTreeWidgetItem(child3_5).setText(0, "茄子")
        QTreeWidgetItem(child3_5).setText(0, "青椒")
        QTreeWidgetItem(child3_5).setText(0, "西红柿")
        child3_6 = QTreeWidgetItem(child3)
        child3_6.setText(0,  "甘蓝类")
        QTreeWidgetItem(child3_6).setText(0, "菜花")
        QTreeWidgetItem(child3_6).setText(0, "洋白菜")
        child3_7 = QTreeWidgetItem(child3)
        child3_7.setText(0, "豆类")
        QTreeWidgetItem(child3_7).setText(0, "豆角")
        child3_8 = QTreeWidgetItem(child3)
        child3_8.setText(0, "葱蒜类")
        QTreeWidgetItem(child3_8).setText(0, "葱头")
        QTreeWidgetItem(child3_8).setText(0, "大蒜")
        QTreeWidgetItem(child3_8).setText(0, "蒜苔")
        QTreeWidgetItem(child3_8).setText(0, "大葱")
        QTreeWidgetItem(child3_8).setText(0, "韭菜")
        child3_9 = QTreeWidgetItem(child3)
        child3_9.setText(0, "莴(菊)苣类")
        QTreeWidgetItem(child3_9).setText(0, "莴笋")
        QTreeWidgetItem(child3_9).setText(0, "生菜")
        child3_10 = QTreeWidgetItem(child3)
        child3_10.setText(0,  "菌类")
        QTreeWidgetItem(child3_10).setText(0, "香菇")
        QTreeWidgetItem(child3_10).setText(0, "平菇")
        child3_11 = QTreeWidgetItem(child3)
        child3_11.setText(0, "水生蔬菜")
        QTreeWidgetItem(child3_11).setText(0, "莲藕")

        child4 = QTreeWidgetItem(root1)
        child4.setText(0, '水果')
        child4_1 = QTreeWidgetItem(child4)
        child4_1.setText(0, "仁果类")
        QTreeWidgetItem(child4_1).setText(0, "富士苹果")
        QTreeWidgetItem(child4_1).setText(0, "橙子")
        QTreeWidgetItem(child4_1).setText(0, "鸭梨")
        child4_2 = QTreeWidgetItem(child4)
        child4_2.setText(0, "浆果类")
        QTreeWidgetItem(child4_2).setText(0, "巨峰葡萄")
        child4_3 = QTreeWidgetItem(child4)
        child4_3.setText(0, "热带")
        QTreeWidgetItem(child4_3).setText(0, "菠萝")
        QTreeWidgetItem(child4_3).setText(0, "香蕉")
        child4_4 = QTreeWidgetItem(child4)
        child4_4.setText(0, "瓜类")
        QTreeWidgetItem(child4_4).setText(0, "西瓜")
        # 添加到布局中
        layout.addWidget(self.tree, 1)
        self.tree.doubleClicked.connect(self.onTreeClicked)     # 双击信号
        self.tree.setColumnWidth(0, 300)  # 设置树控件的宽度

        # 右侧的控件显示图画
        self.groupBox = QGroupBox()
        layout.addWidget(self.groupBox, 3)

        # 最后布局
        self.setCentralWidget(widget)
        widget.setLayout(layout)    # widget中设置布局

    def onTreeClicked(self, index):
        item = self.tree.currentItem()  # 当前的项
        if item.text(0) in name:
            col = item.parent().parent().text(0)
            print(col)
            if col == '畜禽品':
                collection = db['meat']     # 指定集合
                result = collection.find_one({'pro_name': item.text(0)})
                print(result)   # 返回了一个字典
        self.F = MyFigure(width=3, height=2, dpi=100,)
        self.F.plotax(result['time_price'])
        self.hbox = QGridLayout(self.groupBox)
        self.hbox.addWidget(self.F, 0, 1)

    def closeEvent(self, event):  # 默认函数名，关闭应用弹出提示
        reply = QMessageBox.question(self, '退出提示', "你确定要退出吗？",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  # 默认为no
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
