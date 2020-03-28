"""Sunburst in TABs."""


import dash  # (version 1.8.0)
import dash_core_components as dcc
import dash_html_components as html
# from dash.exceptions import PreventUpdate
# print(px.data.gapminder()[:15])#

import plotly.graph_objects as go

import pandas as pd
import json

# -------------------------------
import plotly.express as px
# df = px.data.election()
# geojson = px.data.election_geojson()
file_name = 'data/gemeinden_simplify200.geojson'
# geojson = json.geojson(file_name)
with open(file_name) as f:
    data = json.load(f)

"""
type, crs, source, features
geojson:

type, properties, geometry, id
"""
# for counter, feature in enumerate(data['type']):

for counter, feature in enumerate(data['features']):
    # break
    print(counter, '------------')
    print('\n', feature, '\n', '\t', feature['geometry']['type'])
    print(counter, '------------')
    print('\n', feature, '\n', '\t', feature['geometry']['coordinates'])
    print(counter, '------------')
    print('\n', feature, '\n', '\t', feature['properties'])
    if counter == 0:
        break

# print(data['type'])
# print(data['crs'])
# print(df["district"][2])
# print(geojson["features"][0]["properties"])
# -------------------------------


df_dict = {
    'year': [year for year in range(1989, 2021)],
    'value': [val for val in range(5, (2021-1989)+5)]
}

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
#
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# # ---------------------------------------------------------------

fig = go.Figure(go.Scattergeo())
fig.update_layout(height=300, margin={"r": 0, "t": 0, "l": 0, "b": 0})


# # ---------------------------------------------------------------
app.layout = html.Div([

    html.Div([
        dcc.Graph(figure=fig, id='the_graph')
    ]),

])


# @app.callback(
#     [Output('the_graph')]
# def update_graph(df_dict):
#     """Update the callback."""
#     title='title_name'
#
#     fig=go.Figure(go.Scattergeo())
#     fig.update_layout(height=300, margin={"r": 0, "t": 0, "l": 0, "b": 0})
#
#     return fig, title
