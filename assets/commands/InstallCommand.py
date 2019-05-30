import os

from cleo import Command
from masonite.packages import create_or_append_config

folder = os.path.dirname(os.path.realpath(__file__))

class InstallCommand(Command):
    """
    Install Masonite Assets

    install:assets
    """

    def handle(self):
        create_or_append_config(
            os.path.join(
                folder,
                '../config/storage.py'
            )
        )
