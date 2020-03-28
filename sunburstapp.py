"""Sunburst in TABs."""
import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

# from sunburst import create_sunburst, get_sunburst
from sunburst import create_sunburst_fig_title


# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = DjangoDash('Sunburst')  # , external_stylesheets=external_stylesheets)
app = dash.Dash(__name__)  # , external_stylesheets=external_stylesheets)

fig_one, title_one = create_sunburst_fig_title('ba')
fig_two, title_two = create_sunburst_fig_title('ma')
# _, fig_one_title = get_sunburst('ba')
# _, fig_two_title = get_sunburst('ma')
fig_one_title = 'a fix set tile for testing'
fig_two_title = 'a fix set tile for testing'

app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label=title_one, value='tab-1'),
        dcc.Tab(label=title_two, value='tab-2'),
    ]),
    html.Div(id='tabs-content'),
], style={'font-family': 'Courier'}
)


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    """Render by start and callback."""
    if tab == 'tab-1':
        return html.Div([

            # html.H3(children='The ' + title_one + ' Studies'),
            dcc.Graph(id='graph_one', figure=fig_one)
        ],
            style={'font-family': 'Helvetica',
                   '#123456': 'red',
                   'marginBottom': 50,
                   'marginTop': 25
                   },
            # className='Sunburst'
            # className='six columns'
        ),
    elif tab == 'tab-2':
        return html.Div([

            # html.H3(children='The ' + title_two + ' Studies'),
            dcc.Graph(id='graph_two', figure=fig_two)
        ], style={'font-family': 'Helvetica',
                  '#123456': 'red',
                  'marginBottom': 50,
                  },
            className='container'  # className='six columns'
        )


if __name__ == '__main__':
    app.run_server(8050, debug=True)
