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
from .elements import BaseElement
pygame.init()


class Scene:
    """Scene object."""

    _start: int
    _end: int
    _step: int
    _pause: Tuple[int]
    _elements: List[BaseElement]

    def __init__(self, start: int, end: int, step: int, before_pause: int = 30, after_pause: int = 30) -> None:
        """
        Initializes scene.
        :param start: Start frame of scene.
        :param end: End frame of scene.
        :param step: Frame step.
        :param before_pause: Pause (frames) before the scene starts.
        :param after_pause: Pause (frames) after the scene starts.
        """
        self._start = start
        self._end = end
        self._step = step
        self._pause = (before_pause, after_pause)
        self._elements = []

    def get_frames(self) -> List[int]:
        """
        Returns a list of all frames to render.
        """
        return list(range(self._start, self._end+sum(self._pause), self._step))

    def add_element(self, element: BaseElement) -> None:
        self._elements.append(element)

    def render(self, res, frame):
        surface = pygame.Surface(res)
        for element in self._elements:
            surface.blit(element.render(res, frame-self._pause[0]), (0, 0))
        return surface
