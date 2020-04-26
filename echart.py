from pyecharts.charts import Bar, Line
import pyecharts.options as opts


def initData(result):   # 折线图
    line = Line(init_opts=opts.InitOpts(width="1400px", height="900px"))
    name = result['pro_name']
    # result 数据拆分
    if 'super_price' in result:     # 超市价数据
        super_price = result['super_price']
        time = list(super_price.keys())     # 数据时间可能是乱的，需要排序
        time.sort()
        data = []
        for i in time:
            data.append(float(super_price[i]))      # 按照时间插入数据
        line.add_xaxis(xaxis_data=time)             # 折线图的x轴
        line.add_yaxis(series_name="超市价", y_axis=data,
               markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="最大值"),
                                                       opts.MarkPointItem(type_="min", name="最小值")]),
               markline_opts=opts.MarkLineOpts(data=[opts.MarkPointItem(type_="average", name="平均值")]))

    if 'mell_price' in result:      # 集市价数据
        mell_price = result['mell_price']
        time = list(mell_price.keys())
        time.sort()
        data = []
        for i in time:
            data.append(float(mell_price[i]))
        line.add_xaxis(xaxis_data=time)
        line.add_yaxis(series_name="集市价", y_axis=data,
               markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="最大值"),
                                                       opts.MarkPointItem(type_="min", name="最小值")]),
               markline_opts=opts.MarkLineOpts(data=[opts.MarkPointItem(type_="average", name="平均值")]))

    if 'time_price' in result:      # 批发价数据
        time_price = result['time_price']
        time = list(time_price.keys())
        time.sort()
        data = []
        for i in time:
            data.append(float(time_price[i]))
        line.add_xaxis(xaxis_data=time)
        line.add_yaxis(series_name="批发价", y_axis=data,
               markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="最大值"),
                                                       opts.MarkPointItem(type_="min", name="最小值")]),
               markline_opts=opts.MarkLineOpts(data=[opts.MarkPointItem(type_="average", name="平均值")]))
    # 设置全局选项
    line.set_global_opts(
        title_opts=opts.TitleOpts(title=name + '价格变化'),     # 图表名称
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    )
    line.render(name+'.html')


def initDatas(results):  # 柱状图
    bar = Bar(init_opts=opts.InitOpts(width="1400px", height="900px"))
    for result in results:
        name = result['pro_name']
        classification = result['classfication']
        if 'time_price' in result:
            time_price = result['time_price']
            time = list(time_price.keys())
            time.sort()
            data = []
            for i in time:
                data.append(float(time_price[i]))
            bar.add_xaxis(xaxis_data=time)
            bar.add_yaxis(series_name=name, yaxis_data=data)

    bar.set_global_opts(
        title_opts=opts.TitleOpts(title='同类批发价格比较与相关性'),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=True),
    )   # axislabel_opts=opts.LabelOpts(rotate=-15) x刻度旋转
    bar.render(classification + '.html')
