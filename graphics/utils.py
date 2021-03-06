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

import os
from typing import Tuple
import pygame
import cv2
from .options import *
pygame.init()


def get_parent():
    return os.path.realpath(os.path.dirname(__file__))


def cv2img2surf(img) -> pygame.Surface:
    """
    Converts cv2 image to pygame surface.
    :param img: numpy.ndarray (cv2 image) to convert.
    """
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    surf = pygame.image.frombuffer(img.tostring(), img.shape[1::-1], "RGB")
    return surf


def get_color(color) -> Tuple[int]:
    """
    Gets the color from the color palette if it is in it, otherwise returns the color it received.
    :param color: 
    """
    return get_col_palette()[color] if color in get_col_palette() else color
