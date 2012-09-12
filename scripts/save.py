#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       save.py
#       
#       Copyright 2012 Matthew Copperwaite <>
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



import base

base.parser.add_option("-y", "--on", dest="save", action="store_true", help="Sets the save state on the specified server to on.")
base.parser.add_option("-n", "--off", dest="save", action="store_false", help="Sets the save state on the specified server to off.")

server = base.MrCon.from_args()

if server.options.save == None:
    msg = server.save_all()
else:
    if server.options.save:
        msg = server.save_on()
    else:
        msg = server.save_off()

server.close()
print msg
exit(0)
