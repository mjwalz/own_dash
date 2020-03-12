"""The sunburst template."""
# import plotly.express as px
import plotly.graph_objects as go
from settings_dash import settings_sunburst_ba
from settings_dash import settings_sunburst_ma
from settings_dash import settings_sunburst_both


def get_sunburst(name):
    """Get the wanted fig."""
    if name == 'ba':
        sunburst_dict = settings_sunburst_ba['sunburst_dict']
        title = settings_sunburst_ba['title']
    elif name == 'ma':
        sunburst_dict = settings_sunburst_ma['sunburst_dict']
        title = settings_sunburst_ma['title']
    elif name == 'both':
        sunburst_dict = settings_sunburst_both['sunburst_dict']
        title = settings_sunburst_both['title']

    return sunburst_dict, title


def create_sunburst(sunburst_info):
    """Create the sunburst by sunburst_dict."""
# fig = px.sunburst(
#     sunburst_dict['dff'],
#     path=['parent', 'character'],
#     values='value',
# )
    # return px.sunburst(
    #     sunburst_info[0],
    #     parents='parent',
    #     # title=sunburst_info[1],
    #     names='character',
    #     values='value',
    #     branchvalues="total",
    #     color='value',
    #     color_continuous_scale='Cividis',
    #     # color_continuous_scale='gray',
    #     # maxdepth=3,
    # )
    # # return fig
    sunburst_dict, _ = sunburst_info
    fig = go.Figure(go.Sunburst(
        labels=sunburst_dict['character'],
        parents=sunburst_dict['parent'],
        values=sunburst_dict['value'],
        branchvalues="total",
    ))
    return fig
# fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))
# fig.update_layout(uniformtext_minsize=14, uniformtext_mode='hide')


if __name__ == "__main__":
    """Show M.Sc. if called main as an example."""
    # create_sunburst(get_sunburst('ba')).show()
    # create_sunburst(get_sunburst('ma')).show()
    create_sunburst(get_sunburst('both')).show()

# ---------------------------------------------------------------------
# This looks nice:
# ---------------------------------------------------------------------
# https://plot.ly/python/plotly-express/
# import plotly.express as px
# df = px.data.iris()
# fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="rug", marginal_x="histogram")
# fig
