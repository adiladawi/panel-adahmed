import holoviews as hv
import panel as pn
import numpy as np
from os import environ, listdir
from os.path import isfile, join


hv.extension('bokeh')
heroku_port = int(environ.get('PORT'))
path = 'apps/'
files = [f for f in listdir(path) if isfile(join(path,f))]
titles = ['Echarts', 'Iris']
APPS = {title:file for title,file in zip(titles,files)}


def sine(frequency, phase, amplitude):
    xs = np.linspace(0, np.pi*4)
    return hv.Curve((xs, np.sin(frequency*xs+phase)*amplitude)).options(width=800)

if __name__ == '__main__':
    # ranges = dict(frequency=(1, 5), phase=(-np.pi, np.pi), amplitude=(-2, 2), y=(-2, 2))
    # dmap = hv.DynamicMap(sine, kdims=['frequency', 'phase', 'amplitude']).redim.range(**ranges)
    pn.serve(APPS, title='duh', port=heroku_port, allow_websocket_origin=["panel-adahmed.herokuapp.com"])
