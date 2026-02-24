import logging
import sys

from cliff import app
from cliff import commandmanager

from importlib.metadata import version


class EntryPointInspector(app.App):
    log = logging.getLogger(__name__)

    def __init__(self):
        super(EntryPointInspector, self).__init__(
            description="Tool for looking at the entry points on a system",
            version=version("entry_point_inspector"),
            command_manager=commandmanager.CommandManager("epi.commands"),
        )


def main(argv=sys.argv[1:]):
    return EntryPointInspector().run(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
