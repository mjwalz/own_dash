"""Handling data for the f'{name}_app.py'.

Example data or import from local projects with it as a PYTHONPATH.
"""
try:
    # from projects.food_runner.data.food_runner_data import sunburst as sunburst_food
    # from projects.food_runner.data.food_runner_data import ranked, checking_ranked
    from projects.food_runner.data.food_runner_data import sunburst_info
    # from projects.food_runner.data.food_runner_data import sunburst_info_tabs
    from projects.food_runner.data.food_runner_data import get_tabs
# this area will be updated !
except ImportError:
    """
    TODO: return the right data example in the update

    - how is the structure of
        - sunburst_info_temlplate
        - sunburst_info()
        - with tab and so on
    """
    # those will be updated
    sunburst_info_temlplate = ''

    TABS = ['WabiSabi', 'Nahrung', '']

    def sunburst_info(tab):
        """was there a default value?"""
        return sunburst_info_temlplate

    def get_tabs():
        """Wil be executet if the machine is not the local.

        one with data in projects.
        """
        return TABS
try:
    from own_dash.sunburst import create_sunburst_fig
except ModuleNotFoundError:
    from sunburst import create_sunburst_fig
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


<<<<<<< HEAD
fig = create_sunburst_fig(sunburst_info())
=======
# character, parent, value
sunburst_info_f = sunburst_info()
# sunburst_info = dict(
#     character=['Kohlenhydrate', 'Fette', 'Proteine', 'Stärke'],
#     parent=['Nahrung']*4,
#     value=[1]*4,
# )
# for key, value in sunburst_info.items():
#     print(key, value)

# print(sunburst_info, 'in food_runner.py')
fig = create_sunburst_fig(sunburst_info_f)
# tabs = get_tabs()
>>>>>>> 4bea4bf2321c23fb4696a328ebe8a81811e8b24f
