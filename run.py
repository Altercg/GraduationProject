import os
import pymongo
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QMessageBox, QWidget, QTreeWidget, QTreeWidgetItem,\
    QGridLayout, QTabWidget
from exponential_smoothing import MyFigure      # from matplot import MyFigure
# from exponential_smoothing2 import MyFigure
from echart import initData, initDatas
from PyQt5.QtWebEngineWidgets import QWebEngineView

client = pymongo.MongoClient(host='localhost', port=27017)  # 连接
db = client['rept']
name = ['猪肉', '牛肉', '羊肉', '白条鸡', '鸡蛋',
        '大带鱼', '大黄花鱼', '活鲤鱼', '活草鱼', '白鲢活鱼', '活鲫鱼', '花鲢活鱼',
        '菠菜', '芹菜', '油菜', '大白菜', '冬瓜', '黄瓜', '南瓜', '西葫芦', '白萝卜', '胡萝卜', '生姜', '土豆', '茄子',
        '青椒', '西红柿', '菜花', '洋白菜', '豆角', '葱头', '大蒜', '蒜苔', '大葱', '韭菜', '莴笋', '生菜', '香菇', '平菇', '莲藕',
        '富士苹果', '鸭梨', '巨峰葡萄', '菠萝', '香蕉', '西瓜', '橙子']


class run(QMainWindow):
    def __init__(self, parent=None):
        super(run, self).__init__(parent)  # 显示调用父类的变量
        self.setWindowTitle('农产品物价分析')
        self.setWindowIcon(QIcon('timg.jpg'))
        self.resize(2100, 1200)  # 窗口大小,宽/高

        widget = QWidget()  # 为了布局添加widget窗口
        layout = QHBoxLayout()  # 最外层水平布局

        # 左侧的树控件
        self.tree = QTreeWidget()
        self.tree.setColumnCount(1)
        self.tree.setHeaderLabels(['农产品信息'])

        # 设置农产品物价信息根节点
        root1 = QTreeWidgetItem(self.tree)
        root1.setText(0, '农产品')
        root1.setExpanded(True)     # 设置该结点展开

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
        child2_1.setText(0,  "海水鱼")
        QTreeWidgetItem(child2_1).setText(0, "大带鱼")
        QTreeWidgetItem(child2_1).setText(0, "大黄花鱼")
        child2_2 = QTreeWidgetItem(child2)
        child2_2.setText(0,  "淡水鱼")
        QTreeWidgetItem(child2_2).setText(0, "活鲤鱼")
        QTreeWidgetItem(child2_2).setText(0, "活草鱼")
        QTreeWidgetItem(child2_2).setText(0, "白鲢活鱼")
        QTreeWidgetItem(child2_2).setText(0, "活鲫鱼")
        QTreeWidgetItem(child2_2).setText(0, "花鲢活鱼")

        child3 = QTreeWidgetItem(root1)
        child3.setText(0, '蔬菜')
        child3.setExpanded(True)
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

        layout.addWidget(self.tree, 1)  # 树控件添加到最大布局中
        self.tree.doubleClicked.connect(self.onTreeClicked)     # 双击信号，显示func
        self.tree.setColumnWidth(0, 300)  # 设置树控件的宽度

        # 右侧显示和选项放在groupBox里面
        # self.groupBox = QGroupBox()
        self.tab = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab.addTab(self.tab1, "时间序列")
        self.tab.addTab(self.tab2, "地点比较")
        self.tab.addTab(self.tab3, "同类比较")

        self.local_picture = QGridLayout(self.tab2)     # 三个选项卡的三个布局
        self.same_classification_picture = QGridLayout(self.tab3)
        self.F = MyFigure(width=3, height=2, dpi=100)   # 创建画布
        self.time_picture = QHBoxLayout(self.tab1)
        layout.addWidget(self.tab, 4)  # 组控件添加到最大布局中

        # 最后布局
        self.setCentralWidget(widget)
        widget.setLayout(layout)    # widget中设置布局

    # 点击的形成func
    def onTreeClicked(self, index):
        # 当前的项
        item = self.tree.currentItem()
        # 指定集合
        if item.text(0) in name:
            self.col = item.parent().parent().text(0)
            if self.col == '畜禽品':
                self.collection = db['meat']
            elif self.col == '水产品':
                self.collection = db['aqua']
            elif self.col == '蔬菜':
                self.collection = db['vege']
            elif self.col == '水果':
                self.collection = db['frut']

            # 地点比较的数据
            self.result = self.collection.find_one({'pro_name': item.text(0)})
            initData(self.result)   # 地点比较的图生成

            # 同类比较的数据
            self.results = self.collection.find({'classification': self.result['classification']})
            initDatas(self.results)

            self.draw_local_picture()
            self.draw_same_picture()
            self.draw_time_series()

    def draw_local_picture(self):   # 地点比较显示
        for i in range(self.local_picture.count()):
            self.local_picture.itemAt(i).widget().deleteLater()
        self.localHtml = QWebEngineView()
        # 打开本地html文件
        url = os.getcwd() + '/showhtml/' + self.tree.currentItem().text(0) + '.html'
        self.localHtml.load(QUrl.fromLocalFile(url))
        self.local_picture.addWidget(self.localHtml)

    def draw_same_picture(self):    # 同类比较显示
        for i in range(self.same_classification_picture.count()):
            self.same_classification_picture.itemAt(i).widget().deleteLater()
        self.sameHtml = QWebEngineView()
        # 打开本地html文件
        url = os.getcwd() + '/showhtml/' + self.tree.currentItem().parent().text(0) + '.html'
        self.sameHtml.load(QUrl.fromLocalFile(url))
        self.same_classification_picture.addWidget(self.sameHtml)

    def draw_time_series(self):
        # self.F.plotDoubleExponentialSmoothing(self.result['time_price'], alphas=[0.9], betas=[0.9])
        # self.time_picture.addWidget(self.F)
        if self.tree.currentItem().text(0) == '橙子':
            self.F.main(self.result['fair_price'])   # 绘制时间序列图    # self.F.tree_wholesale(self.result['time_price'])
            self.time_picture.addWidget(self.F)
        else:
            self.F.main(self.result['time_price'])  # 绘制时间序列图
            self.time_picture.addWidget(self.F)

    def closeEvent(self, event):  # 默认函数名，关闭应用弹出提示
        reply = QMessageBox.question(self, '退出提示', "你确定要退出吗？",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  # 默认为no
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


