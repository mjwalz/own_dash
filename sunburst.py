"""The sunburst template."""
import plotly.graph_objects as go
from settings_dash_no_panda import hold_up_ba
from settings_dash_no_panda import hold_up_ma
# from .settings_dash_no_panda import hold_up_ba
# from .settings_dash_no_panda import hold_up_ma
# from owndash.models import Sunburst


def create_sunburst_fig_title(caller):
    """Create the sunburst by sunburst_dict."""
    if caller == 'ba':
        sunburst_info, sunburst_title = hold_up_ba
    elif caller == 'ma':
        sunburst_info, sunburst_title = hold_up_ma

    fig = go.Figure(go.Sunburst(
        labels=sunburst_info['character'],
        parents=sunburst_info['parent'],
        values=sunburst_info['value'],
        branchvalues="total",
        marker=dict(
            colors=sunburst_info['value'],
            colorscale='Cividis',
        )

    ))

    fig.update_layout(
        # autosize=False,
        margin={
            "t": 0,
            "l": 0,
            "r": 0,
            "b": 0,
            "pad": 0,
        },
        showlegend=True,
        height=512,
    )
    return fig, sunburst_title
