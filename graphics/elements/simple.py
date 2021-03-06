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
import time
import shutil
from typing import Tuple
from math import atan, cos, degrees, radians, sin, sqrt, tan
from hashlib import sha256
import atexit
import pygame
from pygame import gfxdraw
import cv2
from . import BaseElement
from ..options import *
from ..props import *
from ..utils import *
from ..printer import printer
pygame.init()


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
        border_color = get_color(border_color)
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

    def render_raw(self, res: Tuple[int], frame: int) -> pygame.Surface:
        surface = pygame.Surface(res, pygame.SRCALPHA)

        loc = self.loc(frame)
        size = self.size(frame)
        border = self.border(frame)
        color = self.color(frame)
        border_color = self.border_color(frame)
        antialias = self.antialias(frame)

        if antialias:
            surface.fill(color, loc+size)
        else:
            pygame.draw.rect(surface, color, loc+size)
        if border > 0:
            pygame.draw.rect(surface, border_color, loc+size, border)

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
        color = get_color(color)
        border_color = get_color(border_color)
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

    def render_raw(self, res: Tuple[int], frame: int) -> pygame.Surface:
        surface = pygame.Surface(res, pygame.SRCALPHA)

        loc = self.loc(frame)
        radius = self.radius(frame)
        border = self.border(frame)
        color = self.color(frame)
        border_color = self.border_color(frame)
        antialias = self.antialias(frame)

        if antialias:
            gfxdraw.aacircle(surface, *loc, radius, color)
            gfxdraw.filled_circle(surface, *loc, radius, color)
        else:
            pygame.draw.circle(surface, color, loc, radius)
        if border > 0:
            pygame.draw.circle(surface, border_color, loc, radius, border)

        return surface


class Ellipse(BaseElement):
    """Ellipse element."""

    loc: VectorProp
    size: VectorProp
    color: VectorProp
    border: IntProp
    border_color: VectorProp
    antialias: BoolProp

    def __init__(self, loc: Tuple[int] = (0, 0), size: Tuple[int] = (100, 200), color: Tuple[int] = (255, 255, 255),
            border: int = 0, border_color: Tuple[int] = (255, 255, 255), antialias: bool = True) -> None:
        """
        Initializes ellipse.
        :param loc: Top left corner location (pixels) of ellipse.
        :param size: Size (x, y) pixels of ellipse. The ellipse will be centered inside this.
        :param color: Color (rgba, 0 to 255) of ellipse. The ALPHA will be set to 255 if no alpha is given.
        :param border: Border width (pixels) of ellipse. Set to 0 to disable border.
        :param border_color: Border color of ellipse.
        :param antialias: Whether to perform simple antialiasing when rendering.
        """
        super().__init__()
        color = get_color(color)
        border_color = get_color(border_color)
        if len(color) == 3:
            color = (*color, 255)
        if len(border_color) == 3:
            border_color = (*border_color, 255)

        self.loc = VectorProp(2, IntProp, loc)
        self.size = VectorProp(2, IntProp, size)
        self.color = VectorProp(4, IntProp, color)
        self.border = IntProp(border)
        self.border_color = VectorProp(4, IntProp, border_color)
        self.antialias = BoolProp(antialias)

    def render_raw(self, res: Tuple[int], frame: int) -> pygame.Surface:
        surface = pygame.Surface(res, pygame.SRCALPHA)

        loc = self.loc(frame)
        size = self.size(frame)
        color = self.color(frame)
        border = self.border(frame)
        border_color = self.border_color(frame)
        antialias = self.antialias(frame)

        if antialias:
            gfxdraw.aaellipse(surface, *loc, *size, color)
            gfxdraw.filled_ellipse(surface, *loc, *size, color)
        else:
            pygame.draw.ellipse(surface, color, loc+size)
        if border > 0:
            pygame.draw.ellipse(surface, border_color, loc+size, border)

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
        color = get_color(color)
        border_color = get_color(border_color)
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

    def render_raw(self, res: Tuple[int], frame: int) -> pygame.Surface:
        surface = pygame.Surface(res, pygame.SRCALPHA)

        border = self.border(frame)
        color = self.color(frame)
        border_color = self.border_color(frame)
        offset = self.offset(frame)
        antialias = self.antialias(frame)
        verts = [(vx + offset[0], vy + offset[1]) for v in self.verts for vx, vy in v(frame)]

        if antialias:
            gfxdraw.aapolygon(surface, verts, color)
            gfxdraw.filled_polygon(surface, verts, color)
        else:
            pygame.draw.polygon(surface, color, verts)
        if border > 0:
            pygame.draw.polygon(surface, border_color, verts, border)

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
        color = get_color(color)
        if len(color) == 3:
            color = (*color, 255)

        self.loc1 = VectorProp(2, IntProp, loc1)
        self.loc2 = VectorProp(2, IntProp, loc2)
        self.thickness = IntProp(thickness)
        self.color = VectorProp(4, IntProp, color)
        self.antialias = BoolProp(antialias)

    @classmethod
    def from_vector(cls, origin: Tuple[int] = (0, 0), angle: float = 0, magnitude: float = 100,
            thickness: int = 1, color: Tuple[int] = (255, 255, 255, 255)):
        """
        Initializes line from vector.
        :param origin: The origin of line.
        :param angle: The direction line is pointing to (degrees).
        :param magnitude: The distance of line.
        :param thickness: The thickness of line.
        :param color: Color (rgba, 0 to 255) of line. The ALPHA will be set to 255 if no alpha is given.
        """
        loc1 = origin
        x_off = cos(radians(-angle)) * magnitude
        y_off = sin(radians(-angle)) * magnitude
        loc2 = (loc1[0] + x_off, loc1[1] + y_off)
        return cls(loc1, loc2, thickness, color)

    def render_raw(self, res: Tuple[int], frame: int) -> pygame.Surface:
        surface = pygame.Surface(res, pygame.SRCALPHA)

        loc1 = self.loc1(frame)
        loc2 = self.loc2(frame)
        thickness = self.thickness(frame)
        color = self.color(frame)
        antialias = self.antialias(frame)

        if antialias:
            gfxdraw.line(surface, *loc1, *loc2, color)
        else:
            pygame.draw.line(surface, color, loc1, loc2, thickness)

        return surface


