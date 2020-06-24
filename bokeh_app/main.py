import os

from bokeh.io import curdoc
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, BoxAnnotation, Toggle, HoverTool, Button
from bokeh.layouts import row, column, gridplot, layout, Spacer
from bokeh.models.widgets import Tabs, Panel, DatePicker, Slider, PreText
from bokeh.palettes import Dark2_5 as palette
from bokeh.models import ColumnDataSource

import numpy as np
import pandas as pd
import itertools
from PredictionVisualization import PredictionVisualization
from datetime import date, datetime

# importing data
vd = PredictionVisualization()
df_cases_transport = vd.df_cases_transport
df_london_mobility = vd.df_london_mobility
df_uk_mobility = vd.df_uk_mobility
tfl_tube = df_cases_transport[['Date', 'Tfl Tube use change percentage']]
national_rail = df_cases_transport[['Date', 'National rail use change percentage']]
df_cases_transport['new_cases_world'] = df_cases_transport['new_cases_world']
df_cases_transport['world_deaths'] = df_cases_transport['world_deaths']

colors = itertools.cycle(palette)

source_tfl = ColumnDataSource(tfl_tube)
source_rail = ColumnDataSource(national_rail)
source_london_mob = ColumnDataSource(df_london_mobility)
source_uk_mob =ColumnDataSource(df_london_mobility)
source_cases = df_cases_transport
# Specify input for data prediction
predictedDataSource_tfl = ColumnDataSource(data=dict(Date=[], prediction=[]))
predictedDataSource_rail = ColumnDataSource(data=dict(Date=[], prediction=[]))





# Set up the figures for Predictor Data

## Set up the figure for london mobility
fig_london_mob = figure(
    title="COVID-19 Mobility Variables for London",
    plot_height=550,
    plot_width=900,
    x_axis_label="Date",
    y_axis_label="Change from the baseline in %",
    x_minor_ticks=2,
    y_range=(-150, 170),
    toolbar_location=None,
    x_axis_type="datetime",
)
# Connect to and draw the data
for c in df_london_mobility.iloc[:, 1:]:
    # create a new plot with a title and axis labels
    fig_london_mob.line(
        x="Date",
        y=c,
        source=source_london_mob,
        line_width=2,
        legend_label=str(c).replace("_", " ").title(),
        color=next(colors),
    )
fig_london_mob.legend.location = "top_left"
fig_london_mob.legend.click_policy = "hide"
# add a box showing the national lockdown

box_left = pd.to_datetime("23-3-2020")
box_right = pd.to_datetime("10-6-2020")
box_london_mob = BoxAnnotation(
    left=box_left,
    right=box_right,
    line_width=1,
    line_color="black",
    line_dash="dashed",
    fill_alpha=0.2,
    fill_color="orange",
    name="Lockdown Introduction",
)
fig_london_mob.add_layout(box_london_mob)
fig_london_mob.xaxis.major_tick_line_color = "firebrick"
fig_london_mob.xaxis.major_tick_line_width = 1
fig_london_mob.xaxis.minor_tick_line_color = "black"
toggle_london_mob = Toggle(label="Show National Lockdown", button_type="success", active=True)
toggle_london_mob.js_link("active", box_london_mob, "visible")



## Set up the figure for UK mobility
fig_uk_mob = figure(
    title="COVID-19 Mobility Variables for UK",
    plot_height=550,
    plot_width=900,
    x_axis_label="Date",
    y_axis_label="Change from the baseline in %",
    x_minor_ticks=2,
    y_range=(-150, 170),
    toolbar_location=None,
    x_axis_type="datetime",
)
# Connect to and draw the data
for c in df_uk_mobility.iloc[:, 1:]:
    # create a new plot with a title and axis labels
    fig_uk_mob.line(
        x="Date",
        y=c,
        source=source_uk_mob,
        line_width=2,
        legend_label=str(c).replace("_", " ").title(),
        color=next(colors),
    )
fig_uk_mob.legend.location = "top_left"
fig_uk_mob.legend.click_policy = "hide"
# add a box showing the national lockdown

