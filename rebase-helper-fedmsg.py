#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
#
# This tool helps you to rebase package to the latest version
# Copyright (C) 2013-2014 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# he Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Authors: Petr Hracek <phracek@redhat.com>
#          Tomas Hozza <thozza@redhat.com>


# It requires fedmsg package
from __future__ import print_function
import fedmsg
from rebasehelper.upstream_monitoring import UpstreamMonitoring

# Testing command line
# echo "{'package':'wget', 'version': '1.6.13'} | fedmsg-logger

for name, endpoint, topic, msg in fedmsg.tail_messages():
    if msg['username'] == 'phracek':
        up = UpstreamMonitoring(name, endpoint, topic, msg)
        up.process_messsage()