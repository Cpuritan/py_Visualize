import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import Pie, TreeMap, Line

plt.style.use("seaborn-darkgrid")
# 显示中文，设置字体
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

area = ["金融", "医疗保健", "市场业", "零售业", "制造业", "司法", "工程与科学", "保险业", "其他"]
vote = [172, 136, 135, 101, 80, 68, 50, 29, 41]
# 绘制饼图
plt.pie(vote, labels=area, autopct='%.1f%%')  # 显示百分比
plt.title("感兴趣的数据领域_BQF")
plt.show()

pie = (
    Pie(init_opts=opts.InitOpts(width="1200px", height="800px"))
        .add("", data_pair=[list(z) for z in zip(area, vote)])  # 导入数据
        # ,rosetype=area)
        .set_global_opts(title_opts=opts.TitleOpts(title="感兴趣的数据领域"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="领域:{b}---票数{c}比例{d}%", position='inside'))  #

        .render("饼图_鲍其峰.html")
)
# 绘制环形图
plt.pie(vote, labels=area, autopct='%1.1f%%', startangle=90, counterclock=False, radius=0.9)
plt.pie([1], radius=0.3, colors='w', labeldistance=-0.0001)
plt.title("感兴趣的数据领域_环形图_BQF")
plt.show()

pie_huan = (
    Pie(init_opts=opts.InitOpts(width="1200px", height="800px"))
        .add("", data_pair=[list(z) for z in zip(area, vote)], radius=[210, 300])
        # ,rosetype=area)
        .set_global_opts(title_opts=opts.TitleOpts(title="感兴趣的数据领域"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="领域:{b}---票数{c}比例{d}%", position='inside'))  #
        # .set_series_opts(label_opts=opts.LabelOpts(formatter="领域:{b}))
        .render("环形图_BQF.html")
)
# 绘制堆叠柱状图
question = ["种族问题", "教育", "恐怖活动", "能源政策", "外交事务", "环境", "宗教政策",
            "税收", "医疗保健政策", "经济", "就业政策", "贸易政策", "外来移民"]
agree = [52, 49, 48, 47, 44, 43, 41, 41, 40, 38, 36, 31, 29]
disagree = [38, 40, 45, 42, 48, 51, 53, 54, 57, 59, 57, 64, 62]
noview = [10, 11, 7, 11, 8, 6, 6, 5, 3, 3, 7, 5, 9]
ddd = [i + j for i, j in zip(agree, disagree)]
l1 = plt.bar(np.arange(len(question)), agree, fc='r', width=0.3)
l2 = plt.bar(np.arange(len(question)), disagree, fc='b', width=0.3, bottom=agree)
l3 = plt.bar(np.arange(len(question)), noview, fc='y', width=0.3, bottom=ddd)

plt.legend(handles=[l1[0], l2[0], l3[0]], labels=['支持', '反对', '不发表意见'])
plt.xticks(np.arange(len(question)), question, rotation=45)
plt.ylabel('票数')
plt.title('奥巴马政治举措投票情况可视化_BQF')
plt.show()

# 绘制矩阵层级图
data = [
    {"value": 235, "name": "北京"},
    {
        "value": 268,
        "name": "湖北",
        "children": [
            {
                "value": 76,
                "name": "武汉",
                "children": [
                    {"value": 12, "name": "洪山区"},
                    {"value": 28, "name": "东湖高新"},
                    {"value": 20, "name": "江夏区"},
                ],
            },
            {"value": 67, "name": "鄂州"},
            {"value": 34, "name": "襄阳"}
        ],
    },
    {
        "value": 633,
        "name": "湖南",
        "children": [
            {
                "value": 76,
                "name": "长沙",
                "children": [
                    {"value": 55, "name": "雨花区"},
                    {"value": 34, "name": "岳麓区"},
                    {"value": 144, "name": "天心区"},
                ]
            },
            {
                "value": 290,
                "name": "常德",
                "children": [
                    {"value": 156, "name": "武陵区"},
                    {"value": 134, "name": "鼎城区"},
                ]
            },
            {"value": 87, "name": "湘潭"},
            {"value": 23, "name": "株洲"}]}
]
c = (
    TreeMap()
    .add("标准矩阵树图", data)
    .set_global_opts(title_opts=opts.TitleOpts(title="标准矩阵树图"))
    .render("矩阵树图_BQF.html")
)

# 可视化美国1860年—2005年间人口老龄化的变化情况
df = pd.read_excel(r'us-population-by-age.xls')
time = ["1860", "1870", "1880", "1890", "1900", "1910", "1920",
 "1930", "1940", "1950", "1960", "1970", "1980", "1990", "2000"]#list(df.iloc[:15, 0])
t_5 = df.iloc[:15, 1]
t_19 = df.iloc[:15, 2]
t_44 = df.iloc[:15, 3]
t_64 = df.iloc[:15, 4]
t_65 = df.iloc[:15, 5]

Line_square = (
    Line()
    .add_xaxis(xaxis_data=time)
    .add_yaxis(series_name="<5 years", y_axis=list(t_5), stack="stack", is_smooth=True, is_connect_nones=True)
    .add_yaxis(series_name="9-19 years", y_axis=list(t_19), stack="stack", is_smooth=True, is_connect_nones=True)
    .add_yaxis(series_name="20-44 years", y_axis=list(t_44), stack="stack", is_smooth=True, is_connect_nones=True)
    .add_yaxis(series_name="44-64 years", y_axis=list(t_64), stack="stack", is_smooth=True, is_connect_nones=True)
    .add_yaxis(series_name=">65 years", y_axis=list(t_65), stack="stack", is_smooth=True, is_connect_nones=True)
    .set_global_opts(title_opts=opts.TitleOpts(title="人口老龄化趋势图"))
    .set_series_opts(areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
    .render("square_BQF.html")
    )
