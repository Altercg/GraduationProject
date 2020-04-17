from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox, \
    QDialog, QWidget, QTreeWidget, QTreeWidgetItem


class run_free(QMainWindow):
    def __init__(self, parent=None):
        super(run_free, self).__init__(parent)  # 显示调用父类的变量
        self.setWindowTitle('农产品物价_免费版')
        self.setWindowIcon(QIcon('timg.jpg'))
        self.resize(1800, 1000)  # 窗口大小,宽/高

        self.tree = QTreeWidget()
        self.tree.setColumnCount(1)
        self.tree.setHeaderLabels(['keys'])
        self.tree.setColumnWidth(0, 500)

        # 设置农产品物价信息根节点
        root1 = QTreeWidgetItem(self.tree)
        root1.setText(0, '农产品物价信息')

        # 添加子节点1，畜禽品
        child1 = QTreeWidgetItem(root1)
        child1.setText(0, '畜禽品')

        # 畜禽品细分
        pig = QTreeWidgetItem(child1)
        pig.setText(0, '猪肉')
        beef = QTreeWidgetItem(child1)
        beef.setText(0, '牛肉')
        mutton = QTreeWidgetItem(child1)
        mutton.setText(0, '羊肉')
        cock = QTreeWidgetItem(child1)
        cock.setText(0, '白条鸡')
        egg = QTreeWidgetItem(child1)
        egg.setText(0, '鸡蛋')

        # 添加子节点2，水产品
        child2 = QTreeWidgetItem(root1)
        child2.setText(0, '水产品')

        # 水产品细分
        ddfish = QTreeWidgetItem(child2)
        ddfish.setText(0, '大带鱼')
        dhhfish = QTreeWidgetItem(child2)
        dhhfish.setText(0, '大黄花鱼')
        hlfish = QTreeWidgetItem(child2)
        hlfish.setText(0, '活鲤鱼')
        hcfish = QTreeWidgetItem(child2)
        hcfish.setText(0, '活草鱼')
        blhfish= QTreeWidgetItem(child2)
        blhfish.setText(0, '白鲢活鱼')
        hjfish = QTreeWidgetItem(child2)
        hjfish.setText(0, '活鲫鱼')
        hlhfish = QTreeWidgetItem(child2)
        hlhfish.setText(0, '花鲢活鱼')

        # 添加子节点3，蔬菜
        child3 = QTreeWidgetItem(root1)
        child3.setText(0, '蔬菜')

        # 蔬菜细分
        bveg = QTreeWidgetItem(child3)
        bveg.setText(0, '菠菜')
        qveg = QTreeWidgetItem(child3)
        qveg.setText(0, '芹菜')
        yveg = QTreeWidgetItem(child3)
        yveg.setText(0, '油菜')
        dbveg = QTreeWidgetItem(child3)
        dbveg.setText(0, '大白菜')
        dg = QTreeWidgetItem(child3)
        dg.setText(0, '冬瓜')
        hg = QTreeWidgetItem(child3)
        hg.setText(0, '黄瓜')
        ng = QTreeWidgetItem(child3)
        ng.setText(0, '南瓜')
        xhl = QTreeWidgetItem(child3)
        xhl.setText(0, '西葫芦')
        blb = QTreeWidgetItem(child3)
        blb.setText(0, '白萝卜')
        hlb = QTreeWidgetItem(child3)
        hlb.setText(0, '胡萝卜')
        sj = QTreeWidgetItem(child3)
        sj.setText(0, '生姜')
        td = QTreeWidgetItem(child3)
        td.setText(0, '土豆')
        qz = QTreeWidgetItem(child3)
        qz.setText(0, '茄子')
        qj = QTreeWidgetItem(child3)
        qj.setText(0, '青椒')
        xhs = QTreeWidgetItem(child3)
        xhs.setText(0, '西红柿')
        ch = QTreeWidgetItem(child3)
        ch.setText(0, '菜花')
        ybc = QTreeWidgetItem(child3)
        ybc.setText(0, '洋白菜')
        dj = QTreeWidgetItem(child3)
        dj.setText(0, '豆角')
        ct = QTreeWidgetItem(child3)
        ct.setText(0, '葱头')
        ds = QTreeWidgetItem(child3)
        ds.setText(0, '大蒜')
        stai = QTreeWidgetItem(child3)
        stai.setText(0, '蒜苔')
        dc = QTreeWidgetItem(child3)
        dc.setText(0, '大葱')
        jc = QTreeWidgetItem(child3)
        jc.setText(0, '韭菜')
        ws = QTreeWidgetItem(child3)
        ws.setText(0, '莴笋')
        scai = QTreeWidgetItem(child3)
        scai.setText(0, '生菜')
        xg = QTreeWidgetItem(child3)
        xg.setText(0, '香菇')
        pg = QTreeWidgetItem(child3)
        pg.setText(0, '平菇')
        lo = QTreeWidgetItem(child3)
        lo.setText(0, '莲藕')

        # 添加子节点4，水果
        child4 = QTreeWidgetItem(root1)
        child4.setText(0, '水果')

        self.setCentralWidget(self.tree)

    def closeEvent(self, event):  # 默认函数名，关闭应用弹出提示
        reply = QMessageBox.question(self, '退出提示', "你确定要退出吗？",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  # 默认为no
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
