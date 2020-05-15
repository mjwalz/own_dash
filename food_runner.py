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
        """."""
        return sunburst_info_temlplate

    def get_tabs():
        """Wil be executet if the machine is not the local.

        one with data in projects.
        """
        return TABS
from own_dash.sunburst import create_sunburst_fig
# from own_dash.food_runner import get_figs


def multi_figs():
    """Give the created figs from data for app."""
    holder = dict()
    for tab in get_tabs():
        # print('\n', tab, '\n\t', 'tab in multi_figs()')
        # print(sunburst_info(tab), '\n\t', 'sunburst_info in multi_figs()', '\n')
        holder[tab] = create_sunburst_fig(sunburst_info(tab))
    return holder


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
