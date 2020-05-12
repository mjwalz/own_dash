"""
Settings for dash.

- sunburst
    - last childs must have a value
    - second main_parent shouldn't have a value (at least one!)
"""
import csv
# import os

# from owndash.models import Sunburst


def read_csv(filename):
    """Read in a csv without header."""
    holder = list()
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            # print(row)
            row_list = list(map(lambda x: x, row[:-1]))
            # right = list(map(lambda x: x, row[-1:]))
            holder.append(row_list)
    return holder[1:]


def get_cha_par_val(liste_list):
    """Return each list."""
    return (
        [ho[0] for ho in liste_list],
        [ho[1] for ho in liste_list],
        [0.0 if ho[2] == '' else float(ho[2]) for ho in liste_list]
    )


def get_first_main_parent(character, parent,):
    """Get the title which is a parent but not a child - any."""
    for par in parent:
        if par not in character:
            return par


def get_main_childs(parent, character):
    """Get all childs which are not a parent."""
    return [cha if cha not in parent else '' for cha in character]


def add_values_parent_current(parent_current, parent, pos, value):
    """Add values for the current parents."""
    if parent[pos] not in parent_current:
        parent_current[parent[pos]] = value[pos]
    else:
        parent_current[parent[pos]] += value[pos]
    return value


def refill_values_from_bottom(character, parent, value,
                              length,
                              parents_old,
                              first=False
                              ):
    """Get the child, add the values and set the value for the parent."""
    parent_current = {}
    # get the value of childs and add to parents
    for pos in range(length):
        if first:
            if get_main_childs(parent, character)[pos]:
                value = add_values_parent_current(parent_current,
                                                  parent,
                                                  pos,
                                                  value)
        else:
            if parent[pos] not in parents_old:
                value = add_values_parent_current(parent_current,
                                                  parent,
                                                  pos,
                                                  value)
    # set the value for chosen parents
    for pos in range(length):
        if character[pos] in parent_current:
            value[pos] = parent_current[character[pos]]

    return value, parent_current


def value_is_not_filled(values):
    """Check if all values are filled."""
    if 0 in values:
        return True
    else:
        return False


def calculate_sunburst_info(character, parent, value):
    """
    Calculate the rank of parents and character.

    Set the value starting from bottom for parent by child.
    The red csv file is a listed list of [[cha,par,val],...]
    """
    # child_last = get_main_childs(parent, character)

    length = len(character)

    is_first = True
    parent_old = {}
    while value_is_not_filled(value):
        value, parent_old = refill_values_from_bottom(character,
                                                      parent,
                                                      value,
                                                      length,
                                                      parents_old=parent_old,
                                                      first=is_first
                                                      )
        # fill old parents
        for key in parent_old.keys():
            parent_old[key] = parent_old[key]

        is_first = False

    sunburst_title = get_first_main_parent(character, parent)
    return {'value': value,
            'parent': parent,
            'character': character}, sunburst_title


# cwd = os.getcwd()
# data_dir = cwd + '/data/'
# print(data_dir)


def get_cha_par_val_DB(sun, key):
    """Return each list from DB."""
    character = []
    parent = []
    value = []

    for each in sun.objects.filter(key=key).all():
        character.append(each.character)
        parent.append(each.parent)
        value.append(each.value)

    return character, parent, value


""" DB
character, parent, value = get_cha_par_val_DB(Sunburst, 'Bachelor')

hold_up_ba = calculate_sunburst_info(character, parent, value)

character, parent, value = get_cha_par_val_DB(Sunburst, 'Master')
hold_up_ma = calculate_sunburst_info(character, parent, value)
"""

"""
absFilePath = os.path.abspath(__file__)
basFilePath = os.path.basename(__file__)
dirFilePath = os.path.dirname(__file__)
print(dirFilePath)
fix_path_to_data = '../data'
comFilePath = os.path.commonprefix([fix_path_to_data, absFilePath])
print(comFilePath)
file_name_bachelor = os.path.join(dirFilePath, 'data', 'studies_ba.csv')
print(file_name_bachelor)
file_name_master = os.path.join(dirFilePath, 'data', 'studies_ma.csv')
# #should already be the BASE_DIR(!)  # get_cha_par_val()
# file_name_bachelor = os.path.join(os.getcwd(), 'xdata', 'studies_ba.csv')
# file_name_master = os.path.join(os.getcwd(), 'data', 'studies_ma.csv')
file_bachelor = read_csv(file_name_bachelor)
file_master = read_csv(file_name_master)

# file_bachelor = read_csv(data_dir+'studies_ba.csv')
# file_master = read_csv(data_dir+'studies_ma.csv')
"""

