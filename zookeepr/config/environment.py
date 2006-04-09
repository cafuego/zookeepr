import sys, os

import pylons.config

from zookeepr.config.routing import make_map

def load_environment():
    map = make_map()
    # Setup our paths
    paths = {}
    paths['root_path'] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    paths['controllers'] = paths['root_path'] + '/controllers'
    paths['templates'] = [paths['root_path'] + '/templates', paths['root_path'] + '/components']
    paths['static_files'] = paths['root_path'] + '/public'
    [sys.path.append(paths['root_path'] + path) for path in [paths['controllers'], '/lib']]


    # The following options are passed directly into Myghty, so all configuration options
    # available to the Myghty handler are available for your use here
    myghty = {}
    myghty['log_errors'] = True

    # Add your own Myghty config options here, note that all config options will override
    # any Pylons config options
    
    # Return our loaded config object
    return pylons.config.Config(myghty, map, paths)
