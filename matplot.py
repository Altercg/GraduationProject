import matplotlib as mpl    # 创建绘图窗口
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter # 设置刻度间隔
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import sort

mpl.rcParams['font.sans-serif'] = ['SimHei']    # 后即可正确显示中文  plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
mpl.use('Qt5Agg')    # print(matplotlib.get_backend())


class MyFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)     # 设置图形的大小,以及每英寸的点数
        super(MyFigure, self).__init__(self.fig)    # 在父类中激活Figure窗口

    def plotax(self, time_price):
        self.ax = self.fig.add_subplot(1, 1, 1)
        time = sort(list(time_price.keys()))
        data = []
        for i in time:
            data.append(float(time_price[i]))
        # y主刻度
        # self.ax.set_ylim(20, 100)
        # y_major_locator = MultipleLocator(10)
        # y_major_formatter = FormatStrFormatter('%.2f')
        # self.ax.yaxis.set_major_locator(y_major_locator)
        # self.ax.yaxis.set_major_formatter(y_major_formatter)
        # 次刻度
        # y_minor_locator = MultipleLocator(1)
        # self.ax.yaxis.set_minor_locator(y_minor_locator)
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        self.ax.set_xticklabels(time)
        self.ax.plot(x, data, linestyle='-', marker='o')









'''
fig = plt.figure()    # fig 图片对象
ax = fig.add_subplot(1, 1, 1)    # 创建2*2的子图
ax.plot(np.random.randn(1000).cumsum())

ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
# plt.plot([1.5, 3.5, -2, 1.6])
plt.plot(np.random.randn(50).cumsum(), 'k--')  # k-- 表示分线段的style
_ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)   # 柱状 bin:总共有几条条状图 alpha: 透明度
ax2.scatter(np.arange(30), np.array(30) + 3*np.random.randn(30))    # 点散图
# plt.plot(np.random.randn(30).cumsum(), 'ko--', label='Default')
# plt.plot(np.random.randn(30).cumsum(), 'ko-', drawstyle='steps-post', label='steps-post') # label表示这条线叫什么
plt.legend(loc='best')  # 生出图例
ticks = ax.set_xticks([0, 250, 500, 750, 1000])   # 设置x轴的刻度位置
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')  # rotation 旋转
ax.set_title('My')
plt.show()
'''