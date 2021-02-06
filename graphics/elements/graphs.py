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
from ..props import *
pygame.init()


class BarGraphVert:
    """Vertical Bar Graph element."""

    loc: VectorProp
    size: VectorProp
    choices: Tuple[StringProp]
    colors: Tuple[VectorProp]
    border: IntProp
    border_color: VectorProp

    def __init__(self, loc: Tuple[int], size: Tuple[int], choices: Tuple[str], colors: Tuple[Tuple[int]] = None, border: int = 4, border_color: int = (0, 0, 0)):
        if len(choices) != len(colors):
            raise ValueError(f"The length of choices, {len(choices)} must be equal to the length of colors, {len(colors)}")
        self.loc = VectorProp(2, IntProp, loc)
        self.size = VectorProp(2, IntProp, size)
        self.choices = [StringProp(choices[i]) for i in range(len(choices))]
        self.colors = [VectorProp(4, IntProp, (*colors[i], 255) if len(colors[i]) == 3 else colors[i]) for i in range(len(colors))]
        self.border = IntProp(border)
        self.border_color = VectorProp(2, IntProp, border_color)
