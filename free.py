from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox, \
    QDialog, QWidget, QTreeWidget, QTreeWidgetItem, QTextEdit, QGroupBox, QGridLayout, QCheckBox
from matplot import MyFigure
import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)  # 连接
db = client['rept']
name = ['猪肉', '牛肉', '羊肉', '白条鸡', '鸡蛋',
        '大带鱼', '大黄花鱼', '活鲤鱼', '活草鱼', '白鲢活鱼', '活鲫鱼', '花鲢活鱼',
        '菠菜', '芹菜', '油菜', '大白菜', '冬瓜', '黄瓜', '南瓜', '西葫芦', '白萝卜', '胡萝卜', '生姜', '土豆', '茄子',
        '青椒', '西红柿', '菜花', '洋白菜', '豆角', '葱头', '大蒜', '蒜苔', '大葱', '韭菜', '莴笋', '生菜', '香菇', '平菇', '莲藕',
        '富士苹果', '鸭梨', '巨峰葡萄', '菠萝', '香蕉', '西瓜', '橙子']


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

        layout.addWidget(self.tree, 1)  # 树控件添加到布局中
        self.tree.doubleClicked.connect(self.onTreeClicked)     # 双击信号，显示func
        self.tree.setColumnWidth(0, 300)  # 设置树控件的宽度

        # 右侧显示和选项放在groupBox里面
        self.groupBox = QGroupBox()
        groupbox_vbox = QVBoxLayout(self.groupBox)

        self.func = QGroupBox()         # 右侧上面显示功能
        func_box = QGridLayout(self.func)   # 右侧上面使用栅格布局
        # 样式：同一农产品的不同地点物价比较的复选框
        self.checkBox1 = QCheckBox('批发价')
        self.checkBox2 = QCheckBox('集市价')
        self.checkBox3 = QCheckBox('超市价')
        self.local_button = QPushButton('地点比较')
        self.checkBox1.setEnabled(False)
        self.checkBox2.setEnabled(False)
        self.checkBox3.setEnabled(False)

        func_box.addWidget(self.checkBox1, 0, 0, 1, 1)
        func_box.addWidget(self.checkBox2, 1, 0, 1, 1)
        func_box.addWidget(self.checkBox3, 2, 0, 1, 1)
        func_box.addWidget(self.local_button, 3, 0, 1, 1)
        self.local_button.clicked.connect(self.differlocal_cmp)       # 功能一：同一农产品的不同地点物价比较

        # 功能二：同类农产品的比较和线性相关

        self.picture = QGroupBox()
        self.F = MyFigure(width=3, height=2, dpi=100, )  # 每次点击触发新的画布生成
        self.picture_box = QGridLayout(self.picture)

        groupbox_vbox.addWidget(self.func, 1)
        groupbox_vbox.addWidget(self.picture, 6)
        layout.addWidget(self.groupBox, 4)

        # 最后布局
        self.setCentralWidget(widget)
        widget.setLayout(layout)    # widget中设置布局

    # 点击的形成func
    def onTreeClicked(self, index):
        # 设置默认的地点比较
        self.checkBox1.setEnabled(False)
        self.checkBox2.setEnabled(False)
        self.checkBox3.setEnabled(False)
        self.checkBox1.setChecked(False)
        self.checkBox2.setChecked(False)
        self.checkBox3.setChecked(False)
        self.tree_draw_picture()
        # 功能二：同类农产品的比较和线性相关

    def tree_draw_picture(self):
        # 当前的项
        item = self.tree.currentItem()
        # 指定集合
        if item.text(0) in name:
            col = item.parent().parent().text(0)
            if col == '畜禽品':
                collection = db['meat']
            elif col == '水产品':
                collection = db['aqua']
            elif col == '蔬菜':
                collection = db['vege']
            elif col == '水果':
                collection = db['frut']
            self.result = collection.find_one({'pro_name': item.text(0)})
            # 复选框的呈现状态
            select = ''
            if 'super_price' in self.result:
                self.checkBox3.setEnabled(True)
                select = 'super_price'
            else:
                self.checkBox3.setEnabled(False)
            if 'mell_price' in self.result:
                self.checkBox2.setEnabled(True)
                select = 'mell_price'
            else:
                self.checkBox2.setEnabled(False)
            if 'time_price' in self.result:
                self.checkBox1.setEnabled(True)
                select = 'time_price'
            else:
                self.checkBox1.setEnabled(False)
            # 复选框改变显示图片
            if select == 'time_price':
                self.checkBox1.setChecked(True)
            elif select == 'mell_price':
                self.checkBox2.setChecked(True)
            elif select == 'super_price':
                self.checkBox3.setChecked(True)

            self.F.tree_wholesale(self.result[select])
            self.picture_box.addWidget(self.F, 0, 1)

    # 地点比较
    def differlocal_cmp(self):
        check1 = str(self.checkBox1.isChecked())    # time_price
        check2 = str(self.checkBox2.isChecked())    # mall_price
        check3 = str(self.checkBox3.isChecked())    # super_price
        if check1 == 'True' or check2 == 'True' or check3 == 'True':
            self.F.differlocal(self.result, check1, check2, check3)
            self.picture_box.addWidget(self.F, 0, 1)

    def closeEvent(self, event):  # 默认函数名，关闭应用弹出提示
        reply = QMessageBox.question(self, '退出提示', "你确定要退出吗？",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  # 默认为no
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
