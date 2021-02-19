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
from .base import BaseElement
from .simple import Text
from ..options import *
from ..props import *
pygame.init()


class TitleHoriz(BaseElement):
    """Two text horizontal title."""

    loc: Tuple[int]
    size: Tuple[int]
    text1: Text
    text2: Text

    def __init__(self, frame_start: int, frame_len: int = 120, loc: Tuple[int] = (0, 0), size: Tuple[int] = (1920, 1080),
            font: str = None, font_size_1: int = 36, font_size_2: int = 36, text1: str = "Text 1", text2: str = "Text 2",
            text_col: Tuple[int] = (255, 255, 255)) -> None:

        super().__init__()
        if font is None:
            font = get_font()

        self.loc = loc
        self.size = size
        self.text1 = Text((0, 0), text_col, font, text1, font_size_1)
        self.text2 = Text((0, 0), text_col, font, text2, font_size_2)

        width = self.text1.get_size()[0]
        self.text1.loc.keyframe((-1*width, size[1]//3), frame_start, interp="LINEAR")
        self.text1.loc.keyframe((size[0]//2-size[0]//15, size[1]//3), frame_start+frame_len//3, interp="LINEAR")
        self.text1.loc.keyframe((size[0]//2+size[0]//15, size[1]//3), frame_start+frame_len//1.5, interp="LINEAR")
        self.text1.loc.keyframe((size[0]+width, size[1]//3), frame_start+frame_len, interp="LINEAR")

        width = self.text2.get_size()[0]
        self.text2.loc.keyframe((size[0]+width, size[1]//1.5), frame_start, interp="LINEAR")
        self.text2.loc.keyframe((size[0]//2+size[0]//15, size[1]//1.5), frame_start+frame_len//3, interp="LINEAR")
        self.text2.loc.keyframe((size[0]//2-size[0]//15, size[1]//1.5), frame_start+frame_len//1.5, interp="LINEAR")
        self.text2.loc.keyframe((-1*width, size[1]//1.5), frame_start+frame_len, interp="LINEAR")

    def render_raw(self, res: Tuple[int], frame: int):
        surface = pygame.Surface(res, pygame.SRCALPHA)

        subsurf = pygame.Surface(self.size, pygame.SRCALPHA)
        subsurf.blit(self.text1.render(res, frame), (0, 0))
        subsurf.blit(self.text2.render(res, frame), (0, 0))

        surface.blit(subsurf, self.loc)
        return surface


class CaptionLeft(BaseElement):
    """Small caption fit to be displayed on the left."""

    frame_start: int
    frame_len: int
    transition_len: int

    loc: Tuple[int]
    circle_radius: int
    rect_width: int
    rect_height: int

    color_circle: VectorProp
    color_rect: VectorProp

    def __init__(self, frame_start: int, frame_len: int, transition_len: int, loc: Tuple[int], circle_radius: int = 35,
            rect_width: int = 50, rect_height: int = 200, color_circle: Tuple[int] = (30, 40, 120, 255),
            color_rect: Tuple[int] = (180, 50, 15, 255), auto_show: bool = True) -> None:
        super().__init__()
        self.frame_start = frame_start
        self.frame_len = frame_len
        self.transition_len = transition_len

        self.loc = loc
        self.circle_radius = circle_radius
        self.rect_width = rect_width
        self.rect_height = rect_height

        self.color_circle = VectorProp(4, IntProp, color_circle)
        self.color_rect = VectorProp(4, IntProp, color_rect)

        if auto_show:
            self.show.keyframe(False, frame_start-1)
            self.show.keyframe(True, frame_start)
            self.show.keyframe(True, frame_start+frame_len+2*transition_len)
            self.show.keyframe(False, frame_start+frame_len+2*transition_len+1)
