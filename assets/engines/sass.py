from subprocess import check_call, CalledProcessError
import os

from assets.engines.config import sass_config_file
from assets.engines.messages import (sass_info_compile, sass_info_install, sass_error_compile, sass_error_npm_install, sass_error_npm_missing)

log = os.path.join('.', '.sass.log')
binary = os.path.join('.', 'node_modules', '.bin', 'node-sass')
config = sass_config_file('.')

def sass_compile(in_file, out_folder):
    print(sass_info_compile.format(in_file = in_file))

    if not config:
        try:
            check_call(
                [binary, '--output', out_folder, in_file],
                stdout = open(os.devnull, 'wb'),
                stderr = open(log, 'wb'),
            )
        except CalledProcessError:
            print(sass_error_compile.format(log = log))
    else:
        script = (
            'var fs = require("fs");'
            'var path = require("path");'
            'var sass = require("node-sass");'
            ''
            'var name = path.parse("{in_file}").base;'
            'var out_file = path.join("{out_folder}", name);'
            ''
            'out_file = out_file.substr(0, out_file.lastIndexOf(".")) + ".css";'
            ''
            'var result = sass.renderSync({{ file: "{in_file}", ...require("{config}") }});'
            ''
            'fs.writeFileSync(out_file, result.css);'
        )

        try:
            check_call(
                ['node', '-e', script.format(in_file = in_file, out_folder = out_folder, config = config)],
                stdout = open(os.devnull, 'wb'),
                stderr = open(log, 'wb'),
            )
        except CalledProcessError:
            print(sass_error_compile.format(log = log))

def sass_install():
    print(sass_info_install)

    try:
        check_call(
            ['npm', 'install', '--save-dev', 'node-sass'],
            stdout = open(os.devnull, 'wb'),
            stderr = open(log, 'wb'),
        )
    except CalledProcessError:
        print(sass_error_npm_install)
    except OSError:
        print(sass_error_npm_missing)

if not os.path.isfile(binary):
    sass_install()

if __name__ == '__main__':
    sass_compile(
        os.path.join('.', 'storage', 'static', 'sass', 'app.scss'),
        os.path.join('.', 'storage', 'compiled')
    )
