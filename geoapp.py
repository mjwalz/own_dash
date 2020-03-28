"""Geomap dash."""
import dash
import dash_core_components as dcc
import dash_html_components as html

from geo import create_geo_fig_title

fig, title = create_geo_fig_title('two')


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
