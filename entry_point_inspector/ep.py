import logging
import sys
import traceback

from cliff import show

import pkg_resources

LOG = logging.getLogger(__name__)


class EntryPointShow(show.ShowOne):
    """Shows the details for a single entry point.
    """

    def get_parser(self, prog_name):
        p = super(EntryPointShow, self).get_parser(prog_name)
        p.add_argument(
            'group',
            help='the name of the group to show',
        )
        p.add_argument(
            'name',
            help='the name of the entry point to show',
        )
        p.add_argument(
            '--distribution',
            default=None,
            help='the name of the distribution if name is not unique',
        )
        return p

    def take_action(self, parsed_args):
        if parsed_args.distribution:
            LOG.debug(
                'Loading %s from %s using distribution %s',
                parsed_args.name,
                parsed_args.group,
                parsed_args.distribution,
            )
            dist = pkg_resources.get_distribution(parsed_args.distribution)
            ep = pkg_resources.get_entry_info(
                dist,
                parsed_args.group,
                parsed_args.name,
            )
        else:
            LOG.debug(
                'Looking for %s in group %s',
                parsed_args.name,
                parsed_args.group,
            )
            try:
                ep = next(pkg_resources.iter_entry_points(
                    parsed_args.group,
                    parsed_args.name,
                ))
            except StopIteration:
                raise ValueError('Could not find %r in %r' % (
                    parsed_args.name,
                    parsed_args.group,
                ))
        try:
            ep.load()
        except Exception:
            tb = traceback.format_exception(*sys.exc_info())
        else:
            tb = ''
        return (
            ('Module', 'Member', 'Distribution', 'Path', 'Error'),
            (ep.module_name,
             '.'.join(ep.attrs),
             str(ep.dist),
             ep.dist.location,
             tb),
        )