box_left = pd.to_datetime("23-3-2020")
box_right = pd.to_datetime("10-6-2020")
box_uk_mob = BoxAnnotation(
    left=box_left,
    right=box_right,
    line_width=1,
    line_color="black",
    line_dash="dashed",
    fill_alpha=0.2,
    fill_color="orange",
    name="Lockdown Introduction",
)
fig_uk_mob.add_layout(box_uk_mob)
fig_uk_mob.xaxis.major_tick_line_color = "firebrick"
fig_uk_mob.xaxis.major_tick_line_width = 1
fig_uk_mob.xaxis.minor_tick_line_color = "black"
toggle_uk_mob = Toggle(label="Show National Lockdown", button_type="success", active=True)
toggle_uk_mob.js_link("active", box_uk_mob, "visible")




## Set up the figure for new cases and deaths worldwide
fig_deaths = figure(
    title="COVID-19 Deaths and Cases worldwide",
    plot_height=550,
    plot_width=900,
    x_axis_label="Date",
    y_axis_label="Number of cases/deaths per day",
    x_minor_ticks=2,
    y_range=(0, 150000),
    toolbar_location=None,
    x_axis_type="datetime",
)
# Connect to and draw the data
    # create a new plot with a title and axis labels
fig_deaths.line(
        x="Date",
        y="world_deaths",
        source=source_cases,
        line_width=2,
        legend_label='Number of fatal cases worldwide in 100s',
        color=next(colors),
    )
fig_deaths.line(
    x="Date",
    y="new_cases_world",
    source=source_cases,
    line_width=2,
    legend_label='Number of infection cases worldwide in 1000s',
    color=next(colors),
)
fig_deaths.legend.location = "top_left"
fig_deaths.legend.click_policy = "hide"
# add a box showing the national lockdown

box_left = pd.to_datetime("23-3-2020")
box_right = pd.to_datetime("10-6-2020")
box_deaths = BoxAnnotation(
    left=box_left,
    right=box_right,
    line_width=1,
    line_color="black",
    line_dash="dashed",
    fill_alpha=0.2,
    fill_color="orange",
    name="Lockdown Introduction",
)
fig_deaths.add_layout(box_deaths)
fig_deaths.xaxis.major_tick_line_color = "firebrick"
fig_deaths.xaxis.major_tick_line_width = 1
fig_deaths.xaxis.minor_tick_line_color = "black"
toggle_deaths = Toggle(label="Show National Lockdown", button_type="success", active=True)
toggle_deaths.js_link("active", box_deaths, "visible")


## Set up the figure for new cases and deaths in the UK
fig_cases_uk = figure(
    title="COVID-19 Deaths and Cases in the UK",
    plot_height=550,
    plot_width=900,
    x_axis_label="Date",
    y_axis_label="Number of cases/deaths per day",
    x_minor_ticks=2,
    y_range=(-1000, 10000),
    toolbar_location=None,
    x_axis_type="datetime",
)
# Connect to and draw the data
    # create a new plot with a title and axis labels
fig_cases_uk.line(
        x="Date",
        y="uk_deaths",
        source=source_cases,
        line_width=2,
        legend_label='Number of fatal cases in the UK',
        color=next(colors),
    )
fig_cases_uk.line(
    x="Date",
    y="new_cases_uk",
    source=source_cases,
    line_width=2,
    legend_label='Number of infection cases in the UK',
    color=next(colors),
)
fig_cases_uk.legend.location = "top_left"
fig_cases_uk.legend.click_policy = "hide"
# add a box showing the national lockdown

box_left = pd.to_datetime("23-3-2020")
box_right = pd.to_datetime("10-6-2020")
box_cases_uk = BoxAnnotation(
    left=box_left,
    right=box_right,
    line_width=1,
    line_color="black",
    line_dash="dashed",
    fill_alpha=0.2,
    fill_color="orange",
    name="Lockdown Introduction",
)
fig_cases_uk.add_layout(box_cases_uk)
fig_cases_uk.xaxis.major_tick_line_color = "firebrick"
fig_cases_uk.xaxis.major_tick_line_width = 1
fig_cases_uk.xaxis.minor_tick_line_color = "black"
toggle_cases_uk = Toggle(label="Show National Lockdown", button_type="success", active=True)
toggle_cases_uk.js_link("active", box_cases_uk, "visible")

