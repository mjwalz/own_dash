"""Food runner display.

display a sunburst for healthy food.
"""


from own_dash.food_runner import fig#, sunburst_info_figs
from projects.food_runner.data.food_runner_data import (
                                                        # sunburst_info,
                                                        sunburst_info_tabs,
                                                        sunburst_info_figs,
                                                        get_tabs
                                                        )
#---
from dash.dependencies import Input, Output
#
import dash_core_components as dcc
import dash_html_components as html

import dash
# change it in get_app()
# app = DjangoDash('Sunburst')
app = dash.Dash(__name__)
#---

# the amount of values in tabs will be the amount of tabs
figs = [fig]*4
# get tab list
tabs = get_tabs()



# sunburst_info = sunburst_info()
# # use values for sunburst_info_tabs
# # keys contain the topics
sunburst_info_tabs = sunburst_info_tabs()

sunburst_info_figs = sunburst_info_figs()

# app = sunburst_tabs(tabs, figs)
# app.layout = get_layout(tabs)
def get_layout(topics):
    children = [dcc.Tab(label=each, value='tab-1') for each in topics ]
    return html.Div([
    dcc.Tabs(id='tabs', value='tab-1',
    children=children
    ),
    html.Div(id='tabs-content'),
    ], style={'font-family': 'Courier'}
    )


app.layout = get_layout([key for key in sunburst_info_tabs.keys()])


def get_content_render(fig):
    return html.Div([
            dcc.Graph(id='graph_two', figure=fig)
            ], style={'font-family': 'Helvetica',
            '#123456': 'red',
            'marginBottom': 50,
            },
            className='container'  # className='six columns'
        )
def get_content(fig):
    return get_content_render(fig)

# render_content(app, figs)
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    """Render by start and callback."""
    rander_holder = True
    for index in range(len(sunburst_info_figs)):
        tabbi = f'tab-{i+1}'
        if tab == tabbi:
            return get_content(figs[i])
    # if tab == 'tab-1':
    #     return get_content(figs[0])
    # elif tab == 'tab-2':
    #     return get_content(figs[1])
    # elif tab == 'tab-3':
    #     return get_content(figs[2])
    # elif tab == 'tab-4':
    #     return get_content(figs[3])
    # elif tab == 'tab-5':
    #     return get_content(figs[4])
    # elif tab == 'tab-6':
    #     return get_content(figs[5])
    # elif tab == 'tab-7':
    #     return get_content(figs[6])
    # elif tab == 'tab-8':
    #     return get_content(figs[7])


if __name__ == '__main__':
    app.run_server()
