"""The sunburst template."""
import plotly.express as px
# import plotly.graph_objects as go
from settings_dash import settings_sunburst_ma

sunburst_dict = settings_sunburst_ma['sunburst_dict']
title = settings_sunburst_ma['title']

# fig = px.sunburst(
#     sunburst_dict['dff'],
#     path=['parent', 'character'],
#     values='value',
# )
fig = px.sunburst(
    sunburst_dict,
    parents='parent',
    title=title,
    names='character',
    values='value',
    branchvalues="total",
    color='value',
    color_continuous_scale='Cividis',
    # color_continuous_scale='gray',
    # maxdepth=3,
)
# fig = go.Figure(go.Sunburst(
#     labels=sunburst_dict['character'],
#     parents=sunburst_dict['parent'],
#     values=sunburst_dict['value'],
#     branchvalues="total",
# ))
# fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))
# fig.update_layout(uniformtext_minsize=14, uniformtext_mode='hide')

fig.show()

# ---------------------------------------------------------------------
# This looks nice:
# ---------------------------------------------------------------------
# https://plot.ly/python/plotly-express/
# import plotly.express as px
# df = px.data.iris()
# fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="rug", marginal_x="histogram")
# fig
