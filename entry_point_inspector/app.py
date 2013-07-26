import logging
import sys

from cliff import app
from cliff import commandmanager

import pkg_resources


class EntryPointInspector(app.App):

    log = logging.getLogger(__name__)

    def __init__(self):
        dist = pkg_resources.get_distribution('entry_point_inspector')
        super(EntryPointInspector, self).__init__(
            description='Tool for looking at the entry points on a system',
            version=dist.version,
            command_manager=commandmanager.CommandManager('epi.commands'),
        )


def main(argv=sys.argv[1:]):
    return EntryPointInspector().run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
