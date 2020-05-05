import plotly.express as px

import plotly.graph_objects as go
import numpy as np
np.random.seed(42)

import dash
import dash_core_components as dcc
import dash_html_components as html



def extra(df):
    df.head()
    col_name = ['Xx','Yy','Zz']
    for index, each in zip(col_name, df.columns):
        df[index]=df[each]

    df['species']=0
    df['Xx']=0.0
    df['Yy']=0.5
    df['Zy'] = 1.0
    print(df)


#df = px.data.iris()
#extra(df)
def get_color(max_length:int, diagonal_len):
    if diagonal_len:
        max_length -= diagonal_len
        output = [i for i in range(diagonal_len)]
    else:
        output = []
    more_color = [4]*max_length
    [output.append(more) for more in more_color]
    return output

def get_plate(output_x, output_y, output_z, diagonal_len):
    [output_x.append(each) for each in [2,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4,4,6,6,6,6,6,6,6,6,6,8,8,8,8,8,8,8,8,8]]
    [output_y.append(each) for each in [9,8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8,9]]
    [output_z.append(4) for each in range(diagonal_len+10+18)]
    print(output_x, output_y, output_z)
    return output_x, output_y, output_z

def get_points():
    return {'x':[2,2,8,8,2,2,8,8],'y':[2,8,2,8,2,8,2,8],'z':[2,2,2,2,8,8,8,8],'c':[1,1,1,1,1,1,1,1]}

def get_dict(diagonal:bool=False):
    n=42
    if diagonal:
        output_x = [0,1,2,4,6,7,8,9]
        output_y = [0,1,2,4,6,7,8,9]
        output_z = [0,1,2,4,6,7,8,9]
        diagonal_len = len(output_x)

    print(len(output_x),len(output_y),len(output_z),len(get_color(len(output_x),diagonal_len)))

    output_x, output_y, output_z = get_plate(
        output_x, output_y, output_z,
        diagonal_len,
        )
    #print(len(output_x), len(get_color(len(output_x),diagonal)))
    #for x in output_x:
#        print(x)
    print(len(output_x),len(output_y),len(output_z),len(get_color(len(output_x),diagonal_len)))
    color = get_color(len(output_x),diagonal_len)
    print(output_x)
    for value in get_points()['x']:
        print(value)
        output_x.append(value)
    for value in get_points()['y']:
        output_y.append(value)
    for value in get_points()['z']:
        output_z.append(value)
    for value in get_points()['c']:
        color.append(value)

    output = dict(
            Xx=output_x,
            Yy=output_y,
            Zz=output_z,
            color=color,
    )

    return output

df = get_dict(diagonal=True)

# N = 70
#
# fig2 = go.Figure(data=[go.Mesh3d(x=(70*np.random.randn(N)),
#                    y=(55*np.random.randn(N)),
#                    z=(40*np.random.randn(N)),
#                    opacity=0.5,
#                    color='rgba(244,22,100,0.6)'
#                   )])
# fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
fig = px.scatter_3d(df, x='Xx', y='Yy', z='Zz',
              color='color')

# fig.show()
app = dash.Dash()
app.layout = html.Div([
    html.Div([
        dcc.Graph(figure=fig)
        ]),
    # html.Div([
    #     dcc.Graph(figure=fig2)
    #     ]),
    ])
app.run_server(debug=True)
