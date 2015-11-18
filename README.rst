=======================
 Entry Point Inspector
=======================

Entry Point Inspector is a tool for looking at the entry point plugins
installed on a system.

Commands
========

==============  =================================================
Name            Description
==============  =================================================
ep show         Shows the details for a single entry point.
group list      Shows the groups for which plugins are available.
group show      Shows the members of a specific group.
help            print detailed help for another command
==============  =================================================

Examples
========

::

  $ epi group list
  +--------------------------+
  | Name                     |
  +--------------------------+
  | cliff.formatter.list     |
  | cliff.formatter.show     |
  | console_scripts          |
  | distutils.commands       |
  | distutils.setup_keywords |
  | egg_info.writers         |
  | epi.commands             |
  | setuptools.file_finders  |
  | setuptools.installation  |
  +--------------------------+

  $ epi group show epi.commands
  +------------+-----------------------------+----------------+---------------------------+-------+
  | Name       | Module                      | Member         | Distribution              | Error |
  +------------+-----------------------------+----------------+---------------------------+-------+
  | group_list | entry_point_inspector.group | GroupList      | entry-point-inspector 0.1 |       |
  | group_show | entry_point_inspector.group | GroupShow      | entry-point-inspector 0.1 |       |
  | ep_show    | entry_point_inspector.ep    | EntryPointShow | entry-point-inspector 0.1 |       |
  +------------+-----------------------------+----------------+---------------------------+-------+

  $ epi -v ep show epi.commands ep_show
  Looking for ep_show in group epi.commands
  +--------------+--------------------------------------------------------------------+
  | Field        | Value                                                              |
  +--------------+--------------------------------------------------------------------+
  | Module       | entry_point_inspector.ep                                           |
  | Member       | EntryPointShow                                                     |
  | Distribution | entry-point-inspector 0.1                                          |
  | Path         | /Users/dhellmann/Devel/entry_point_inspector/entry_point_inspector |
  | Error        |                                                                    |
  +--------------+--------------------------------------------------------------------+

  $ epi -v ep show epi.commands ep_show --distribution "entry-point-inspector==0.1"
  Loading ep_show from epi.commands using distribution entry-point-inspector==0.1
  +--------------+--------------------------------------------------------------------+
  | Field        | Value                                                              |
  +--------------+--------------------------------------------------------------------+
  | Module       | entry_point_inspector.ep                                           |
  | Member       | EntryPointShow                                                     |
  | Distribution | entry-point-inspector 0.1                                          |
  | Path         | /Users/dhellmann/Devel/entry_point_inspector/entry_point_inspector |
  | Error        |                                                                    |
  +--------------+--------------------------------------------------------------------+

See Also
========

* `stevedore`_

.. _stevedore: https://pypi.python.org/pypi/stevedore
