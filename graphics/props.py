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

from .options import *


class BoolProp:
    allowed_interps = ("CONSTANT",)
    default_interp = "CONSTANT"

    def __init__(self, default_val):
        """
        Initializes boolean property.
        :param default_val: Value to use when there are no keyframes.
        """
        self._default_val = bool(default_val)
        self._keyframes = []

    def add_keyframe(self, frame, value, interp=None):
        """
        Adds a keyframe and performs value checks.
        :param frame: Frame to insert a keyframe.
        :param value: Value of keyframe.
        :param interp: Keyframe interpolation. Uses self.default_interp if set to None.
        """
        if interp is None:
            interp = self.default_interp
        if interp not in self.allowed_interps:
            raise ValueError(f"Interpolation {interp} not allowed.")
        self._keyframes.append((frame, value, interp))
        self._keyframes.sort(key=lambda x: x[0])
