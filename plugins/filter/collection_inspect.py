# Copyright (c) 2017 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}


def collection_inspect(text):
    aq = [text, "# __file__: %s" % (__file__)]
    return ''.join(aq)


# ---- Ansible filters ----
class FilterModule(object):
    ''' collection inspect and introspection filter '''

    def filters(self):
        return {
            'collection_inspect': collection_inspect
        }
