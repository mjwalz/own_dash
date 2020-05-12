
from projects.food_runner.data.food_runner_data import sunburst as sunburst_food
from projects.food_runner.data.food_runner_data import ranked, checking_ranked
from projects.food_runner.data.food_runner_data import sunburst_info

from own_dash.sunburst import create_sunburst_fig

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

fig = create_sunburst_fig(sunburst_info)
