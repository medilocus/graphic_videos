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

from typing import List, Tuple
import pygame
from .props import *
from .elements import BaseElement
from .modifiers import Modifier
pygame.init()


class Group:
    """Group class, which contains elements and modifiers."""

    loc: VectorProp
    size: VectorProp
    elements: List[BaseElement]
    modifiers: List[Modifier]

    def __init__(self, loc: Tuple[int] = (0, 0), size: Tuple[int] = (1920, 1080)):
        """
        Initializes group.
        :param loc: Location (x, y) of top left corner of group.
        :param size: Size (x, y) of group.
        """
        self.loc = VectorProp(2, IntProp, loc)
        self.size = VectorProp(2, IntProp, size)
        self.elements = []
        self.modifiers = []

    def add_element(self, element: BaseElement) -> None:
        self.elements.append(element)

    def add_modifier(self, modifier: Modifier) -> None:
        self.modifiers.append(modifier)

    def render(self, res: Tuple[int], frame: int) -> pygame.Surface:
        surface = pygame.Surface(res, pygame.SRCALPHA)
        final_surf = pygame.Surface(res, pygame.SRCALPHA)

        for element in self.elements:
            surface.blit(element.render(res, frame), (0, 0))
        for modifier in self.modifiers:
            surface = modifier.modify(surface, frame)

        loc = self.loc.get_value(frame)
        size = self.size.get_value(frame)

        surface = pygame.transform.scale(surface, size)
        final_surf.blit(surface, loc)

        return final_surf
