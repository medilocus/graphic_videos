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

from typing import Tuple
from PIL import Image, ImageFilter
import colorsys
import pygame
from .props import *
pygame.init()


class Modifier:
    """Base modifier class. Other modifiers should inherit from this."""

    def modify(self, src: pygame.Surface, frame: int) -> pygame.Surface:...


class ModFlip(Modifier):
    """Flips the surface along x or y or both axes."""

    x: BoolProp
    y: BoolProp

    def __init__(self, x: bool, y: bool) -> None:
        """
        Initializes modifier.
        :param x: Flip on x axis?
        :param y: Flip on y axis?
        """
        self.x = BoolProp(x)
        self.y = BoolProp(y)

    def modify(self, src: pygame.Surface, frame: int) -> pygame.Surface:
        x = self.x.get_value(frame)
        y = self.y.get_value(frame)
        src = pygame.transform.flip(src, x, y)
        return src


class ModHsva(Modifier):
    """Changes surface HSVA."""
    # todo efficiency
    # todo fix bugs

    h: FloatProp
    s: FloatProp
    v: FloatProp
    a: FloatProp

    def __init__(self, h: float, s: float, v: float, a: float) -> None:
        """
        Initializes modifier.
        :param h: Hue (additive).
        :param s: Saturation (multiplicative).
        :param v: Value (multiplicative).
        :param a: Alpha (multiplicative).
        """
        self.h = FloatProp(h)
        self.s = FloatProp(s)
        self.v = FloatProp(v)
        self.a = FloatProp(a)

    def modify(self, src: pygame.Surface, frame: int) -> pygame.Surface:
        surf = src.copy()
        h = self.h.get_value(frame)
        s = self.s.get_value(frame)
        v = self.v.get_value(frame)
        a = self.a.get_value(frame)

        for x in range(src.get_width()):
            for y in range(src.get_height()):
                curr_col = [i/255 for i in src.get_at((x, y))]
                curr_col = [*colorsys.rgb_to_hsv(*curr_col[:3]), curr_col[3]]
                curr_col = [curr_col[0]+h, curr_col[1]*s, curr_col[2]*v, curr_col[3]*a]
                curr_col = [*[i*255 for i in colorsys.hsv_to_rgb(*curr_col[:3])], curr_col[3]]
                surf.set_at((x, y), curr_col)

        return surf


class ModGaussianBlur(Modifier):
    """Blurs the surface using Gaussian Blur"""

    radius: FloatProp

    def __init__(self, radius: int):
        self.radius = IntProp(radius)

    def modify(self, src: pygame.Surface, frame: int) -> pygame.Surface:
        surf = pygame.surfarray.array3d(src)
