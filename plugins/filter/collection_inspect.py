# Copyright (c) 2017 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.collection_inspect import get_dunders

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}


def collection_inspect(text):
    dunders = get_dunders(globals())

    aq = [text,
          "#( __file__=%s" % dunders['__file__'],
          "__path__=%s" % dunders['__path__'],
          "__name__=%s" % dunders['__name__']]
    return ''.join(aq)


# ---- Ansible filters ----
class FilterModule(object):
    ''' collection inspect and introspection filter '''

    def filters(self):
        return {
            'collection_inspect': collection_inspect
        }