class Arc(BaseElement):
    """Arc element."""

    loc: VectorProp
    size: VectorProp
    start_angle: FloatProp
    stop_angle: FloatProp
    color: VectorProp
    border: IntProp
    border_color: VectorProp
    antialias: BoolProp

    def __init__(self, loc: Tuple[int] = (0, 0), size: Tuple[int] = (100, 100), start_angle: float = 0, stop_angle: float = 1.57,
            border: int = 0, color: Tuple[int] = (255, 255, 255), antialias: bool = True) -> None:
        """
        Initializes arc.
        :param loc: Top left corner location (pixels) of arc.
        :param size: Size (x, y) pixels of arc.
        :param start_angle: Start angle of the arc in radians.
        :param stop_angle: Stop angle of the arc in radians.
        :param color: Color (rgba, 0 to 255) of arc. The ALPHA will be set to 255 if no alpha is given.
        :param border: Border width (pixels) of arc. Set to 0 to disable border.
        :param antialias: Whether to perform simple antialiasing when rendering.
        """
        super().__init__()
        color = get_color(color)
        if len(color) == 3:
            color = (*color, 255)

        self.loc = VectorProp(2, IntProp, loc)
        self.size = VectorProp(2, IntProp, size)
        self.start_angle = FloatProp(start_angle)
        self.stop_angle = FloatProp(stop_angle)
        self.border = IntProp(border)
        self.color = VectorProp(4, IntProp, color)
        self.antialias = BoolProp(antialias)

    def render_raw(self, res: Tuple[int], frame: int) -> pygame.Surface:
        surface = pygame.Surface(res, pygame.SRCALPHA)

        loc = self.loc(frame)
        size = self.size(frame)
        start_angle = self.start_angle(frame)
        stop_angle = self.stop_angle(frame)
        border = self.border(frame)
        color = self.color(frame)
        antialias = self.antialias(frame)

        pygame.draw.arc(surface, color, loc+size, start_angle, stop_angle, border)

        return surface


