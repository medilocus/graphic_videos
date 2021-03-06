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
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import numpy as np
import pygame
from .props import *
pygame.init()


class Modifier:
    """Base modifier class. Other modifiers should inherit from this."""

    show: BoolProp

    def __init__(self) -> None:
        """
        Initializes base modifier. Inherited classes should have their own init
        and call super().__init__()
        """
        self.show = BoolProp(True)

    def modify(self, src: pygame.Surface, frame: int) -> pygame.Surface:
        #alpha = pygame.surfarray.array_alpha(src)
        non_alpha = pygame.Surface(src.get_size())
        non_alpha.blit(src, (0, 0))
        result = self.modify_raw(non_alpha, frame)
        #result = pygame.surfarray.array3d(result)
        #result = np.dstack((result, alpha)).swapaxes(1, 0).tostring()
        #surf = pygame.image.fromstring(result, src.get_size(), "RGBA")
        return result

    def modify_raw(self, src: pygame.Surface, frame: int) -> pygame.Surface:...


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

    def modify_raw(self, src: pygame.Surface, frame: int) -> pygame.Surface:
        x = self.x(frame)
        y = self.y(frame)
        src = pygame.transform.flip(src, x, y)
        return src


class ModMixSolidColor(Modifier):
    """Mixes surface with a solid color."""

    color: VectorProp
    fac: FloatProp

    def __init__(self, color: Tuple[int] = (0, 0, 0, 0), fac: float = 0.5):
        super().__init__()
        self.color = VectorProp(4, IntProp, color)
        self.fac = FloatProp(fac)

    def modify_raw(self, src: pygame.Surface, frame: int) -> pygame.Surface:
        color = self.color(frame)
        fac = self.fac(frame)
        color[3] = int(fac*color[3])

        surf = pygame.Surface(src.get_size())
        color_surf = pygame.Surface(src.get_size(), pygame.SRCALPHA)
        color_surf.fill(color)
        surf.blit(src, (0, 0))
        surf.blit(color_surf, (0, 0))

        return surf


class ModHsva(Modifier):
    """Changes surface HSVA."""

    def __init__(self) -> None:
        """
        Initializes modifier.
        """
        super().__init__()

    def modify_raw(self, src: pygame.Surface, frame: int) -> pygame.Surface:
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

    def modify_raw(self, src: pygame.Surface, frame: int) -> pygame.Surface:
        surf = pygame.surfarray.pixels3d(src).swapaxes(1, 0)
        img = Image.fromarray(surf).filter(ImageFilter.GaussianBlur(self.radius(frame)))
        data = (img.tobytes(), img.size, img.mode)
        return pygame.image.fromstring(*data)


class ModGrayscale(Modifier):
    """Converts the surface into grayscale"""

    def __init__(self) -> None:
        """
        Initializes modifier.
        """
        super().__init__()

    def modify_raw(self, src: pygame.Surface, frame: int) -> pygame.Surface:
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

    def modify_raw(self, src: pygame.Surface, frame: int) -> pygame.Surface:
        surf = pygame.surfarray.pixels3d(src).swapaxes(1, 0)
        img = ImageEnhance.Brightness(Image.fromarray(surf)).enhance(self.factor(frame))
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

    def modify_raw(self, src: pygame.Surface, frame: int) -> pygame.Surface:
        surf = pygame.surfarray.pixels3d(src).swapaxes(1, 0)
        img = ImageEnhance.Contrast(Image.fromarray(surf)).enhance(self.factor(frame))
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

    def modify_raw(self, src: pygame.Surface, frame: int) -> pygame.Surface:
        surf = pygame.surfarray.pixels3d(src).swapaxes(1, 0)
        img = ImageEnhance.Color(Image.fromarray(surf)).enhance(self.factor(frame))
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
        super().__init__()
        self.factor = FloatProp(factor)

    def modify_raw(self, src: pygame.Surface, frame: int) -> pygame.Surface:
        surf = pygame.surfarray.pixels3d(src).swapaxes(1, 0)
        img = ImageEnhance.Sharpness(Image.fromarray(surf)).enhance(self.factor(frame))
        data = (img.tobytes(), img.size, img.mode)
        return pygame.image.fromstring(*data)


class ModInvert(Modifier):
    """Inverts surface"""

    def __init__(self) -> None:
        """
        Initializes modifier
        """
        super().__init__()

    def modify_raw(self, src: pygame.Surface, frame: int) -> pygame.Surface:
        surf = pygame.surfarray.pixels3d(src).swapaxes(1, 0)
        img = ImageOps.invert(Image.fromarray(surf))
        data = (img.tobytes(), img.size, img.mode)
        return pygame.image.fromstring(*data)
