import logging

from cliff import lister

import pkg_resources

LOG = logging.getLogger(__name__)


class GroupList(lister.Lister):
    """Shows the groups for which plugins are available.
    """

    def take_action(self, parsed_args):
        names = set()
        for dist in pkg_resources.working_set:
            LOG.debug('checking distribution "%s"', dist)
            entry_map = pkg_resources.get_entry_map(dist)
            names.update(set(entry_map.keys()))
        return (
            ('Name',),
            ((n,) for n in sorted(names)),
        )


class GroupShow(lister.Lister):
    """Shows the members of a specific group.
    """

    def get_parser(self, prog_name):
        p = super(GroupShow, self).get_parser(prog_name)
        p.add_argument(
            'group',
            help='the name of the group to show',
        )
        return p

    def take_action(self, parsed_args):
        results = []
        for ep in pkg_resources.iter_entry_points(parsed_args.group):
            try:
                ep.load()
            except Exception as err:
                load_error = str(err)  # unicode?
            else:
                load_error = ''
            attr = '.'.join(ep.attrs)
            results.append((
                ep.name,
                ep.module_name,
                attr,
                str(ep.dist),  # unicode?
                load_error,
            ))
        return (
            ('Name', 'Module', 'Member', 'Distribution', 'Error'),
            results,
        )
