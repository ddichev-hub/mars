#
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
---
cliconf: saos6x
short_description: Use saos6x cliconf to run command on CIENA SAOS 6x platform
description:
  - This saos6x plugin provides low level abstraction apis for
    sending and receiving CLI commands from CIENA SAOS 6x network devices.
version_added: "0.1"
"""

import re
import json

from itertools import chain

#from ansible.module_utils._text import to_bytes, to_text
#from ansible.module_utils.network.common.utils import to_list
#from ansible.plugins.cliconf import CliconfBase

#from functools import wraps

#from ansible.errors import AnsibleConnectionFailure
from ansible.module_utils._text import to_text
from ansible.module_utils.common._collections_compat import Mapping
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible.plugins.cliconf import CliconfBase


class Cliconf(CliconfBase):

    def get_device_info(self):
        device_info = {}

        device_info['network_os'] = 'saos6x'
#        device_info['network_os_version'] = 'saos-06-19-00-0242'
#        device_info['network_os_model'] = 'xxxx'
#        device_info['network_os_hostname'] = 'xxx'

        #reply = self.get('software show')
        #data = to_text(reply, errors='surrogate_or_strict').strip()
#
        #match = re.search(r'| Running Package     : (\S+)', data)
        #if match:
        #    device_info['network_os_version'] = match.group(1)
#
        #reply = self.get('chassis show capabilitie')
        #data = to_text(reply, errors='surrogate_or_strict').strip()
#
        #match = re.search(r'| Part Number/Revision      | (\S+)', data, re.M)
        #if match:
        #    device_info['network_os_model'] = match.group(1)
#
        #reply = self.get('system show host-name')
        #data = to_text(reply, errors='surrogate_or_strict').strip()
#
        #match = re.search(r'| Oper |  (\S+)', data, re.M)
        #if match:
        #    device_info['network_os_hostname'] = match.group(1)
                
        return device_info

    def configure(self, admin=False, exclusive=False):
        prompt = to_text(
            self._connection.get_prompt(), errors="surrogate_or_strict"
        ).strip()
        if not prompt.endswith("([>])|([\*>])"):
#            if admin and "admin-" not in prompt:
#                self.send_command("admin")
#            if exclusive:
#                self.send_command("configure exclusive")
#                return
            self.send_command("configure terminal")

    def get_config(self, source='running', flags=None):
        if source not in ('running', 'startup'):
            raise ValueError("fetching configuration from %s is not supported" % source)
        if source == 'running':
            cmd = 'config show diff'
        if source == 'startup':
            cmd = 'config show'
        else:
            cmd = 'config show'

        return self.send_command(cmd)

       
    def edit_config(self, commit, command,):
#        self.send_command(command, prompt, answer, False, newline)

        for cmd in chain(to_list(command)):
            self.send_command(cmd)

    def get(self, command, prompt=None, answer=None, sendonly=False, newline=True, check_all=False):
        return self.send_command(command=command, prompt=prompt, answer=answer, sendonly=sendonly, newline=newline, check_all=check_all)

    def get_device_operations(self):
        return {
            'supports_diff_replace': True,
            'supports_commit': True,
            'supports_rollback': False,
            'supports_defaults': True,
            'supports_onbox_diff': True,
            'supports_commit_comment': False,
            'supports_multiline_delimiter': True,
            'supports_diff_match': True,
            'supports_diff_ignore_lines': True,
            'supports_generate_diff': True,
            'supports_replace': True
        }

    def get_capabilities(self):
        result = super(Cliconf, self).get_capabilities()
        result['device_operations'] = self.get_device_operations()
        return json.dumps(result)

