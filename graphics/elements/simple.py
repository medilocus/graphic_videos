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
from . import BaseElement
from ..props import *
from ..utils import *
pygame.init()

# todo antialiasing


class Rect(BaseElement):
    """Rectangle element."""

    loc: VectorProp
    size: VectorProp
    border: IntProp
    color: VectorProp
    border_color: VectorProp
    antialias: BoolProp

    def __init__(self, loc: Tuple[int] = (0, 0), size: Tuple[int] = (100, 200), color: Tuple[int] = (255, 255, 255),
            border: int = 0, border_color: Tuple[int] = (255, 255, 255), antialias: bool = True) -> None:
        """
        Initializes rectangle.
        :param loc: Top left corner location (pixels) of rectangle.
        :param size: Size (x, y) pixels of rectangle.
        :param border: Border width (pixels) of rectangle. Set to 0 to disable border.
        :param color: Color (rgba, 0 to 255) of rectangle. The ALPHA will be set to 255 if no alpha is given.
        :param border_color: Border color of rectangle.
        :param antialias: Whether to perform simple antialiasing when rendering.
        """
        super().__init__()
        color = get_color(color)
        if len(color) == 3:
            color = (*color, 255)
        if len(border_color) == 3:
            border_color = (*border_color, 255)

        self.loc = VectorProp(2, IntProp, loc)
        self.size = VectorProp(2, IntProp, size)
        self.border = IntProp(border)
        self.color = VectorProp(4, IntProp, color)
        self.border_color = VectorProp(4, IntProp, border_color)
        self.antialias = BoolProp(antialias)

    def render(self, res: Tuple[int], frame: int) -> pygame.Surface:
        surface = pygame.Surface(res, pygame.SRCALPHA)

        loc = self.loc.get_value(frame)
        size = self.size.get_value(frame)
        border = self.border.get_value(frame)
        color = self.color.get_value(frame)
        border_color = self.border_color.get_value(frame)
        antialias = self.antialias.get_value(frame)

        pygame.draw.rect(surface, color, (*loc, *size))
        if border > 0:
            pygame.draw.rect(surface, border_color, (*loc, *size), border)

        return surface


class Circle(BaseElement):
    """Circle element."""

    loc: VectorProp
    radius: IntProp
    border: IntProp
    color: VectorProp
    border_color: VectorProp
    antialias: BoolProp

    def __init__(self, loc: Tuple[int] = (0, 0), radius: int = 25, color: Tuple[int] = (255, 255, 255),
            border: int = 0, border_color: Tuple[int] = (255, 255, 255), antialias: bool = True) -> None:
        """
        Initializes circle.
        :param loc: Center location (pixels) of circle.
        :param radius: Radius of circle (pixels).
        :param border: Border of circle (pixels).
        :param color: Color (rgba, 0 to 255) of circle. The ALPHA will be set to 255 if no alpha is given.
        :param border_color: Color of circle border.
        :param antialias: Whether to perform simple antialiasing when rendering.
        """
        super().__init__()
        if len(color) == 3:
            color = (*color, 255)
        if len(border_color) == 3:
            border_color = (*border_color, 255)

        self.loc = VectorProp(2, IntProp, loc)
        self.radius = IntProp(radius)
        self.border = IntProp(border)
        self.color = VectorProp(4, IntProp, color)
        self.border_color = VectorProp(4, IntProp, border_color)
        self.antialias = BoolProp(antialias)

    def render(self, res: Tuple[int], frame: int) -> pygame.Surface:
        surface = pygame.Surface(res, pygame.SRCALPHA)

        loc = self.loc.get_value(frame)
        radius = self.radius.get_value(frame)
        border = self.border.get_value(frame)
        color = self.color.get_value(frame)
        border_color = self.border_color.get_value(frame)
        antialias = self.antialias.get_value(frame)

        pygame.draw.circle(surface, color, loc, radius)
        if border > 0:
            pygame.draw.circle(surface, border_color, loc, radius, border)

        return surface


