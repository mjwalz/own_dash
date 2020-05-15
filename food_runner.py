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
