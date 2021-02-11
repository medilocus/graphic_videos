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
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
import pygame
from .props import *
pygame.init()


class Modifier:
    """Base modifier class. Other modifiers should inherit from this."""

    show: BoolProp

    def __init__(self) -> None:
        self.show = BoolProp(True)

    def modify(self, src: pygame.Surface, frame: int) -> pygame.Surface:...


class ModFlip(Modifier):
    """Flips the surface along x or y or both axes."""

    x: BoolProp
    y: BoolProp

    def __init__(self, x: bool, y: bool) -> None:
        """
        Initializes modifier.
        :param x: Flip on x axis?
        :param y: Flip on y axis?
        """
        super().__init__()
        self.x = BoolProp(x)
        self.y = BoolProp(y)

    def modify(self, src: pygame.Surface, frame: int) -> pygame.Surface:
        x = self.x.get_value(frame)
        y = self.y.get_value(frame)
        src = pygame.transform.flip(src, x, y)
        return src


class ModHsva(Modifier):
    """Changes surface HSVA."""

    def __init__(self) -> None:
        """
        Initializes modifier.
        """
        super().__init__()

    def modify(self, src: pygame.Surface, frame: int) -> pygame.Surface:
        surf = pygame.surfarray.pixels3d(src).swapaxes(1, 0)
        img = Image.fromarray(surf).convert("HSV")
        data = (img.tobytes(), img.size, "RGB")
        return pygame.image.fromstring(*data)


class ModGaussianBlur(Modifier):
    """Blurs the surface using Gaussian Blur"""

    radius: FloatProp

    def __init__(self, radius: float = 4) -> None:
        """
        Initializes modifier.
        :param radius: Radius of blurring
        """
        super().__init__()
        self.radius = FloatProp(radius)

    def modify(self, src: pygame.Surface, frame: int) -> pygame.Surface:
        surf = pygame.surfarray.pixels3d(src).swapaxes(1, 0)
        img = Image.fromarray(surf).filter(ImageFilter.GaussianBlur(self.radius.get_value(frame)))
        data = (img.tobytes(), img.size, img.mode)
        return pygame.image.fromstring(*data)


class ModGrayscale(Modifier):
    """Converts the surface into grayscale"""

    def __init__(self) -> None:
        """
        Initializes modifier.
        """
        super().__init__()

    def modify(self, src: pygame.Surface, frame: int) -> pygame.Surface:
        super().__init__()
        surf = np.dstack((np.resize(pygame.surfarray.array3d(src), (*src.get_size(), 3)), np.ones(src.get_size())))
        arr = surf.dot([0.216, 0.587, 0.144, 1])[..., np.newaxis].repeat(3, 2)
        return pygame.surfarray.make_surface(arr)


class ModBright(Modifier):
    """Brightens the surface by a factor"""

    factor: FloatProp

    def __init__(self, factor: float = 4) -> None:
        """
        Initializes modifier.
        :param factor: Factor of brightness
        """
        super().__init__()
        self.factor = FloatProp(factor)

    def modify(self, src: pygame.Surface, frame: int) -> pygame.Surface:
        surf = pygame.surfarray.pixels3d(src).swapaxes(1, 0)
        img = ImageEnhance.Brightness(Image.fromarray(surf)).enhance(self.factor.get_value(frame))
        data = (img.tobytes(), img.size, img.mode)
        return pygame.image.fromstring(*data)


class ModContrast(Modifier):
    """Manipulates the contrast of the surface"""

    factor: FloatProp

    def __init__(self, factor: float = 4) -> None:
        """
        Initializes modifier.
        :param factor: Factor of contrast
        """
        super().__init__()
        self.factor = FloatProp(factor)

    def modify(self, src: pygame.Surface, frame: int) -> pygame.Surface:
        surf = pygame.surfarray.pixels3d(src).swapaxes(1, 0)
        img = ImageEnhance.Contrast(Image.fromarray(surf)).enhance(self.factor.get_value(frame))
        data = (img.tobytes(), img.size, img.mode)
        return pygame.image.fromstring(*data)


class ModColorEnhance(Modifier):
    """Enhances color of surface"""

    factor: FloatProp

    def __init__(self, factor: float = 4) -> None:
        """
        Initializes modifier.
        :param factor: Factor of color enhancement
        """
        super().__init__()
        self.factor = FloatProp(factor)

    def modify(self, src: pygame.Surface, frame: int) -> pygame.Surface:
        surf = pygame.surfarray.pixels3d(src).swapaxes(1, 0)
        img = ImageEnhance.Color(Image.fromarray(surf)).enhance(self.factor.get_value(frame))
        data = (img.tobytes(), img.size, img.mode)
        return pygame.image.fromstring(*data)


class ModSharpen(Modifier):
    """Sharpens color of surface"""

    factor: FloatProp

    def __init__(self, factor: float = 4) -> None:
        """
        Initializes modifier.
        :param factor: Factor of sharpness
        """
        self.factor = FloatProp(factor)

    def modify(self, src: pygame.Surface, frame: int) -> pygame.Surface:
        pass
