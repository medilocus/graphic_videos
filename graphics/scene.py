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
from .props import *
pygame.init()


class Scene:
    def __init__(self, cam_loc, cam_xsize, before_pause=10, after_pause=10):
        """
        Initializes scene.
        :param cam_loc: Location of the center of the camera.
        :param cam_xsize: Size, NOT resolution (pixels) of the camera X. Decreasing this value is like zooming in.
        :param before_pause: Pause (frames) before the scene starts.
        :param after_pause: Pause (frames) after the scene starts.
        """
        self._pause = (before_pause, after_pause)
        self._elements = []
        self.cam_loc = VectorProp(2, IntProp, cam_loc)
        self.cam_xsize = FloatProp(cam_xsize)

    def add_element(self, element):
        self._elements.append(element)

    def get_length(self):
        pass

    def render(self, res, frame):
        surface = pygame.Surface(res)
