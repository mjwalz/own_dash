"""The geo template."""
import plotly.graph_objects as go

from urllib.request import urlopen
import json

import pandas as pd

import plotly.express as px
df = px.data.election()
print(df.head())


def create_geo_fig_title(caller):
    """Create the geo by geo_dict."""
    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)

    # df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
    #                  dtype={"fips": str})

    fig = go.Figure(go.Choroplethmapbox(
        geojson=counties,
        locations=df.Coderre,
        z=df.total,
        # projection='natural earth',
        projection='orthographic',
        colorscale="Viridis",
        zmin=0,
        zmax=12,
        marker_opacity=0.5,
        marker_line_width=0))

    fig.update_layout(mapbox_style="carto-positron",
                      mapbox_zoom=3,
                      mapbox_center={"lat": 37.0902, "lon": -95.7129})
    fig.update_layout(
        margin={"r": 0,
                "t": 0,
                "l": 0,
                "b": 0}
    )

    geo_title = 'First MAP'

    return fig, geo_title