class Line(BaseElement):
    """Line element."""

    loc1: VectorProp
    loc2: VectorProp
    thickness: IntProp
    color: VectorProp
    antialias: BoolProp

    def __init__(self, loc1: Tuple[int] = (0, 0), loc2: Tuple[int] = (50, 50), thickness: int = 1,
            color: Tuple[int] = (255, 255, 255), antialias: bool = True) -> None:
        """
        Initializes line.
        :param loc1: Location (x, y) of the first point.
        :param loc2: Location (x, y) of the second point.
        :param thickness: Thickness (pixels) of line.
        :param color: Color (RGB) of line.
        :param antialias: Whether to perform simple antialiasing when rendering.
        """
        super().__init__()
        if len(color) == 3:
            color = (*color, 255)

        self.loc1 = VectorProp(2, IntProp, loc1)
        self.loc2 = VectorProp(2, IntProp, loc2)
        self.thickness = IntProp(thickness)
        self.color = VectorProp(4, IntProp, color)
        self.antialias = BoolProp(antialias)

    def render(self, res: Tuple[int], frame: int) -> pygame.Surface:
        surface = pygame.Surface(res, pygame.SRCALPHA)

        loc1 = self.loc1.get_value(frame)
        loc2 = self.loc2.get_value(frame)
        thickness = self.thickness.get_value(frame)
        color = self.color.get_value(frame)
        antialias = self.antialias.get_value(frame)

        pygame.draw.line(surface, color, loc1, loc2, thickness)

        return surface


class Polygon(BaseElement):
    """Polygon element."""

    verts: Tuple[VectorProp]
    border: IntProp
    color: VectorProp
    border_color: VectorProp
    offset: VectorProp
    antialias: BoolProp

    def __init__(self, verts: Tuple[Tuple[int]], color: Tuple[int] = (255, 255, 255), border: int = 0,
            border_color: Tuple[int] = (255, 255, 255), offset: Tuple[int] = (0, 0), antialias: bool = True) -> None:
        """
        Initializes polygon.
        :param verts: List of verts of polygon in the form ((x1, y1), (x2, y2), (x3, y3), ...).
        :param border: Border of polygon (pixels).
        :param color: Color (rgba, 0 to 255) of polygon. The ALPHA will be set to 255 if no alpha is given.
        :param border_color: Color of polygon border.
        :param offset: Offset all the verts by this value in the form (x, y).
        :param antialias: Whether to perform simple antialiasing when rendering.
        """
        super().__init__()
        if len(color) == 3:
            color = (*color, 255)
        if len(border_color) == 3:
            border_color = (*border_color, 255)

        self.verts = [VectorProp(2, IntProp, vert) for vert in verts]
        self.border = IntProp(border)
        self.color = VectorProp(4, IntProp, color)
        self.border_color = VectorProp(4, IntProp, border_color)
        self.offset = VectorProp(2, IntProp, offset)
        self.antialias = BoolProp(antialias)

    def render(self, res: Tuple[int], frame: int) -> pygame.Surface:
        surface = pygame.Surface(res, pygame.SRCALPHA)

        border = self.border.get_value(frame)
        color = self.color.get_value(frame)
        border_color = self.border_color.get_value(frame)
        offset = self.offset.get_value(frame)
        antialias = self.antialias.get_value(frame)
        verts = [(vx + offset[0], vy + offset[1]) for v in self.verts for vx, vy in v.get_value(frame)]

        pygame.draw.polygon(surface, color, verts)
        if border > 0:
            pygame.draw.polygon(surface, border_color, verts, border)

        return surface


