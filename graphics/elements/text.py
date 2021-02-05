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

    text1: Text
    text2: Text

    def __init__(self, frame_start: int, frame_len: int = 60, loc: Tuple[int] = (0, 0), size: Tuple[int] = (1920, 1080),
            font: str = DEFAULT_FONT, text1: str = "Text 1", text2: str = "Text 2", text_col: Tuple[int] = (255, 255, 255)) -> None:
        self.text1 = Text((0, 0), text_col, font, text1, 18)
        self.text2 = Text((0, 0), text_col, font, text2, 18)
