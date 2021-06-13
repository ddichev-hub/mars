#
# (c) 2016 Red Hat Inc.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import re

from ansible.errors import AnsibleConnectionFailure
from ansible.plugins.terminal import TerminalBase


class TerminalModule(TerminalBase):

    terminal_stdout_re = [
#        re.compile(br"[\r\n](?:! )?(?:\* )?(?:\(.*\) )?(?:Slot-\d+ )?(?:VPEX )?\S+\.\d+ (?:[>#]) ?$")
         re.compile(br"([>])| ([\#])")
    ]

    terminal_stderr_re = [
        re.compile(br"ERROR:"),
        re.compile(br"FAILURE:"),
        re.compile(br"[\r\n%] Access denied"),
    ]


    def on_open_shell(self):
        try:
            self._exec_cli_command(u'set session more off')
        except AnsibleConnectionFailure:
            raise AnsibleConnectionFailure('unable to set terminal parameters')
