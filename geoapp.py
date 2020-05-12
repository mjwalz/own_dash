"""Geomap dash."""
import dash
import dash_core_components as dcc
import dash_html_components as html
<<<<<<< HEAD
=======
# from dash.exceptions import PreventUpdate
# print(px.data.gapminder()[:15])#

import plotly.graph_objects as go

import pandas as pd
import json

# -------------------------------
import plotly.express as px
# df = px.data.election()
# geojson = px.data.election_geojson()
# file_name = 'data/gemeinden_simplify200.geojson'
# geojson = json.geojson(file_name)
# with open(file_name) as f:
#     data = json.load(f)

"""
type, crs, source, featuresPP
geojson:

type, properties, geometry, id
"""
# for counter, feature in enumerate(data['type']):
>>>>>>> 8c557aa09fe023f630fe655d0087495b5f54939c

from geo import create_geo_fig_title

fig, title = create_geo_fig_title('three')


app = dash.Dash()
app.layout = html.Div([
    html.H1(title),
    html.Div([
        dcc.Graph(figure=fig)
    ]),
])


# # Turn off reloader if inside Jupyter
# app.run_server(debug=True, use_reloader=True)
if __name__ == '__main__':
    app.run_server(8050, debug=True)
