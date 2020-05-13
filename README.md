# own-dash
own-dash is an extention of dash-plitly

- simple dia / viz / illustration
- same data flow
-

## sunburst:
sunburstapp

sunburst
- `from own_dash.sunburst import create_sunburst_fig  # as workplace beeing in pythonpath !`
 - get data structire as dict: character, parent, value...
- `create_sunburst_fig(sunburstinfo:dict()) -> fig:`
- run python food_runner_app.py it will get the data from food_runner_data and hanldes | passes
    - [ ] local

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

# TODO
- [ ] let somehow a program read the apps in and hanle, give it as a html to the browser
- [ ] and yea. it is with TABS...
# CREATED sunburst_tabs.py
