import logging
import sys
import traceback

from cliff import show

from importlib.metadata import distributions, entry_points

LOG = logging.getLogger(__name__)


class EntryPointShow(show.ShowOne):
    """Shows the details for a single entry point."""

    def get_parser(self, prog_name):
        p = super(EntryPointShow, self).get_parser(prog_name)
        p.add_argument(
            "group",
            help="the name of the group to show",
        )
        p.add_argument(
            "name",
            help="the name of the entry point to show",
        )
        p.add_argument(
            "--distribution",
            default=None,
            help="the name of the distribution if name is not unique",
        )
        return p

    def take_action(self, parsed_args):
        if parsed_args.distribution:
            LOG.debug(
                "Loading %s from %s using distribution %s",
                parsed_args.name,
                parsed_args.group,
                parsed_args.distribution,
            )
            # Find the specific distribution and entry point
            ep = None
            for dist in distributions():
                if dist.metadata["Name"] == parsed_args.distribution:
                    for entry_point in dist.entry_points:
                        if (
                            entry_point.group == parsed_args.group
                            and entry_point.name == parsed_args.name
                        ):
                            ep = entry_point
                            break
                    if ep:
                        break
            if not ep:
                raise ValueError(
                    "Could not find %r in %r from distribution %r"
                    % (parsed_args.name, parsed_args.group, parsed_args.distribution)
                )
        else:
            LOG.debug(
                "Looking for %s in group %s",
                parsed_args.name,
                parsed_args.group,
            )
            eps = entry_points(group=parsed_args.group, name=parsed_args.name)
            try:
                ep = next(iter(eps))
            except StopIteration:
                raise ValueError(
                    "Could not find %r in %r"
                    % (
                        parsed_args.name,
                        parsed_args.group,
                    )
                )
        try:
            ep.load()
        except Exception:
            tb = traceback.format_exception(*sys.exc_info())
        else:
            tb = ""

        # Parse module.attr format
        if "." in ep.value:
            module_name, _, attr = ep.value.rpartition(".")
        else:
            module_name = ep.value
            attr = ""

        dist_name = ep.dist.metadata["Name"] if ep.dist else "unknown"
        dist_location = getattr(ep.dist, "_path", "unknown") if ep.dist else "unknown"

        return (
            ("Module", "Member", "Distribution", "Path", "Error"),
            (module_name, attr, dist_name, str(dist_location), tb),
        )
