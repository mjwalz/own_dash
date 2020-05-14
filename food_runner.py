# try:
# from projects.food_runner.data.food_runner_data import sunburst as sunburst_food
# from projects.food_runner.data.food_runner_data import ranked, checking_ranked
from projects.food_runner.data.food_runner_data import sunburst_info
# from projects.food_runner.data.food_runner_data import sunburst_info_tabs
from projects.food_runner.data.food_runner_data import get_tabs
# except:
#     raise ImportError
from own_dash.sunburst import create_sunburst_fig
# from own_dash.food_runner import get_figs


"""
For Jankins, Travsi or any other data tester:
We need to provide data -
like from `food_runner_data.py` is coming,
but data is local so we need to provide a default
which will be updated
    - update_dict
    - so it will be changed in version controlle (VC)
    - but not all the data hangling functions -

From projects/{{ name }}/data we will just get the result for an Visualization
 We don't want to waste space for data handling and also not in the resources.
 Maybe check Lambda Functions
 and yea test will be done on the data site
 Maybe an import test of the default data


 For sunburst we need a typical data structure: check it in the `README.md`
"""


def multi_figs():
    """Give the created figs from data for app.

    Max amount of the plotted graphs:
        For BackEnd hangling (Flask, Django, Dash, Plotly)
        Max: 8 - or eight in written, if you prevare to like to read more...

        graph_nr = [
                    'one',
                    'two',
                    'three',
                    'four',
                    'five',
                    'six',
                    'seven',
                    'eight'
                    ]
    """
    holder = dict()
    for tab in get_tabs():
        # print('\n', tab, '\n\t', 'tab in multi_figs()')
        # print(sunburst_info(tab), '\n\t', 'sunburst_info in multi_figs()', '\n')
        holder[tab] = create_sunburst_fig(sunburst_info(tab))
    return holder


fig = create_sunburst_fig(sunburst_info())