## Set up the figure for new cases and deaths in London
fig_cases_london = figure(
    title="COVID-19 Deaths and Cases in London",
    plot_height=550,
    plot_width=900,
    x_axis_label="Date",
    y_axis_label="Number of cases/deaths per day",
    x_minor_ticks=2,
    y_range=(0, 1500),
    toolbar_location=None,
    x_axis_type="datetime",
)
# Connect to and draw the data
    # create a new plot with a title and axis labels
fig_cases_london.line(
        x="Date",
        y="london_deaths",
        source=source_cases,
        line_width=2,
        legend_label='Number of fatal cases in London',
        color=next(colors),
    )
fig_cases_london.line(
    x="Date",
    y="new_cases_london",
    source=source_cases,
    line_width=2,
    legend_label='Number of infection cases in London',
    color=next(colors),
)
fig_cases_london.legend.location = "top_left"
fig_cases_london.legend.click_policy = "hide"
# add a box showing the national lockdown

box_left = pd.to_datetime("23-3-2020")
box_right = pd.to_datetime("10-6-2020")
box_cases_london = BoxAnnotation(
    left=box_left,
    right=box_right,
    line_width=1,
    line_color="black",
    line_dash="dashed",
    fill_alpha=0.2,
    fill_color="orange",
    name="Lockdown Introduction",
)
fig_cases_london.add_layout(box_cases_london)
fig_cases_london.xaxis.major_tick_line_color = "firebrick"
fig_cases_london.xaxis.major_tick_line_width = 1
fig_cases_london.xaxis.minor_tick_line_color = "black"
toggle_cases_london = Toggle(label="Show National Lockdown", button_type="success", active=True)
toggle_cases_london.js_link("active", box_cases_london, "visible")

