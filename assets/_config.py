import os

def babel_config_file(base_path):
    config_js = os.path.join(base_path, '.babelrc.js')

    if os.path.isfile(config_js):
        return config_js

    config_json = os.path.join(base_path, '.babelrc.json')

    if os.path.isfile(config_json):
        return config_json

    config_bare = os.path.join(base_path, '.babelrc')

    if os.path.isfile(config_bare):
        return config_bare

def sass_config_file(base_path):
    config_js = os.path.join(base_path, '.sassrc.js')

    if os.path.isfile(config_js):
        return config_js

    config_bare = os.path.join(base_path, '.sassrc')

    if os.path.isfile(config_bare):
        return config_bare
