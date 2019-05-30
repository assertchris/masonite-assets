from masonite.provider import ServiceProvider
from config import application, storage

import os

from assets.commands.InstallCommand import InstallCommand
from assets.engines.babel import babel_compile
from assets.engines.sass import sass_compile

class AssetsProvider(ServiceProvider):
    wsgi = False

    def register(self):
        self.app.bind('AssetsInstallCommand', InstallCommand())

    def boot(self):
        self.compile_babel()
        self.compile_sass()

    def compile_babel(self):
        matches = self.matches_for_extensions(
            storage.BABELFILES['importFrom'],
            ('.js', '.jsm', '.jsx'),
        )

        for filename in matches:
            babel_compile(
                filename,
                storage.BABELFILES['compileTo'],
            )

    def compile_sass(self):
        matches = self.matches_for_extensions(
            storage.SASSFILES['importFrom'],
            ('.sass', '.scss'),
        )

        for filename in matches:
            sass_compile(
                filename,
                storage.SASSFILES['compileTo'],
            )

    def matches_for_extensions(self, importPaths, extensions):
        matches = []

        for importPath in importPaths:
            for root, _, filenames in os.walk(os.path.join(application.BASE_DIRECTORY, importPath)):
                for filename in filenames:
                    if filename.endswith(extensions) and not filename.startswith('_'):
                        matches.append(os.path.join(root, filename))

        return matches
