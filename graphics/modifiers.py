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

    def modify(self, src: pygame.Surface, frame: int) -> None:
        x = self.x.get_value(frame)
        y = self.y.get_value(frame)
        src = pygame.transform.flip(src, x, y)
        return src
