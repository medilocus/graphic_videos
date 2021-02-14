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
pygame.init()


class Scene:
    """Scene object."""

    start: int
    end: int
    step: int
    pause: Tuple[int]
    elements: List[BaseElement]
    bg_col: VectorProp
    motion_blur: bool

    def __init__(self, start: int, end: int, step: int = 1, bg_col: Tuple[int] = (0, 0, 0, 0),
            before_pause: int = 30, after_pause: int = 30, motion_blur: bool = True) -> None:
        """
        Initializes scene.
        :param start: Start frame of scene.
        :param end: End frame of scene.
        :param step: Frame step.
        :param bg_col: Background color of scene.
        :param before_pause: Pause (frames) before the scene starts.
        :param after_pause: Pause (frames) after the scene starts.
        :param motion_blur: Whether to use simple motion blur. Increases export time significantly.
        """
        self.start = start
        self.end = end
        self.step = step
        self.pause = (before_pause, after_pause)
        self.elements = []
        self.bg_col = VectorProp(4, IntProp, bg_col)
        self.motion_blur = motion_blur

    def get_frames(self) -> List[int]:
        """
        Returns a list of all frames to render.
        """
        return list(range(self.start, self.end+sum(self.pause), self.step))

    def add_element(self, element: BaseElement) -> None:
        """
        Appends element.
        :param element: Element to append.
        """
        self.elements.append(element)

    def render_frame(self, res, frame) -> pygame.Surface:
        """
        Renders single frame with no motion blur.
        Meant for internal use.
        """
        surface = pygame.Surface(res, pygame.SRCALPHA)
        surface.fill(self.bg_col(frame))
        for element in self.elements:
            if element.show(frame):
                surface.blit(element.render(res, frame-self.pause[0]), (0, 0))
        return surface

    def render(self, res, frame) -> pygame.Surface:
        """
        Renders element as pygame surface.
        :param res: Resolution to render.
        :param frame: Frame to render.
        """
        if self.motion_blur:
            surface = pygame.Surface(res, pygame.SRCALPHA)
            mb_frames = get_mb_frames()
            mb_step = get_mb_step()
            for offset in reversed([mb_step*i for i in range(mb_frames)]):
                for fac in (1, -1):
                    curr_alpha = 255 * offset / (mb_frames*mb_step)
                    color = (0, 0, 0, int(curr_alpha))
                    mask_surf = pygame.Surface(res, pygame.SRCALPHA)
                    mask_surf.fill(color)

                    curr_frame = frame + fac*offset
                    curr_surf = self.render_frame(res, curr_frame)
                    curr_surf.blit(mask_surf, (0, 0))
                    surface.blit(curr_surf, (0, 0))

            surface.set_alpha(False)
            return surface

        else:
            surface = self.render_frame(res, frame)
            surface.set_alpha(False)
            return surface
