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


class Keyframe:
    def __init__(self, frame, value, interpolation=DEFAULT_INTERPOLATION):
        """
        Initializes keyframe.
        :param frame: Frame of the keyframe.
        :param value: Value of the keyframe.
        :param interpolation: Interpolation of this keyframe to the next (if it exists).
        """
        self.frame = frame
        self.value = value
        self.interpolation = interpolation


class BoolProp:
    def __init__(self, default_val):
        """
        Initializes boolean property.
        :param default_val: Value to use when there are no keyframes.
        """
        self.default_val = default_val
        self.keyframes = []
