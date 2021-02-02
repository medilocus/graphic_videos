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

import pygame
from typing import Tuple
from ..props import *
pygame.init()


class Rect:
    """Rectangle element."""

    loc: VectorProp
    size: VectorProp
    color: VectorProp
    antialias: BoolProp

    def __init__(self, loc: Tuple[int], size: Tuple[int], color: Tuple[int], antialias: bool = True) -> None:
        """
        Initializes rectangle.
        :param loc: Top left corner location (pixels) of rectangle.
        :param size: Size (x, y) pixels of rectangle.
        :param color: Color (rgba, 0 to 255) of rectangle. The ALPHA will be set to 255 if no alpha is given.
        :param antialias: Whether to perform simple antialiasing when rendering.
        """
        if len(color) == 3:
            color = (*color, 255)
        self.loc = VectorProp(2, IntProp, loc)
        self.size = VectorProp(2, IntProp, size)
        self.color = VectorProp(4, IntProp, color)
        self.antialias = BoolProp(antialias)

    def render(self, res: Tuple[int], frame: int, transp: bool = True) -> pygame.Surface:
        """
        Renders the rectangle as a pygame.Surface.
        :param res: Output resolution.
        :param frame: Frame to render.
        :param transp: Background transparent?
        """
        if transp:
            surface = pygame.Surface(res, pygame.SRCALPHA)
        else:
            surface = pygame.Surface(res)

        loc = self.loc.get_value(frame)
        size = self.size.get_value(frame)
        color = self.color.get_value(frame)
        antialias = self.antialias.get_value(frame)

        if antialias:
            pygame.draw.rect(surface, (*color[:3], int(color[3]/2)), (loc[0]-1, loc[1]-1, size[0]+2, size[1]+2))
        pygame.draw.rect(surface, color, (*loc, *size))

        return surface


class Circle:
    """Circle element."""

    loc: VectorProp
    radius: IntProp
    color: VectorProp
    antialias: BoolProp

    def __init__(self, loc: Tuple[int], radius: int, color: Tuple[int], antialias: bool = True) -> None:
        """
        Initializes rectangle.
        :param loc: Center location (pixels) of circle.
        :param radius: Radius of circle (pixels).
        :param color: Color (rgba, 0 to 255) of rectangle. The ALPHA will be set to 255 if no alpha is given.
        :param antialias: Whether to perform simple antialiasing when rendering.
        """
        if len(color) == 3:
            color = (*color, 255)
        self.loc = VectorProp(2, IntProp, loc)
        self.radius = IntProp(radius)
        self.color = VectorProp(4, IntProp, color)
        self.antialias = BoolProp(antialias)

    def render(self, res: Tuple[int], frame: int, transp: bool = True) -> pygame.Surface:
        """
        Renders the rectangle as a pygame.Surface.
        :param res: Output resolution.
        :param frame: Frame to render.
        :param transp: Background transparent?
        """
        if transp:
            surface = pygame.Surface(res, pygame.SRCALPHA)
        else:
            surface = pygame.Surface(res)

        loc = self.loc.get_value(frame)
        radius = self.radius.get_value(frame)
        color = self.color.get_value(frame)
        antialias = self.antialias.get_value(frame)

        if antialias:
            pygame.draw.circle(surface, (*color[:3], int(color[3]/2)), loc, radius+1)
        pygame.draw.circle(surface, color, loc, radius)

        return surface
