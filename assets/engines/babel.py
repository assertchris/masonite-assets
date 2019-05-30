from subprocess import check_call, CalledProcessError
from config import application
import os

from assets.engines.config import babel_config_file
from assets.engines.messages import (babel_info_compile, babel_info_install, babel_error_compile, babel_error_npm_install, babel_error_npm_missing)

log = os.path.join(application.BASE_DIRECTORY, '.babel.log')
binary = os.path.join(application.BASE_DIRECTORY, 'node_modules', '.bin', 'babel')
config = babel_config_file(application.BASE_DIRECTORY)

def babel_compile(in_file, out_folder):
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

def babel_install():
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
    babel_install()