"""The following is a fixed input for the profile example."""
file_bachelor = [
    ['Electrical Engineering / Information Technology',
     'Bachelor of Science',
     ''],
    ['Economic Sciences', 'Bachelor of Science', ''],
    ['Thesis', 'Bachelor of Science', ''],
    ["Bachelor's", 'Thesis', ''],
    ['Professionalisation - Integration Subjects', 'Bachelor of Science', ''],
    ['Fundamentals Eco.', 'Economic Sciences', ''],
    ['Economics - Specialisation', 'Economic Sciences', ''],
    ['Fundamentals El.', 'Electrical Engineering / Information Technology', ''],
    ['Electrotechnical - Specialization',
        'Electrical Engineering / Information Technology',
        ''],
    ['Fundamentals of Mathematics and Natural Science',
        'Bachelor of Science',
        ''],
    ['Mathematics I', 'Fundamentals of Mathematics and Natural Science', '12'],
    ['Mathematics II', 'Fundamentals of Mathematics and Natural Science', '12'],
    ['Mechanics and Thermics for Electrical Engineering',
        'Fundamentals of Mathematics and Natural Science',
        '6'],
    ['Fundamentals of Economics', 'Fundamentals Eco.', '8'],
    ['Accounting', 'Fundamentals Eco.', '5'],
    ['Fundamentals of Business Studies', 'Fundamentals Eco.', '10'],
    ['Electrical Engineereing', 'Fundamentals El.', '9'],
    ['Controll Engineereing', 'Fundamentals El.', '5'],
    ['Electrics', 'Fundamentals El.', '5'],
    ['Digital Systems Design', 'Fundamentals El.', '7'],
    ['Electromagnetic Fields I', 'Fundamentals El.', '5'],
    ['Basic Linear Circuit Theory', 'Fundamentals El.', '13'],
    ['Energy Technology Basics', 'Fundamentals El.', '5'],
    ['Informations Technology', 'Fundamentals El.', '6'],
    ['Focus Economics', 'Economics - Specialisation', '5'],
    ['Focus Finance', 'Economics - Specialisation', '5'],
    ['Focus Production and Logistics', 'Economics - Specialisation', '5'],
    ['Focus Marketing', 'Economics - Specialisation', '5'],
    ['Digital Circuit Design', 'Electrotechnical - Specialization', '5'],
    ['Industrial Internship', 'Bachelor of Science', ''],
    ['BioMedical Instruments', 'Industrial Internship', '8'],
    ['Civil Law', 'Professionalisation - Integration Subjects', '8'],
    ['Quantitative Methods in Economic Science',
        'Professionalisation - Integration Subjects',
        '8'],
    ['Professionalisation', 'Professionalisation - Integration Subjects', '7'],
    ['Algorithms and Skills', 'Professionalisation - Integration Subjects', '5'],
    ['Camera-based detection and classification of traffic signs',
        "Bachelor's",
        '12']
]
file_master = [
    ['Electrical Engineering / Information Technology', 'Master of Science', ''],
    ['Economic Sciences', 'Master of Science', ''],
    ['Lboratory Courses', 'Master of Science', '11'],
    ['Industrial Internship', 'Master of Science', '12'],
    ['Thesis', 'Master of Science', '30'],
    ["Master's", 'Thesis', '30'],
    ['Specialisation Eco.', 'Economic Sciences', '33'],
    ['Elective Area', 'Electrical Engineering / Information Technology', '11'],
    ['Specialisation: Mechatronics and Metrology',
        'Electrical Engineering / Information Technology',
        '20'],
    ['Brain Computer Interface for head mounted display', "Master's", '30'],
    ['Marketing (Major)', 'Specialisation Eco.', '14'],
    ['Economics (Major)', 'Specialisation Eco.', '14'],
    ['Production and Logistics (Minor)', 'Specialisation Eco.', '5'],
    ['Facility Management', 'Production and Logistics (Minor)', '2.5'],
    ['Energy- and resource-efficient Production',
        'Production and Logistics (Minor)',
        '2.5'],
    ['Insurance Economics', 'Economics (Major)', '5'],
    ['Theory and Politics of Taxation', 'Economics (Major)', '5'],
    ['Slows income inequality economic growth', 'Economics (Major)', '4'],
    ['Consumer Bahavior', 'Marketing (Major)', '5'],
    ['Marketing Research', 'Marketing (Major)', '2.5'],
    ['International Marketing', 'Marketing (Major)', '2.5'],
    ['Acceptance of QR-code-ased feedback solution', 'Marketing (Major)', '4'],
    ['Robotics I - Technical and Mathematical Basics',
        'Specialisation: Mechatronics and Metrology',
        '5'],
    ['Robotics II - Programming Modelling Planning',
        'Specialisation: Mechatronics and Metrology',
        '5'],
    ['Precision Measuring Techniques',
        'Specialisation: Mechatronics and Metrology',
        '5'],
    ['Nanoelectronics', 'Specialisation: Mechatronics and Metrology', '5'],
    ['Basics of Medicine for Engineers', 'Elective Area', '5'],
    ['Bioanalysis', 'Elective Area', '6'],
    ['Electrical Machine', 'Lboratory Courses', '5'],
    ['Power Electronics', 'Lboratory Courses', '5'],
    ['Robotics', 'Lboratory Courses', '6'],
    ['add solution', 'Industrial Internship', '12']
]
""""""

character, parent, value = get_cha_par_val(file_bachelor)
hold_up_ba = calculate_sunburst_info(character, parent, value)

character, parent, value = get_cha_par_val(file_master)

hold_up_ma = calculate_sunburst_info(character, parent, value)


"""python
from owndash.models import Sunburst
from owndash.dash_apps.sunburst.settings_dash import *
cha, par, val = get_cha_par_val(file_bachelor)
for (c,p),v in zip(zip(cha,par),val):
    sun = Sunburst(character=c, parent=p, value=v,key='Bachelor')
    sun.save()
"""
