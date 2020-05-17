# -*- coding: utf-8 -*-
# @Date     : 2017-04-11 21:27:00
# @Author   : Alan Lau (rlalan@outlook.com)
# @Language : Python3.5

from matplotlib import pyplot as plt
import matplotlib as mpl    # 创建绘图窗口
import seaborn as sns                            # 更多绘图功能
sns.set(style="darkgrid")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
mpl.rcParams['font.sans-serif'] = ['SimHei']    # 后即可正确显示中文  plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
mpl.use('Qt5Agg')    # print(matplotlib.get_backend())


class MyFigure(FigureCanvas):
    def __init__(self, width=18.5, height=10.5, dpi=100):
        plt.close('all')
        self.fig = Figure(figsize=(width, height), dpi=dpi)     # 设置图形的大小,以及每英寸的点数
        super(MyFigure, self).__init__(self.fig)    # 在父类中激活Figure窗口
        self.ax = self.fig.add_subplot(1, 1, 1)

    #指数平滑公式
    def exponential_smoothing(self, alpha, s):
        s2 = np.zeros(s.shape)  # s2表示预测值，预测值
        s2[0] = s[0]
        for i in range(1, len(s2)):
            s2[i] = alpha*s[i]+(1-alpha)*s2[i-1]
        return s2

    def main(self, time_price):
        alpha = 0.7        # 设置alphe，即平滑系数
        # 所有时间和数据
        time = list(time_price.keys())
        time.sort()
        initial_data = [float(time_price[time[0]])]  # 观测值
        for i in time:
            initial_data.append(float(time_price[i]))
        initial_data = np.array(initial_data)
        s_single = self.exponential_smoothing(alpha, initial_data)   # 计算一次指数平滑
        print(s_single)
        s_double = self.exponential_smoothing(alpha, s_single)   # 计算二次平滑指数，二次平滑指数是在一次指数平滑的基础上进行的，三次指数平滑以此类推

        a_double = 2*s_single-s_double                  # 计算二次指数平滑的a
        b_double = (alpha/(1-alpha))*(s_single-s_double)    # 计算二次指数平滑的b
        s_pre_double = np.zeros(len(s_double))         # 建立预测轴
        for i in range(0, len(s_pre_double)):
            s_pre_double[i] = a_double[i]+b_double[i]       # 循环计算每一年的二次指数平滑法的预测值，下面三次指数平滑法原理相同
                                                            # 意义完全改变,a[0]+b[0]得到的是下月的预测值
        print(s_pre_double)

        s_triple = self.exponential_smoothing(alpha, s_double)
        a_triple = 3*s_single-3*s_double+s_triple
        b_triple = (alpha/(2*((1-alpha)**2)))*((6-5*alpha)*s_single - 2*((5-4*alpha)*s_double)+(4-3*alpha)*s_triple)
        c_triple = ((alpha**2)/(2*((1-alpha)**2)))*(s_single-2*s_double+s_triple)
        s_pre_triple = np.zeros(len(s_triple))
        for i in range(0, len(s_pre_triple)):
            s_pre_triple[i] = a_triple[i]+b_triple[i]*1 + c_triple[i]*(1**2)

        print(s_pre_triple)

        time = time[-12:]
        data = initial_data[-12:]
        s_pre_double = s_pre_double[-13:]
        s_pre_triple = s_pre_triple[-13:]
        self.ax.clear()
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.ax.set_xticks(x)
        self.ax.set_xticklabels(time)
        self.ax.plot(data, color='blue', label="actual value", marker='o')      # 将实际值的折线设置为蓝色
        self.ax.plot(x, s_pre_double, color='red', label="double predicted value")      # 将二次指数平滑法计算的预测值的折线设置为红色
        self.ax.plot(x, s_pre_triple, color='green', label="triple predicted value")    # 将三次指数平滑法计算的预测值的折线设置为绿色
        self.ax.text(12, s_pre_double[12], '%.2f' % s_pre_double[12], family='monospace', fontsize=15)
        self.ax.text(12, s_pre_triple[12], '%.2f' % s_pre_triple[12], family='monospace', fontsize=15)
        self.ax.legend(loc='best')      # 显示图例的位置，这里为右下方
        self.ax.set_title('exponential smoothing')

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
