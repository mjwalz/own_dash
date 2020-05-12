# try:
from projects.food_runner.data.food_runner_data import sunburst as sunburst_food
from projects.food_runner.data.food_runner_data import ranked, checking_ranked
from projects.food_runner.data.food_runner_data import sunburst_info
# from projects.food_runner.data.food_runner_data import get_tabs
# except:
#     raise ImportError
from own_dash.sunburst import create_sunburst_fig
# from own_dash.food_runner import get_figs

ranking = ranked
# print(sunburst_food())
# print(ranking())
print(checking_ranked())




# character, parent, value
sunburst_info = sunburst_info()
# sunburst_info = dict(
#     character=['Kohlenhydrate', 'Fette', 'Proteine', 'Stärke'],
#     parent=['Nahrung']*4,
#     value=[1]*4,
# )
for key, value in sunburst_info.items():
    print(key, value)

print(sunburst_info, 'in food_runner.py')
fig = create_sunburst_fig(sunburst_info)
# tabs = get_tabs()
