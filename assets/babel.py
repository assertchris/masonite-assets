from subprocess import check_call, CalledProcessError
import os

from _config import babel_config_file
from _messages import (babel_info_compile, babel_info_install, babel_error_compile, babel_error_npm_install, babel_error_npm_missing)

log = os.path.join('.', '.babel.log')
binary = os.path.join('.', 'node_modules', '.bin', 'babel')
config = babel_config_file('.')

def compile(in_file, out_folder):
    print(babel_info_compile.format(in_file = in_file))

    if not config:
        try:
            check_call(
                [binary, '--out-dir', out_folder, in_file],
                stdout = open(os.devnull, 'wb'),
                stderr = open(log, 'wb'),
            )
        except CalledProcessError:
            print(babel_error_compile.format(log = log))
    else:
        try:
            check_call(
                [binary, '--out-dir', out_folder, '--config-file', config, in_file],
                stdout = open(os.devnull, 'wb'),
                stderr = open(log, 'wb'),
            )
        except CalledProcessError:
            print(babel_error_compile.format(log = log))

def install():
    print(babel_info_install)

    try:
        check_call(
            ['npm', 'install', '--save-dev', '@babel/core', '@babel/cli'],
            stdout = open(os.devnull, 'wb'),
            stderr = open(log, 'wb'),
        )
    except CalledProcessError:
        print(babel_error_npm_install)
    except OSError:
        print(babel_error_npm_missing)

if not os.path.isfile(binary):
    install()

# DEBUG
compile(os.path.join('.', 'storage', 'static', 'js', 'app.js'), os.path.join('.', 'storage', 'compiled'))
