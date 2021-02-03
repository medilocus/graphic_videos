#
#  Graphic Videos
#  An API for creating graphic videos in Python.
#  Copyright Medilocus 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import sys


class Printer:
    """Simplifies sys.stdout and clearing stdout line."""

    def __init__(self):
        self.max_len = 0

    def write(self, msg):
        sys.stdout.write(msg)
        sys.stdout.flush()
        self.max_len = max(len(msg), self.max_len)

    def clearline(self):
        sys.stdout.write("\r")
        sys.stdout.write(" "*self.max_len)
        sys.stdout.write("\r")
        sys.stdout.flush()


printer = Printer()
