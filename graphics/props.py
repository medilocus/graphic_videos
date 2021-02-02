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

from math import e
from .options import *


class Keyframe:
    def __init__(self, frame, value, interp):
        self.frame = frame
        self.value = value
        self.interp = interp


def interpolate(key1, key2, frame):
    if key1.interp == "CONSTANT":
        return key1.value

    elif key1.interp == "LINEAR":
        fac = (frame-key1.frame) / (key2.frame-key1.frame)
        value = fac * (key2.value-key1.value) + key1.value
        return value

    elif key1.interp == "SIGMOID":
        x_range = 3  # Sigmoid function starts moving from 0 to 1 noticably in the range (-3, 3)
        fac = (frame-key1.frame) / (key2.frame-key1.frame) * x_range * 2
        fac -= x_range
        fac = 1 / (1 + e**(-1*fac))
        value = fac * (key2.value-key1.value) + key1.value
        return value


class Property:
    def __init__(self, default_val):
        """
        Initializes boolean property.
        :param default_val: Value to use when there are no keyframes.
        """
        self._default_val = self.dtype(default_val)
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
        self._keyframes.append(Keyframe(frame, self.dtype(value), interp))
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
                    rval = interpolate(self._keyframes[low_idx], self._keyframes[low_idx+1], frame)

        return self.dtype(rval)


class BoolProp(Property):
    dtype = bool
    default_interp = "CONSTANT"
    allowed_interps = ("CONSTANT",)


class IntProp(Property):
    dtype = int
    default_interp = "SIGMOID"
    allowed_interps = ("LINEAR", "SIGMOID")


class FloatProp(Property):
    dtype = float
    default_interp = "SIGMOID"
    allowed_interps = ("LINEAR", "SIGMOID")
