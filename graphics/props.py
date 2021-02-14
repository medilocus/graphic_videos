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

from typing import Any, Tuple
from math import e
from .options import *


class Keyframe:
    """Keyframe class, used for storing (frame, value, interp)"""

    frame: int
    value: Any
    interp: str

    def __init__(self, frame: int, value: Any, interp: str) -> None:
        self.frame = frame
        self.value = value
        self.interp = interp


def interpolate(key1: Keyframe, key2: Keyframe, frame: int) -> Any:
    """
    Calculates interpolation between two keyframes.
    Meant for internal use.
    """
    if key1.interp == "CONSTANT":
        return key1.value

    elif key1.interp == "LINEAR":
        fac = (frame-key1.frame) / (key2.frame-key1.frame)
        value = fac * (key2.value-key1.value) + key1.value
        return value

    elif key1.interp == "PARABOLIC":
        fac = (frame-key1.frame) / (key2.frame-key1.frame)
        para_max = get_pbola_xmax() ** 2
        if fac > 0.5:
            fac = 1 - fac
            fac = (get_pbola_xmax()/0.5 * fac) ** 2
            fac = -1 * fac / 2 / para_max
            fac += 1
        else:
            fac = (get_pbola_xmax()/0.5 * fac) ** 2
            fac = fac / 2 / para_max
        value = fac * (key2.value-key1.value) + key1.value
        return value

    elif key1.interp == "SIGMOID":
        raise ValueError("Using the SIGMOID interpolation may produce unexpected results.\n    Please use PARABOLIC instead.")
        fac = 2 * (frame-key1.frame) / (key2.frame-key1.frame) * SIGMOID_XRANGE - SIGMOID_XRANGE
        fac = 1 / (1 + e**(-1*fac))
        fac = (fac-0.5) * SIGMOID_COMPENSATION + 0.5
        value = fac * (key2.value-key1.value) + key1.value
        return value

    else:
        raise NotImplementedError(f"Interpolation {key1.interp} is not supported.")


class Property:
    """Base property class. BoolProp, IntProp... extends off of this."""

    dtype: Any
    default_interp: str
    allowed_interps: Tuple[str]

    _default_val: Any
    _keyframes: Tuple[Keyframe]

    def __init__(self, default_val: Any) -> None:
        """
        Initializes boolean property.
        :param default_val: Value to use when there are no keyframes.
        """
        self._default_val = self.dtype(default_val)
        self._keyframes = []

    def __call__(self, frame: int) -> Any:
        """
        Faster way to do self.get_value(frame).
        :param frame: Frame to get value. The value will change based on the keyframes.
        """
        return self.get_value(frame)

    def keyframe(self, value: Any, frame: int, interp: str = None) -> None:
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

    def get_value(self, frame: int) -> Any:
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


class VectorProp:
    """Vector property, a list of properties."""

    length: int
    dtype: Property
    elements: Tuple[Property]

    def __init__(self, length: int, dtype: Any, init_val: Any) -> None:
        """
        :param length: Length of vector property.
        :param dtype: Type of property, e.g. BoolProp, IntProp, FloatProp...
        :param init_val: Initial value of each index, in the form (val0, val1, val2, ...)
        """
        if not length >= 1:
            raise ValueError("Length is too short.")
        self.elements = [dtype(init_val[i]) for i in range(length)]
        self.length = length
        self.dtype = dtype

    def __call__(self, frame: int) -> Tuple[Any]:
        return [p(frame) for p in self.elements]

    def __getitem__(self, index: int) -> Property:
        return self.elements[index]

    def __repr__(self):
        string = "["
        for i in range(self.length):
            string += self.elements[i].__repr__()
            if i != self.length - 1:
                string += ", "
        string += "]"
        return string

    def keyframe(self, values: Tuple[Any], frame: int, interp: str = None) -> None:
        """
        :param values: List or Tuple of values to map to elements.
        :param frame: Frame to keyframe.
        :param interp: Interpolation. Uses default if set to None.
        """
        if not len(values) == self.length:
            raise ValueError("Values length does not match.")
        for i in range(self.length):
            self.elements[i].keyframe(values[i], frame, interp)

    def get_value(self, frame: int) -> Tuple[Any]:
        """
        Returs a list of the value of each prop.
        :param frame: Frame to get value. The value will change based on inserted keyframes.
        """
        return [p(frame) for p in self.elements]


class BoolProp(Property):
    """
    Boolean property.
    Interpolations: CONSTANT
    """
    dtype = bool
    default_interp = "CONSTANT"
    allowed_interps = ("CONSTANT",)

    def __repr__(self):
        return f"<BoolProp object, default_val={self._default_val}>"


class IntProp(Property):
    """
    Integer property.
    Interpolations: LINEAR, PARABOLIC, CONSTANT
    """
    dtype = int
    default_interp = "PARABOLIC"
    allowed_interps = ("LINEAR", "PARABOLIC", "CONSTANT")

    def __repr__(self):
        return f"<IntProp object, default_val={self._default_val}>"


class FloatProp(Property):
    """
    Float property.
    Interpolations: LINEAR, PARABOLIC, CONSTANT
    """
    dtype = float
    default_interp = "PARABOLIC"
    allowed_interps = ("LINEAR", "PARABOLIC", "CONSTANT")

    def __repr__(self):
        return f"<FloatProp object, default_val={self._default_val}>"


class StringProp(Property):
    """
    String property.
    Interpolations: CONSTANT
    """
    dtype = str
    default_interp = "CONSTANT"
    allowed_interps = ("CONSTANT",)

    def __repr__(self):
        return f"<StringProp object, default_val={self._default_val}>"
