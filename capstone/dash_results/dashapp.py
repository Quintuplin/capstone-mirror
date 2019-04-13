from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import dash
import os

import dash_table

import numpy as np
import pandas as pd

from .server import app
from . import router
# change your directory


df = pd.read_csv('/home/cowdendt/Desktop/misc/capstone-2019-nist/capstone/dash_results/temp/que.csv')




colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict("rows"),
)