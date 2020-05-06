"""The geo template."""
import plotly.express as px
import pandas as pd
import json
from urllib.request import urlopen
import os

file_name = 'gemeinden_simplify200.geojson'
data_path = 'data'
# cwd = os.getcwd()
file_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(file_dir, data_path, file_name)
# print(data_file)

# geojson = json.geojson(file_name)
with open(data_file) as f:
    data = json.load(f)

# print(data['features'][0])


def first_one():
    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        geojson = json.load(response)

    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                     dtype={"fips": str})
    # print(geojson['features'][0])
    print(df)

    fig = px.choropleth_mapbox(
        # a dict for column names like district, etx ...
        df,
        geojson=geojson,
        locations='fips',
        color='unemp',
        color_continuous_scale="Viridis",
        range_color=(0, 12),
        mapbox_style="carto-positron",
        zoom=3,
        center={"lat": 37.0902, "lon": -95.7129},
        # center={"lat": 47.40724, "lon": 54.9079},
        opacity=0.5,
        labels={'unemp': 'unemployment rate'}
        # -----------------------------------
        # -------------------------------
    )
    fig.update_geos(fitbounds="locations", visible=True)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    title = 'first one'
    return fig, title


def second_one():
    df = px.data.election()
    geojson = px.data.election_geojson()
    # print(geojson['features'][0])
    # #
    # print(data['features'][0])
    # print(df.head())
    # fig = px.choropleth(
    fig = px.choropleth_mapbox(
        # a dict for column names like district, counties etc ...
        df,
        geojson=geojson,
        color='Joly',  # color='winner',  # color='Bergeron',
        # this paints it
        locations="district",
        hover_name="district",
        featureidkey="properties.district",
        # needs CENTER!!!
        # -----------------------------------
        center={"lat": 45.5517, "lon": -73.7073},
        zoom=9,
        # center={
        #     "lat": 51.612,  # value raises into the north
        #     "lon": 10.391  # lower to the west
        # },
        # zoom=5,
        # center={
        #     "lat": 54.112,  # value raises into the north
        #     "lon": 10.391  # lower to the west
        # },
        # zoom=7,
        # -----------------------------------
        mapbox_style="carto-positron",
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    title = 'second one'

    return fig, title


def third_one():
    df = px.data.election()
    geojson = px.data.election_geojson()
    # print(geojson['features'][0])
    # #
    # print(data['features'][0])
    # print(df.head())
    fig = px.choropleth(
        # fig=px.choropleth_mapbox(
        # a dict for column names like district, counties etc ...
        df,
        geojson=geojson,
        color='winner',  # color='Joly',  # color='Bergeron',
        # this paints it
        locations="district",
        hover_name="district",
        featureidkey="properties.district",
        # needs CENTER!!!
        # -----------------------------------
        center={"lat": 45.5517, "lon": -73.7073},
        # zoom=9,
        # center={
        #     "lat": 51.612,  # value raises into the north
        #     "lon": 10.391  # lower to the west
        # },
        # zoom=5,
        # center={
        #     "lat": 54.112,  # value raises into the north
        #     "lon": 10.391  # lower to the west
        # },
        # zoom=7,
        # -----------------------------------
        # mapbox_style="carto-positron",
        # projection='natural earth',
        projection='orthographic',
        # projection='miller',
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    title = 'third one is like secound but not'

    return fig, title


def coro_gap():
    """Choropleth map for europe with gapminder data."""
    df = px.data.gapminder().query("year==2007")
    c_modes = ['lifeExp',
               'gdpPercap',
               'pop'
               ]
    continents = ['world', 'usa',
                  'europe', 'asia',
                  'africa', 'north america',
                  'south america']
    continent = continents[2]
    c_mode = c_modes[1]
    print(df.head())
    fig = px.choropleth(
        df,
        # color='lifeExp',
        color=c_mode,
        # color='pop',
        hover_name='country',
        locations='iso_alpha',
        # locations=["CA", "TX", "NY"],
        locationmode="ISO-3",
        scope=continent
    )

    title = 'The colored areas are {} data.'.format(c_mode.upper())
    return fig, title


def create_geo_fig_title(caller):
    """Create the map by {}."""  # TODO: {}.format() with something
    if caller == 'one':
        fig, title = first_one()
    elif caller == 'two':
        fig, title = second_one()
    elif caller == 'three':
        fig, title = third_one()
    elif caller == 'gap':
        fig, title = coro_gap()
    return fig, title