class Arrow(BaseElement):
    """Arrow pointer element."""

    loc1: VectorProp
    loc2: VectorProp
    stem_width: IntProp
    head_width: IntProp
    head_length: IntProp
    color: VectorProp

    def __init__(self, loc1: Tuple[int] = (0, 0), loc2: Tuple[int] = (50, 50), stem_width: int = 20, head_width: int = 50,
            head_length: int = 25, color: Tuple[int] = (255, 255, 255, 255)) -> None:
        """
        Initializes arrow.
        :param loc1: The origin of arrow.
        :param loc2: The end point of arrow (where arrow is pointing).
        :param stem_width: The width of the base of arrow.
        :param head_width: The width of the top of arrow.
        :param head_length: The length of the top of arrow.
        :param color: Color (rgba, 0 to 255) of arrow. The ALPHA will be set to 255 if no alpha is given.
        """
        super().__init__()
        self.loc1 = VectorProp(2, IntProp, loc1)
        self.loc2 = VectorProp(2, IntProp, loc2)
        self.stem_width = IntProp(stem_width)
        self.head_width = IntProp(head_width)
        self.head_length = IntProp(head_length)
        self.color = VectorProp(4, IntProp, color)

    @classmethod
    def from_vector(cls, origin: Tuple[int] = (0, 0), angle: float = 0, magnitude: float = 100, stem_width: int = 20,
            head_width: int = 50, head_length: int = 25, color: Tuple[int] = (255, 255, 255, 255)):
        """
        Initializes arrow from vector.
        :param origin: The origin of arrow.
        :param angle: The direction arrow is pointing to (degrees).
        :param magnitude: The distance of arrow.
        :param stem_width: The width of the base of arrow.
        :param head_width: The width of the top of arrow.
        :param head_length: The length of the top of arrow.
        :param color: Color (rgba, 0 to 255) of arrow. The ALPHA will be set to 255 if no alpha is given.
        """
        loc1 = origin
        x_off = cos(radians(-angle)) * magnitude
        y_off = sin(radians(-angle)) * magnitude
        loc2 = (loc1[0] + x_off, loc1[1] + y_off)
        return cls(loc1, loc2, stem_width, head_width, head_length, color)

    @staticmethod
    def dist(loc1, loc2):
        return sqrt((loc1[0]-loc2[0])**2 + (loc1[1]-loc2[1])**2)

    @staticmethod
    def walk(point, angle, dist):
        angle = radians(angle)

        x_diff = dist * cos(angle)
        y_diff = dist * sin(angle)

        return (point[0]+x_diff, point[1]+y_diff)

    @staticmethod
    def get_verts(loc1, loc2, stem_width, head_width, head_length):
        (x1, y1), (x2, y2) = loc1, loc2
        dist = Arrow.dist(loc1, loc2)
        if (dx := x2 - x1) == 0:
            angle = 90 if y2-y1 > 0 else -90
        else:
            angle = degrees(atan((y2-y1)/dx))
            if angle < 0:
                angle += 180

        p1 = Arrow.walk(loc1, angle+90, stem_width//2)
        p2 = Arrow.walk(p1, angle, dist-head_length)
        p3 = Arrow.walk(p2, angle+90, (head_width-stem_width)//2)
        p4 = loc2
        p7 = Arrow.walk(loc1, angle-90, stem_width//2)
        p6 = Arrow.walk(p7, angle, dist-head_length)
        p5 = Arrow.walk(p6, angle-90, (head_width-stem_width)//2)

        return [p1, p2, p3, p4, p5, p6, p7]

    def render_raw(self, res: Tuple[int], frame: int) -> pygame.Surface:
        surface = pygame.Surface(res, pygame.SRCALPHA)

        loc1 = self.loc1(frame)
        loc2 = self.loc2(frame)
        stem_width = self.stem_width(frame)
        head_width = self.head_width(frame)
        head_length = self.head_length(frame)
        color = self.color(frame)

        verts = Arrow.get_verts(loc1, loc2, stem_width, head_width, head_length)
        pygame.draw.polygon(surface, color, verts)

        return surface


class Text(BaseElement):
    """Text element."""

    loc: VectorProp
    color: VectorProp
    font: StringProp
    text: StringProp
    size: IntProp
    bold: BoolProp
    italic: BoolProp
    antialias: BoolProp

    def __init__(self, loc: Tuple[int] = (0, 0), color: Tuple[int] = (255, 255, 255), font: str = None,
            text: str = "Text", size: int = 36, bold: bool = False, italic: bool = False, antialias: bool = True) -> None:
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
        color = get_color(color)
        if len(color) == 3:
            color = (*color, 255)
        if font is None:
            font = get_font()

        self.loc = VectorProp(2, IntProp, loc)
        self.color = VectorProp(4, IntProp, color)
        self.font = StringProp(font)
        self.text = StringProp(text)
        self.size = IntProp(size)
        self.bold = BoolProp(bold)
        self.italic = BoolProp(italic)
        self.antialias = BoolProp(antialias)

    def get_font(self, frame):
        font_family = self.font(frame)
        font_size = self.size(frame)

        if os.path.isfile(font_family):
            return pygame.font.Font(font_family, font_size)
        else:
            bold = self.bold(frame)
            italic = self.italic(frame)
            return pygame.font.SysFont(font_family, font_size, bold, italic)

    def get_size(self, frame: int = 0) -> Tuple[int]:
        font_family = self.font(frame)
        text_str = self.text(frame)
        size = self.size(frame)

        font = pygame.font.SysFont(font_family, size)
        text = font.render(text_str, True, (0, 0, 0))

        return text.get_size()

    def render_raw(self, res: Tuple[int], frame: int) -> pygame.Surface:
        surface = pygame.Surface(res, pygame.SRCALPHA)

        loc = self.loc(frame)
        color = self.color(frame)
        text_str = self.text(frame)
        antialias = self.antialias(frame)

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
        src = self.src(frame)
        if src == self.last_src:
            return self.last_img

        image = pygame.image.load(src)
        self.last_src = src
        self.last_img = image

        return image

    def render_raw(self, res: Tuple[int], frame: int) -> pygame.Surface:
        surface = pygame.Surface(res, pygame.SRCALPHA)

        loc = self.loc(frame)
        size = self.size(frame)

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

    def render_raw(self, res: Tuple[int], frame: int) -> pygame.Surface:
        surface = pygame.Surface(res, pygame.SRCALPHA)

        loc = self.loc(frame)
        size = self.size(frame)
        surf = self.get_surf(frame*self.speed-self.offset)

        surf = pygame.transform.scale(surf, size)
        surface.blit(surf, loc)

        return surface


class NewVideo(BaseElement):
    """
    Improved video element.
    todo change class name after testing
    """

    loc: VectorProp
    size: VectorProp
    src: str
    length: int
    speed: float
    offset: float
    max_cache: int

    def __init__(self, loc: Tuple[int] = (0, 0), size: Tuple[int] = (1920, 1080), src: str = "", speed: float = 1,
            offset: float = 0, max_cache: int = 0, cache_verbose: bool = True) -> None:
        super().__init__()

        self.loc = VectorProp(2, IntProp, loc)
        self.size = VectorProp(2, IntProp, size)
        self.src = src
        self.speed = speed
        self.offset = offset
        self.max_cache = max_cache

        self.cache(cache_verbose)

    def rm_cache(self):
        if self.cache_path.startswith(get_parent()):
            shutil.rmtree(self.cache_path)

    def cache(self, verbose):
        base_dir = os.path.join(get_parent(), ".videocache")
        get_path = lambda: os.path.join(base_dir, sha256(str(time.time()).encode()).hexdigest()[:20])
        path = get_path()
        while os.path.isdir(path):
            path = get_path()

        self.cache_path = path
        os.makedirs(self.cache_path)
        atexit.register(self.rm_cache)

        video = cv2.VideoCapture(self.src)
        self.length = 0
        while self.max_cache == 0 or self.length < self.max_cache:
            if verbose:
                printer.clearline()
                printer.write(f"[GRAPHICS] Video cache: {os.path.basename(self.src)}: Frame {self.length}")
            rval, frame = video.read()
            if not rval:
                break

            path = os.path.join(self.cache_path, f"{self.length}.png")
            cv2.imwrite(path, frame)
            self.length += 1

        printer.clearline()
        printer.write(f"[GRAPHICS] Video cache: {os.path.basename(self.src)}: Finished, {self.length} frames")
        printer.newline()

    def get_frame(self, frame):
        path = os.path.join(self.cache_path, f"{frame}.png")
        surf = pygame.image.load(path)
        return surf

    def render_raw(self, res: Tuple[int], frame: int) -> pygame.Surface:
        surface = pygame.Surface(res, pygame.SRCALPHA)

        loc = self.loc(frame)
        size = self.size(frame)
        video_frame = int(frame*self.speed + self.offset)

        image = self.get_frame(video_frame)
        image = pygame.transform.scale(image, size)
        surface.blit(image, loc)

        return surface
