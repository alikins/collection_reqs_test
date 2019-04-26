from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action import ActionBase

from ansible_collections.alikins.collection_inspect.plugins.module_utils import whatever


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        if hasattr(whatever, 'anything_at_all'):
            # nah
            pass

        return result
