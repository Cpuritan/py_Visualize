import pandas as pd
from pyecharts.charts import Line, Bar, Polar, Page
from pyecharts.faker import Faker
import pyecharts.options as opts
datax = ["2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010"]
datay = [0.32,    0.32,   0.35,   0.35,   0.39,   0.41,   0.41,   0.45,   0.47,   0.47]

line = (
    Line()
    .add_xaxis(xaxis_data=datax)
    .add_yaxis(series_name="Price", y_axis=datay, is_step=True
               , label_opts=opts.LabelOpts(is_show=True))
    .set_global_opts(title_opts=opts.TitleOpts(title="美感邮票阶梯图"),
                     yaxis_opts=opts.AxisOpts(
                         type_="value",
                         min_=0.3,
                         max_=100.45
                        ))
    .render()
)

df = pd.read_csv('hot-dog-places.csv')
bar = (
    Bar(init_opts=opts.InitOpts(width="1200px", height="800px"))
    .add_xaxis(list(df.columns))
    .add_yaxis(series_name="The First", y_axis=list(df.iloc[0, :]), stack="stack")
    .add_yaxis(series_name="The Second", y_axis=list(df.iloc[1, :]), stack="stack")
    .add_yaxis(series_name="The Third", y_axis=list(df.iloc[2, :]), stack="stack")
    .set_global_opts(title_opts=opts.TitleOpts("堆叠柱状图", pos_left="left"),
                     legend_opts=opts.LegendOpts(
                         pos_left="center", pos_top="top", orient="horizontal"),
                     yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True))
                     )
    #.render("hot_dogs_bar_stack.html")
)

pol = (
    Polar(init_opts=opts.InitOpts(width="1200px", height="800px"))
    .add_schema(radiusaxis_opts=opts.RadiusAxisOpts(data=list(df.columns), type_="category"))
    .add("The First", list(df.iloc[0, :]), type_="bar", stack="stack0")
    .add("The Second", list(df.iloc[1, :]), type_="bar", stack="stack0")
    .add("The Third", list(df.iloc[2, :]), type_="bar", stack="stack0")
    .set_global_opts(title_opts=opts.TitleOpts("极坐标堆叠柱状图1", pos_left="left"))
    #.render("hot_dogs_polar_stack.html")
)

pol1 = (
    Polar(init_opts=opts.InitOpts(width="1200px", height="800px"))
    .add_schema(angleaxis_opts=opts.AngleAxisOpts(data=list(df.columns), type_="category"))
    .add("The First", list(df.iloc[0, :]), type_="bar", stack="stack0")
    .add("The Second", list(df.iloc[1, :]), type_="bar", stack="stack0")
    .add("The Third", list(df.iloc[2, :]), type_="bar", stack="stack0")
    .set_global_opts(title_opts=opts.TitleOpts("极坐标堆叠柱状图2", pos_left="left"))
)

page = Page(layout=Page.DraggablePageLayout)
page.add(bar, pol, pol1)
page.render("hot_dogs_BQF.html")
