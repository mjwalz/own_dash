"""Handling data for the f'{name}_app.py'.

Example data or import from local projects with it as a PYTHONPATH.
"""
try:
    from projects.it_structure.data.it_structure_data import sunburst_info
    from projects.it_structure.data.it_structure_data import get_tabs, get_msg
except ImportError:
    from data.it_structure import data
    TABS = [each for each in data.keys()]

    def sunburst_info(tab=''):
        """Was there a default value?."""
        # print(tab)
        # shouldn't be empty in this file !
        return data[tab]

    def get_tabs():
        """Wil be executet if the machine is not the local.

        one with data in projects.
        """
        return TABS

    def get_msg():
        """."""
        return {'IT':
                """
                Diese Sunburstdarstellung überblickt die Themen der Informationstechnik.
                Sie sind nicht in totaler Gänze dargestellt, jedoch gibt es einen
                rahmenden Einblick in relevante Bereiche, welche in jeglichen technischen
                Prozessen ein Thema ist.
                """
                }

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
    - so it will be changed in version control (VC)
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
        holder[tab] = create_sunburst_fig(sunburst_info(tab))
    return holder


# fig = create_sunburst_fig(sunburst_info())

msgs = get_msg()


if __name__ == "__main__":
    print('\n\t', 'THIS IS A DATA FILE AND SHOULD NOT BE RUN AS A MAIN.', '\n\t')
