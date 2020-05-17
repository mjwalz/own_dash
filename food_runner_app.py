"""Food runner display.

display a sunburst for healthy food.
"""
try:
    from own_dash.food_runner import (
        # fig,
        multi_figs  # , sunburst_info_fig
    )
except ImportError:
    from food_runner import (
        # fig,
        multi_figs  # , sunburst_info_fig
    )

    import os
    print(os.getcwd())

    # from os import getcwd, path
    # import sys
    #
    # print(getcwd())
    # path_holder = path.join(getcwd(), '..')
    # print(path_holder)
    # sys.path(path_holder)
# finally:
#     from own_dash.food_runner import (
#         # fig,
#         multi_figs  # , sunburst_info_fig
#     )


from own_dash.food_runner import (
        fig,  # is used but not needed...
        multi_figs  # will read in multi figures with sunburst_info_figs
    )
from projects.food_runner.data.food_runner_data import (
        sunburst_info_figs,  # returns a fig
        get_tabs
    )

#---
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

# append(getcwd())

# from projects.food_runner.data.food_runner_data import (
#     # sunburst_info,
#     # sunburst_info_tabs,
#     sunburst_info_figs,
#     get_tabs
# )

# ---
#

# change it in get_app()
# app = DjangoDash('Sunburst')
app = dash.Dash(__name__)
# ---

# the amount of values in tabs will be the amount of tabs
# figs = [fig]*4
# get tab list
# tabs = get_tabs()

figs = multi_figs()

[print(each) for each in figs.items()]

# the keys are the TABS
key_list = [key for key in figs.keys()]


def get_layout(topics):
    """Give a Topic a Tab and an Index."""
    children = [dcc.Tab(label=tab,
                        value=f'tab-{i+1}') for i, tab in enumerate(topics)]

    return html.Div([
        dcc.Tabs(id='tabs', value='tab-1',
                 children=children
                 ),
        html.Div(id='tabs-content'),
    ], style={'font-family': 'Courier'}
    )

# here we create the tabs by keys
app.layout = get_layout([key for key in figs.keys()])

graph_nr = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']



def get_content_render(fig, index):
    """Give an indexed a graph_nr [1,8] and a fig."""
    return html.Div([
        dcc.Graph(id=f'graph_{graph_nr[index]}', figure=fig)
    ], style={'font-family': 'Helvetica',
              '#123456': 'red',
              'marginBottom': 50,
              },
        className='container'  # className='six columns'
    )
# get different figs


def get_content(topic, index):
    """Get the content to be randered as figs and topics in the app."""
    return get_content_render(figs[topic], index)


# render_content(app, figs)
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    """Render by start and callback."""
    # rander_holder = True
    for index in range(len(figs)):
        """Render by start and callback."""
        tabbi = f'tab-{index+1}'
        print(tabbi, 'in tabbi')
        if tab == tabbi:
            return get_content(key_list[index], index)


if __name__ == '__main__':
    app.run_server()
