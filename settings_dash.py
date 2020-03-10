"""Settings for dash."""
# from jinja2 import Template
# import csv
import pandas as pd
df_ba = pd.read_csv('studies_ba.csv')
df_ma = pd.read_csv('studies_ma.csv')
# df.drop_duplicates()
# df2 = pd.read_csv('studies_ba.csv')
# df = pd.concat([df1, df2], axis=1)
#df = dff[:]
# base_studies = ['Economics', 'Electronics']


# def put_parent_list():
#     """Put the parents list."""
#     holder = ['Studies' for i in range(len(base_studies))]
#     holder.extend(base_studies)
#     return holder


def set_value_by_child(key_parents, df):
    """Set the value of the parent by child."""
    for key in key_parents:
        df.loc[df['character'] == key, 'value'] =\
            df['value'][df['parent'] == key].sum()


def add_list_to_list(list1, list2):
    """Add the string values of two lists."""
    re_list = list1[:]
    [re_list.append(item) for item in list2]
    # print(re_list)
    return re_list


def get_value_list(df):
    """Get the value list which is calculatd from the bottom."""
    # remaining parents
    parent_r = list(set(df.parent))
    # child00 is lowest in tree
    child00 = [item for item in df.character if item not in parent_r]
    child_all = child00
    # get the parents of the lowest - child00
    # child01_p are possible child01 - next key childs
    # need to be checked if keys
    # child of key in parent - child01 of child01_p in parent
    child_p = set(df['parent'].loc[df.character.isin(child_all)])
    while child_p:
        set_value_by_child(child_p, df)
        child_all = add_list_to_list(list(child_p), child_all)
        child_p = set(df.character[df.character.isin(child_all) == False])
    return list(df.value)

# with open('studies.csv', 'r') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')
#     for row in csvreader:
#         print(row)


def get_title(df):
    """Get the title which is a parent but not a child."""
    return (df.parent[df.parent.isin(df.character) == False][0])


# print(df)
settings_sunburst_ma = {
    'title': get_title(df_ma),
    'sunburst_dict': dict(
        parent=list(df_ma.parent),
        character=list(df_ma.character),
        value=get_value_list(df_ma),
        # dff=df
    )
}
settings_sunburst_ba = {
    'title': get_title(df_ba),
    'sunburst_dict': dict(
        parent=list(df_ba.parent),
        character=list(df_ba.character),
        value=get_value_list(df_ba),
        # dff=df
    )
}
# print(len(settings_sunburst['sunburst_dict']['parent']))
# print((settings_sunburst['sunburst_dict']['parent'][0]))
