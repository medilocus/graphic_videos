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
    def __init__(self, frame, value, interp):
        self.frame = frame
        self.value = value
        self.interp = interp


def interpolate(key1, key2):
    if key1.interp == "CONSTANT":
        return key1.value


class Property:
    def __init__(self, default_val):
        """
        Initializes boolean property.
        :param default_val: Value to use when there are no keyframes.
        """
        self._default_val = self.type(default_val)
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
        self._keyframes.append(Keyframe(frame, self.type(value), interp))
        self._keyframes.sort(key=lambda x: x.frame)

    def get_value(self, frame):
        """
        Gets property value at frame. Returns default_val if no keyframes exist.
        :param frame: Frame to get value. The value will change based on the keyframes.
        """
        if len(self._keyframes) == 0:
            rval = self._default_val
        else:
            if frame < self._keyframes[0].frame:
                rval = self._keyframes[0].value
            else:
                low_idx = len(self._keyframes) - 1
                for i, key in enumerate(self._keyframes):
                    if key.frame > frame:
                        low_idx = i - 1
                        break

                if low_idx == len(self._keyframes) - 1:
                    rval = self._keyframes[-1].value
                else:
                    rval = interpolate(self._keyframes[low_idx], self._keyframes[low_idx+1])

        return self.type(rval)


class BoolProp(Property):
    type = bool
    default_interp = "CONSTANT"
    allowed_interps = ("CONSTANT",)


class IntProp(Property):
    type = int
    default_interp = "SIGMOID"
    allowed_interps = ("LINEAR", "SIGMOID")
