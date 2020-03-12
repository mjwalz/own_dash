import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

from sunburst import create_sunburst, get_sunburst

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)  # , external_stylesheets=external_stylesheets)

fig_one = create_sunburst(get_sunburst('ba'))
fig_two = create_sunburst(get_sunburst('ma'))
_, fig_one_title = get_sunburst('ba')
_, fig_two_title = get_sunburst('ma')

app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label=fig_one_title, value='tab-1'),
        dcc.Tab(label=fig_two_title, value='tab-2'),
    ]),
    html.Div(id='tabs-content')
])


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([

            html.H3(children=fig_one_title),
            # html.Div(children='Dash: Python framework to build web application'),

            # Insert plotly plot into dash
            dcc.Graph(id='graph_one', figure=fig_one)
        ], className='container'  # className='six columns'
        )
    elif tab == 'tab-2':
        return html.Div([

            html.H3(children=fig_two_title),
            # html.Label(['Use Plotly plot in Dash'], style={
            #     'font-weight': 'bold', "text-align": "center"}),
            # html.Div(children='Dash: Python framework to build web application'),

            # Insert plotly plot into dash
            dcc.Graph(id='graph_two', figure=fig_two)
        ], className='container'  # className='six columns'
        )


if __name__ == '__main__':
    app.run_server(8050, debug=True)
