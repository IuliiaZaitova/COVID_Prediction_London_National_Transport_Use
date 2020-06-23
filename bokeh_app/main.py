import os
from random import random

from bokeh.io import curdoc
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, BoxAnnotation, Toggle, HoverTool, Button
from bokeh.layouts import row, column, gridplot, layout
from bokeh.models.widgets import Tabs, Panel, DatePicker, Slider
from bokeh.palettes import Dark2_5 as palette
from bokeh.models import ColumnDataSource, HoverTool, Panel

import numpy as np
import pandas as pd
import itertools
from PredictionVisualization import PredictionVisualization
from datetime import date, datetime


pd.options.display.max_rows = 500
pd.options.display.max_columns = 500
pd.set_option("display.max_colwidth", 500)

# importing data

vd = PredictionVisualization()
df_cases_transport = vd.df_cases_transport
df_london_mobility = vd.df_london_mobility
df_uk_mobility = vd.df_uk_mobility
tfl_tube = df_cases_transport[['Date', 'Tfl Tube use change percentage']]
national_rail = df_cases_transport[['Date', 'National rail use change percentage']]


colors = itertools.cycle(palette)

source_tfl = ColumnDataSource(tfl_tube)
source_rail = ColumnDataSource(national_rail)
predictedDataSource = ColumnDataSource(data=dict(Date=[], prediction=[]))

# Set up the figure(s)
fig_tfl = figure(
    title="Predict TfL Tube Demand",
    plot_height=400,
    plot_width=700,
    x_axis_label="Date",
    y_axis_label="Change from the baseline in %",
    x_minor_ticks=2,
    y_range=(-150, 170),
    toolbar_location=None,
    x_axis_type="datetime",
)  # Instantiate a figure() object
fig_tfl.circle(
    x="Date", y="prediction", source=predictedDataSource, size=7, color="red"
)
# Connect to and draw the data
for c in tfl_tube.iloc[:, 1:]:
    # output to static HTML file
    # create a new plot with a title and axis labels
    fig_tfl.line(
        x="Date",
        y=c,
        source=source_tfl,
        line_width=2,
        legend_label=str(c).replace("_", " ").title(),
        color=next(colors),
    )
fig_tfl.legend.location = "top_left"
fig_tfl.legend.click_policy = "hide"
# add a box showing the national lockdown

box_left = pd.to_datetime("23-3-2020")
box_right = pd.to_datetime("10-6-2020")
box = BoxAnnotation(
    left=box_left,
    right=box_right,
    line_width=1,
    line_color="black",
    line_dash="dashed",
    fill_alpha=0.2,
    fill_color="orange",
    name="Lockdown Introduction",
)
fig_tfl.add_layout(box)
fig_tfl.xaxis.major_tick_line_color = "firebrick"
fig_tfl.xaxis.major_tick_line_width = 1
fig_tfl.xaxis.minor_tick_line_color = "black"
toggle_tfl = Toggle(label="Show National Lockdown", button_type="success", active=True)
toggle_tfl.js_link("active", box, "visible")




def update():
    date = datetime.strptime(datePicker.value, "%Y-%m-%d")
    params = [[int(newCasesWorld.value), int(mobility.value)]]
    predict = vd.predict_transport_use("TfL Tube", params)
    predictedDataSource.stream(dict(Date=[date], prediction=predict))


newCasesWorld = Slider(title="New Cases World", value=10, start=0, end=700000, step=1)
mobility = Slider(title="Mobility", value=0, start=-400, end=400, step=1)
datePicker = DatePicker(title="Date", min_date=date(2020, 3, 1), max_date=date.today())
preidctToggle = Button(label="Predict")
preidctToggle.on_click(lambda event: update())

l = layout(
    [
        [
            column(datePicker, newCasesWorld, mobility, preidctToggle),
            column(fig_tfl, toggle_tfl),
        ],
    ],
    sizing_mode="scale_both",
)

curdoc().add_root(l)