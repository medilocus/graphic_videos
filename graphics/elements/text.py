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
from ..options import *
from .simple import Text
pygame.init()


class TitleHoriz:
    """Two text horizontal title."""

    loc: Tuple[int]
    size: Tuple[int]
    text1: Text
    text2: Text

    def __init__(self, frame_start: int, frame_len: int = 120, loc: Tuple[int] = (0, 0), size: Tuple[int] = (1920, 1080),
            font: str = DEFAULT_FONT, font_size_1: int = 36, font_size_2: int = 36, text1: str = "Text 1", text2: str = "Text 2",
            text_col: Tuple[int] = (255, 255, 255)) -> None:

        self.loc = loc
        self.size = size
        self.text1 = Text((0, 0), text_col, font, text1, font_size_1)
        self.text2 = Text((0, 0), text_col, font, text2, font_size_2)

        self.text1.loc.keyframe((-100, size[1]//3), frame_start, interp="LINEAR")
        self.text1.loc.keyframe((size[0]//2-75, size[1]//3), frame_start+frame_len//3, interp="LINEAR")
        self.text1.loc.keyframe((size[0]//2+75, size[1]//3), frame_start+frame_len//1.5, interp="LINEAR")
        self.text1.loc.keyframe((size[0]+100, size[1]//3), frame_start+frame_len, interp="LINEAR")

        self.text2.loc.keyframe((size[0]+100, size[1]//1.5), frame_start, interp="LINEAR")
        self.text2.loc.keyframe((size[0]//2+75, size[1]//1.5), frame_start+frame_len//3, interp="LINEAR")
        self.text2.loc.keyframe((size[0]//2-75, size[1]//1.5), frame_start+frame_len//1.5, interp="LINEAR")
        self.text2.loc.keyframe((-100, size[1]//1.5), frame_start+frame_len, interp="LINEAR")

    def render(self, res: Tuple[int], frame: int, transp: bool = True):
        if transp:
            surface = pygame.Surface(res, pygame.SRCALPHA)
        else:
            surface = pygame.Surface(res)

        subsurf = pygame.Surface(self.size, pygame.SRCALPHA)
        subsurf.blit(self.text1.render(res, frame), (0, 0))
        subsurf.blit(self.text2.render(res, frame), (0, 0))

        surface.blit(subsurf, self.loc)
        return surface
