# own-dash
own-dash is an extension of dash-plotly

- simple dia / viz / illustration
- same data flow

## it_structure_app()
- doesn't have to be updated anymore
- [ ] change the import name form `data.py` to something and maybe change the way it updates files by name or something
    - [ ] change also PATH in projects food_runner

## food_runner_app()

<!-- ### test it with food_runner_app.py -->
## dont forget to `pip install -r requirements.txt`in a `source .venv/bin/activate` a.k.a `virtualenv .venv` oder `python3 -m venv .venv`


## sunburst:
sunburstapp

sunburst
- `from own_dash.sunburst import create_sunburst_fig  # as workplace beeing in pythonpath !`
 - get data structire as dict: character, parent, value...
- `create_sunburst_fig(sunburstinfo:dict()) -> fig:`
- run python food_runner_app.py it will get the data from food_runner_data and hanldes | passes
    - [ ] locale

- wants a structure as:
`update_dict(sunburst_info_dict, update)`
- get the correct file structure and put it into the app - append it to end
  - data must be handled correctly before
  - check food_runner_data.py in projects
  - food_runner.py create app and food_runner_app.py can be runned in terminal as a python shell command `python food_runner_app.py`

```python
dict(
  parent=[]
  character=[]
  value=[]
)
```

## Data Handling
\*\_app.py will get data from \*\_data.py and fig info from \*.py
and will display it as known.

# simple rick


# CREATED
```python
f'{name}'.py  # infrastructure for the following files
f'{name}_data'.py  # prepare the data so it fits in the app structure
f'{name}_app'.py  # run visual app with it
```
### test it with `python it_structure_app.py`
of course after you `source`d the `.venv/bin/activate` in which you will
`pip install -r requirements.txt`.

# TODO
- [X] let somehow a program read the apps in and hanDle, give it as a html to the browser
- more or less...
- [x] and yea. it is with TABS...
- [ ] prepare an easy django read in :-1:
---

- [ ] ah yea. the data hdanling is still local :+1:
- [ ] maybe put some apps with two files in each folder... I just mean äh. many files though

# CREATED
{name}.py  # infrastructure for the following files
{name}_data.py  # prepare the data so it fits in the app structure
{name}_app.py  # run visual app with it

# update
here are where project can not be read in it has to get an update and take default example data



# DATA .
looks like it wasn't correctly on `.gitignore` - so data was commited on misfortune
- is now included again
- [ ] don't upload trash again !


# danger - it is back on
danger_data_danger.py is showing a nice way to design a data file in
`dirname(\__file__).endwith('data')``


# Textarea will be awesome for using a input with `-` for the tree
- [1,8]
    - [1,8][1,8]
        - [1,8][1,8][1,8]
            - [1,8][1,8][1,8][1,8]
                - [1,8][1,8][1,8][1,8][1,8]
                    - [1,8][1,8][1,8][1,8][1,8][1,8]
                        - [1,8][1,8][1,8][1,8][1,8][1,8][1,8]
                            - [1,8][1,8][1,8][1,8][1,8][1,8][1,8][1,8]
- it is solved with `depth`for now. should be changed in a nice flask app form
- Topic
    - Topic1
        - Topic11
        - Topic12
    - Topic2

# totaly needs an overwork for the terminal output
# the character and parents are not allowed to be same named