# Set up the figure for TfL Use prediction
fig_tfl = figure(
    title="Predict the UK Transport Demand",
    plot_height=550,
    plot_width=900,
    x_axis_label="Date",
    y_axis_label="Change from the baseline in %",
    x_minor_ticks=2,
    y_range=(-150, 170),
    toolbar_location=None,
    x_axis_type="datetime",
)  # Instantiate a figure() object
fig_tfl.circle(
    x="Date", y="prediction", source=predictedDataSource_tfl, size=7, color="red"
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
box_tfl = BoxAnnotation(
    left=box_left,
    right=box_right,
    line_width=1,
    line_color="black",
    line_dash="dashed",
    fill_alpha=0.2,
    fill_color="orange",
    name="Lockdown Introduction",
)


# Set up the figure for National Rail Use
fig_rail = figure(
    title="Predict National Rail Demand",
    plot_height=550,
    plot_width=900,
    x_axis_label="Date",
    y_axis_label="Change from the baseline in %",
    x_minor_ticks=2,
    y_range=(-150, 170),
    toolbar_location=None,
    x_axis_type="datetime",
)  # Instantiate a figure() object
fig_rail.circle(
    x="Date", y="prediction", source=predictedDataSource_rail, size=7, color="red"
)
# Connect to and draw the data
for c in national_rail.iloc[:, 1:]:
    # output to static HTML file
    # create a new plot with a title and axis labels
    fig_rail.line(
        x="Date",
        y=c,
        source=source_rail,
        line_width=2,
        legend_label=str(c).replace("_", " ").title(),
        color=next(colors),
    )
fig_rail.legend.location = "top_left"
fig_rail.legend.click_policy = "hide"
# add a box showing the national lockdown


box_rail = BoxAnnotation(
    left=box_left,
    right=box_right,
    line_width=1,
    line_color="black",
    line_dash="dashed",
    fill_alpha=0.2,
    fill_color="orange",
    name="Lockdown Introduction",
)
fig_rail.add_layout(box_rail)
fig_rail.xaxis.major_tick_line_color = "firebrick"
fig_rail.xaxis.major_tick_line_width = 1
fig_rail.xaxis.minor_tick_line_color = "black"
toggle_rail = Toggle(label="Show National Lockdown", button_type="success", active=True)
toggle_rail.js_link("active", box_rail, "visible")




fig_tfl.add_layout(box_tfl)
fig_tfl.xaxis.major_tick_line_color = "firebrick"
fig_tfl.xaxis.major_tick_line_width = 1
fig_tfl.xaxis.minor_tick_line_color = "black"
toggle_tfl = Toggle(label="Show National Lockdown", button_type="success", active=True)
toggle_tfl.js_link("active", box_tfl, "visible")




def update_tfl():
    date = datetime.strptime(datePicker_tfl.value, "%Y-%m-%d")
    params = [[int(newCasesWorld_tfl.value), int(mobility_tfl.value)]]
    predict_tfl = vd.predict_transport_use("TfL Tube", params)
    predictedDataSource_tfl.stream(dict(Date=[date], prediction=predict_tfl))


newCasesWorld_tfl = Slider(title="New Cases World", value=10, start=0, end=700000, step=1)
mobility_tfl = Slider(title="Mobility", value=0, start=-400, end=400, step=1)
datePicker_tfl = DatePicker(title="Date", min_date=date(2020, 3, 1), max_date=date.today())
preidctToggle_tfl = Button(label="Predict TfL Tube Demand")
preidctToggle_tfl.on_click(lambda event: update_tfl())


def update_rail():
    date = datetime.strptime(datePicker_rail.value, "%Y-%m-%d")
    params = [[int(newCasesWorld_rail.value), int(mobility_rail.value)]]
    predict_rail = vd.predict_transport_use("National Rail", params)
    predictedDataSource_rail.stream(dict(Date=[date], prediction=predict_rail))


newCasesWorld_rail = Slider(title="New Cases World", value=10, start=0, end=700000, step=1)
mobility_rail = Slider(title="Mobility", value=0, start=-400, end=400, step=1)
datePicker_rail = DatePicker(title="Date", min_date=date(2020, 3, 1), max_date=date.today())
preidctToggle_rail = Button(label="Predict National Rail Demand")
preidctToggle_rail.on_click(lambda event: update_rail())

# Add text
pre = PreText(text="""
Below you can find some Transport Demand Prediction-related visualizations:
 1) Data used for prediction;
 2) An interactive tool, that predicts how the demand for transport in the UK will change
according to your input data.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To hide/show the variables, press on their name on the legend.
To hide/show the period of the National Lockdown in the UK, press the green button under the plots.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")

pre_uk = PreText(text="""
The negative number of cases in the UK on March 21 represents a recalculation that was done on that day.
""")

pre_pred_tfl = PreText(text="""
To see how TfL Tube use would change according to the changing number of cases worldwide
and the change in mobility in % (I used transit station mobility change, as the variable most 
correlating with TfL Use), choose the date, number of cases, and mobility change %,
then press 'Predict TfL Tube Demand'.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")

pre_pred_rail = PreText(text="""
To see how the UK National Rail use would change according to the changing number of cases worldwide
and the change in mobility in % (I used retail and recreation mobility change, as the variable most 
correlating with National Rail Use), choose the date, number of cases, and mobility change %,
then press 'Predict National Rail Demand'.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")

mobility = column(pre , Spacer(height=20), fig_london_mob,toggle_london_mob, Spacer(height=20), fig_uk_mob, toggle_uk_mob)
worldwide_cases = column(fig_deaths, toggle_deaths)
uk_cases = column(fig_cases_uk, toggle_cases_uk)
london_cases = column(fig_cases_london, toggle_cases_london)
tfl_prediction = column(datePicker_tfl, newCasesWorld_tfl, mobility_tfl, preidctToggle_tfl, fig_tfl, toggle_tfl)
rail_prediction = column(datePicker_rail, newCasesWorld_rail, mobility_rail, preidctToggle_rail, fig_rail, toggle_rail)


l = layout(
    [   [column(mobility, Spacer(height=30) ,worldwide_cases )],
        [column(Spacer(height=40), pre_uk, Spacer(height=20), uk_cases, Spacer(height=20), london_cases)],
        [column(Spacer(height=40), pre_pred_tfl, tfl_prediction)],
        [column(Spacer(height=40), pre_pred_rail, rail_prediction)],
    ],
    sizing_mode="scale_both",
    max_width = 900
)

curdoc().add_root(l)