# from sunburstapp import app
from geoapp import app  # as geoapp
#from sunburstapp import app as sunbusrstapp

if __name__ == '__main__':
    app.run_server(8054, debug=True)
