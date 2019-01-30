from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
    lookup: collection_inspect
    author: Adrian Likins <alikins@redhat.com>
    version_added: "2.8"
    short_description: report info about where this plugin was loaded from
    description:
        - Inspect and introspect info about this plugin, loader, and collection
    options:
      _terms:
        description: unused list
        required: False
"""

EXAMPLES = """
- debug: msg="This plugin: {{ lookup('collection_inspect','dummy') }} "
"""

RETURN = """
  _list:
    description:
      - values about the plugin and it's collection.
    type: list
"""

import os

from ansible.plugins.lookup import LookupBase


def get_dunders(_globals):
    dunder_candidates = ('__cached__', '__file__', '__loader__',
                         '__name__', '__package__', '__spec__')
    # _globals = globals()

    not_defined_blurb = '_IS_NOT_DEFINED'

    data = {}
    for candidate in dunder_candidates:
        data[candidate] = _globals.get(candidate,
                                       "%s%s" % (candidate.upper(), not_defined_blurb))

    return data


class LookupModule(LookupBase):

    def run(self, terms, variables, **kwargs):

        ret = []
        dunders = get_dunders(globals())
        for key in dunders:
            ret.append("%s=%s" % (key, dunders[key]))
        return ret
