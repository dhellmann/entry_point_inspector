import logging

from cliff import lister

from importlib.metadata import distributions, entry_points

LOG = logging.getLogger(__name__)


class GroupList(lister.Lister):
    """Shows the groups for which plugins are available."""

    def take_action(self, parsed_args):
        names = set()
        for dist in distributions():
            LOG.debug('checking distribution "%s"', dist.metadata["Name"])
            if dist.entry_points:
                for ep in dist.entry_points:
                    names.add(ep.group)
        return (
            ("Name",),
            ((n,) for n in sorted(names)),
        )


class GroupShow(lister.Lister):
    """Shows the members of a specific group."""

    def get_parser(self, prog_name):
        p = super(GroupShow, self).get_parser(prog_name)
        p.add_argument(
            "group",
            help="the name of the group to show",
        )
        return p

    def take_action(self, parsed_args):
        results = []
        eps = entry_points(group=parsed_args.group)
        for ep in eps:
            try:
                ep.load()
            except Exception as err:
                load_error = str(err)  # unicode?
            else:
                load_error = ""
            # Parse module.attr format
            if "." in ep.value:
                module_name, _, attr = ep.value.rpartition(".")
            else:
                module_name = ep.value
                attr = ""
            results.append(
                (
                    ep.name,
                    module_name,
                    attr,
                    ep.dist.metadata["Name"] if ep.dist else "unknown",
                    load_error,
                )
            )
        return (
            ("Name", "Module", "Member", "Distribution", "Error"),
            results,
        )