class Text(BaseElement):
    """Text element."""

    loc: VectorProp
    color: VectorProp
    font: StringProp
    text: StringProp
    size: IntProp
    antialias: BoolProp

    def __init__(self, loc: Tuple[int] = (0, 0), color: Tuple[int] = (255, 255, 255), font: str = None,
            text: str = "Text", size: int = 36, antialias: bool = True) -> None:
        """
        Initializes text element.
        :param loc: Location of top left corner.
        :param color: Color (rgba) of text. Alpha will be set to 255 if omitted.
        :param font: Font family of text.
        :param text: Text.
        :param size: Font size.
        :param antialias: Whether to antialias rendered text.
        """
        super().__init__()
        if len(color) == 3:
            color = (*color, 255)
        if font is None:
            font = get_font()

        self.loc = VectorProp(2, IntProp, loc)
        self.color = VectorProp(4, IntProp, color)
        self.font = StringProp(font)
        self.text = StringProp(text)
        self.size = IntProp(size)
        self.antialias = BoolProp(antialias)

        self.last_font_family = None
        self.last_font = None

    def get_font(self, frame):
        font_family = self.font.get_value(frame)
        font_size = self.size.get_value(frame)
        if os.path.isfile(font_family):
            return pygame.font.Font(font_family, font_size)
        else:
            return pygame.font.SysFont(font_family, font_size)

    def get_size(self, frame: int = 0) -> Tuple[int]:
        font_family = self.font.get_value(frame)
        text_str = self.text.get_value(frame)
        size = self.size.get_value(frame)

        if self.last_font_family == (font_family, size):
            return self.last_font

        font = pygame.font.SysFont(font_family, size)
        text = font.render(text_str, True, (0, 0, 0))

        self.last_font = font
        self.last_font_family = (font_family, size)

        return text.get_size()

    def render(self, res: Tuple[int], frame: int) -> pygame.Surface:
        surface = pygame.Surface(res, pygame.SRCALPHA)

        loc = self.loc.get_value(frame)
        color = self.color.get_value(frame)
        text_str = self.text.get_value(frame)
        antialias = self.antialias.get_value(frame)

        font = self.get_font(frame)
        text = font.render(text_str, antialias, color)
        loc = [loc[i] - text.get_size()[i]//2 for i in range(2)]
        surface.blit(text, loc)

        return surface


class Image(BaseElement):
    """Image element."""

    loc: VectorProp
    size: VectorProp
    src: StringProp

    def __init__(self, loc: Tuple[int] = (0, 0), size: Tuple[int] = (1920, 1080), src: str = ""):
        """
        Initializes image.
        :param loc: Location of top left corner of image.
        :param size: Size (x, y) of image.
        :param src: Source path of image.
        """
        super().__init__()
        self.loc = VectorProp(2, IntProp, loc)
        self.size = VectorProp(2, IntProp, size)
        self.src = StringProp(src)

        self.last_src = None
        self.last_img = None

    def get_image(self, frame):
        src = self.src.get_value(frame)
        if src == self.last_src:
            return self.last_img

        image = pygame.image.load(src)
        self.last_src = src
        self.last_img = image

        return image

    def render(self, res: Tuple[int], frame: int) -> pygame.Surface:
        surface = pygame.Surface(res, pygame.SRCALPHA)

        loc = self.loc.get_value(frame)
        size = self.size.get_value(frame)

        image = self.get_image(frame)
        image = pygame.transform.scale(image, size)
        surface.blit(image, loc)

        return surface


class Video(BaseElement):
    """Video element."""

    loc: VectorProp
    size: VectorProp
    speed: float
    offset: float
    src: str
    video: Any
    last_frame: int
    last_img: pygame.Surface

    def __init__(self, loc: Tuple[int] = (0, 0), size: Tuple[int] = (1920, 1080), src: str = "", speed: float = 1, offset: float = 0):
        """
        Initializes video.
        :param loc: Location of top left corner of video.
        :param size: Size (x, y) of video.
        :param src: Source path of video.
        :param speed: Speed of video. A speed of 1 means 1 frame of the video will be played every frame.
        :param offset: Offset in frames before the video starts playing.
        """
        super().__init__()
        self.loc = VectorProp(2, IntProp, loc)
        self.size = VectorProp(2, IntProp, size)
        self.speed = speed
        self.offset = offset
        self.src = src

        self.video_reset()
        self.max_frame = 0
        while True:
            img = self.video_next()
            if img is None:
                break
            self.max_frame += 1

        self.video_reset()

    def video_reset(self):
        self.video = cv2.VideoCapture(self.src)
        self.last_frame = -1
        self.last_img = None

    def video_next(self):
        if self.last_frame >= self.max_frame:
            return None

        success, img = self.video.read()
        if success:
            self.last_img = cv2img2surf(img)
            self.last_frame += 1
            return img
        return None

    def get_surf(self, frame):
        if self.last_frame > frame:
            self.video_reset()

        while self.last_frame < frame:
            result = self.video_next()
            if result is None:
                # means end of video.
                return pygame.Surface((100, 100), pygame.SRCALPHA)

        return (pygame.Surface((100, 100), pygame.SRCALPHA) if self.last_img is None else self.last_img)

    def render(self, res: Tuple[int], frame: int) -> pygame.Surface:
        surface = pygame.Surface(res, pygame.SRCALPHA)

        loc = self.loc.get_value(frame)
        size = self.size.get_value(frame)
        surf = self.get_surf(frame*self.speed-self.offset)

        surf = pygame.transform.scale(surf, size)
        surface.blit(surf, loc)

        return surface
