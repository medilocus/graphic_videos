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
from ..props import *
from ..modifiers import Modifier
pygame.init()


class BaseElement:
    """
    Empty element, other elements should inherit.
    """

    show: BoolProp
    modifiers: List[Modifier]

    def __init__(self) -> None:
        """
        BaseElement init. Other elements should have their own init
        and call super().__init__()
        """
        self.show = BoolProp(True)
        self.modifiers = []

    def add_modifier(self, modifier: Modifier) -> None:
        """
        Appends modifier.
        :param modifier: Modifier to append.
        """
        self.modifiers.append(modifier)

    def extend_modifiers(self, modifiers: Tuple[Modifier]) -> None:
        self.modifiers.extend(modifiers)

    def render(self, res: Tuple[int], frame: int) -> pygame.Surface:
        """
        Renders element as pygame surface.
        :param res: Resolution to render.
        :param frame: Frame to render.
        """
        surf = self.render_raw(res, frame)
        for modifier in self.modifiers:
            if modifier.show(frame):
                surf = modifier.modify(surf, frame)
        return surf
