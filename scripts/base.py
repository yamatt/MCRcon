#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       base.py
#       
#       Copyright 2012 Copyright 2012 Matthew Copperwaite <>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.



from ConfigParser import ConfigParser
from optparse import OptionParser
from getpass import getpass
import os

os.sys.path.append("..")	

from mrcon import MrConInterface

parser = OptionParser()
parser.add_option("-s", "--host", dest="host", help="Hostname and port of MineCraft Rcon server.")
parser.add_option("-c", "--config", dest="config", help="Optional path to config file.", metavar="FILE", default=None)
parser.add_option("-p", "--password", dest="password", help="Optional password argument for server. If ommited then password from stdin is requested.", default=None)


class MrCon(MrConInterface):
    UNIX_DEFAULT_CONFIG="/etc/mrcon.conf"
    @classmethod
    def from_args(cls):
        (options, args) = parser.parse_args()
        cls.options = options
        if options.config:
            return MrCon.from_config(options.config)
        if ":" in options.host:
            host, port = options.host.rsplit(":", 1)
            port = int(port)
        else:
            host = options.host
            port = MrCon.DEFAULT_PORT
        if options.password:
            password = options.password
        else:
            password = getpass("Password: ")
        return cls(password, host, port)
            
    @classmethod
    def from_config(cls, path):
        CONFIG_PART = "server"
        if not os.isfile(path):
            path = MrCon.UNIX_DEFAULT_CONFIG
            
        config = ConfigParser()
        with open(path, 'r') as f:
            config.readfp(f)
        host = config.get(CONFIG_PART, "host")
        port = config.getint(CONFIG_PART, "port")
        password = config.get(CONFIG_PART, "password")
        return cls(password, host, port)
        
