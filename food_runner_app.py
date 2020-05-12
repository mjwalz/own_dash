"""Food runner display.

display a sunburst for healthy food.
"""

import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

from own_dash.food_runner import fig as fig

fig_one = fig
title_one = 'Nahrung'
# app = DjangoDash('Sunburst')  # , external_stylesheets=external_stylesheets)
app = dash.Dash(__name__)  # , external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label=title_one, value='tab-1'),
        # dcc.Tab(label=title_two, value='tab-2'),
    ]),
    html.Div(id='tabs-content'),
], style={'font-family': 'Courier'}
)


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    """Render by start and callback."""

    # return html.Div([
    #
    #     # html.H3(children='The ' + title_two + ' Studies'),
    #     dcc.Graph(id='graph', figure=fig)
    # ], style={'font-family': 'Helvetica',
    #           '#123456': 'red',
    #           'marginBottom': 50,
    #           },
    #     className='container'  # className='six columns'
    # )
    # # if tab == 'tab-1':
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
    #  # ---
    # elif tab == 'tab-2':
    #     return html.Div([
    #
    #         # html.H3(children='The ' + title_two + ' Studies'),
    #         dcc.Graph(id='graph_two', figure=fig_two)
    #     ], style={'font-family': 'Helvetica',
    #               '#123456': 'red',
    #               'marginBottom': 50,
    #               },
    #         className='container'  # className='six columns'
    #     )



if __name__ == '__main__':
    app.run_server()
