===========================
 Entry Point Inspector 0.1
===========================

.. tags:: python entry_point_inspector release

Entry Point Inspector is a tool for looking at the entry point plugins
installed on a system.

For details, see the `home page on PyPI`_ or `GitHub repository`_.

.. _home page on PyPI: https://pypi.python.org/pypi/entry_point_inspector
.. _GitHub repository: https://github.com/dhellmann/entry_point_inspector

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
