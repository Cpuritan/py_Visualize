import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from pyecharts import options as opts
from pyecharts.charts import Graph

# 数据清洗--过滤出中国 电影
df = pd.read_excel(r'./TOP250.xlsx')
df = df[df['国家/地区'] == "中国"]
df["主演"] = df["主演"].apply(lambda x: x.split(' / '))
df["symbolSize"] = df["主演"].apply(lambda x: str(len(x)))  # json不认识int6


# 数据转换字典
def excelToDict(df):
    # 创建最终返回的空字典
    df_dict = {}
    # 替换Excel表格内的空单元格，否则在下一步处理中将会报错
    df.fillna("", inplace=True)
    df_list = []
    for i in df.index.values:
        # loc为按列名索引 iloc 为按位置索引，使用的是 [[行号], [列名]]
        df_line = df.loc[i, ['导演', 'symbolSize', '主演']].to_dict()
        # 将每一行转换成字典后添加到列表
        df_list.append(df_line)
    df_dict['data'] = df_list
    return [df_list]


data_dict = excelToDict(df)
print(data_dict)

with open("write_json.json", "w", encoding='utf-8') as f:
    # json.dump(dict_, f) # 写为一行
    json.dump(data_dict, f, indent=2, ensure_ascii=False) # 写为多行

with open("write_json.json", "r", encoding="utf-8") as f:
    j = json.load(f)
    nodes, links, categories = j  #, cont, mid, userl = j
c = (
    Graph()
    .add(
        "",
        nodes,
        links,
        categories,
        repulsion=50,
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        title_opts=opts.TitleOpts(title="Graph-华语电影导演演员关系图——鲍其峰"),
    )
    .render("graph_movie_actor.html")
)

