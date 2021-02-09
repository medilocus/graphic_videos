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
from ..props import *
import random
pygame.init()


class BarGraphVert:
    """Vertical Bar Graph element."""

    loc: VectorProp
    size: VectorProp
    categories: Tuple[StringProp]
    values: Tuple[IntProp]
    colors: Tuple[VectorProp]
    border: IntProp
    border_color: VectorProp

    def __init__(self, loc: Tuple[int], size: Tuple[int], categories: Tuple[str], values: Tuple[int], colors: Tuple[Tuple[int]] = None, border: int = 4, border_color: int = (0, 0, 0)):
        """
        Initializes vertical bar graph.
        :param loc: Top left corner location (pixels) of vertical bar graph.
        :param size: Size (x, y) pixels of vertical bar graph.
        :param categories: The name of each category of vertical bar graph. This will be a column.
        :param values: The initializing values for each category.
        :param colors: Colors (rgba, 0 to 255) of each choice of vertical bar graph. The ALPHA will be set to 255 if no alpha is given. None will make all colors random.
        :param border: Border width (pixels) of the axes of vertical bar graph.
        :param border_color: Border color of vertical bar graph.
        """
        if colors is None:
            colors = [VectorProp(4, IntProp, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(1, 255))) for _ in range(len(categories))]
        else:
            colors = [VectorProp(4, IntProp, (*colors[i], 255) if len(colors[i]) == 3 else colors[i]) for i in range(len(colors))]
        if not (len(categories) == len(values) == len(colors)):
            raise ValueError(f"The length of categories ({len(categories)}) must be equal to the length of values ({len(values)}) as well as the length of colors ({len(self.colors)})")
        self.colors = colors
        self.loc = VectorProp(2, IntProp, loc)
        self.size = VectorProp(2, IntProp, size)
        self.categories = [StringProp(categories[i]) for i in range(len(categories))]
        self.values = [IntProp(values[i]) for i in range(len(values))]
        self.border = IntProp(border)
        self.border_color = VectorProp(2, IntProp, border_color)

    def render(self, res: Tuple[int], frame: int):
        surf = pygame.Surface(res, pygame.SRCALPHA)
        font = pygame.font.SysFont(DEFAULT_FONT, 20)
        surf.fill((0, 0, 0, 0))
        base_x, base_y = self.loc.get_value(frame)
        width, height = self.size.get_value(frame)
        gap = (width - 100 - len(self.categories) * 5) // len(self.categories)
        for i in range(len(self.categories)):
            color = self.colors[i].get_value(frame)
            x = 5 + 100 + gap*i + i*5 + base_x
            y = height - 5 - 100 - self.values[i] + base_y
            pygame.draw.rect(surf, color, (x, y, gap, self.values[i]))
            text = font.render(self.categories[i], 1, self.border_color)
            surf.blit(text, (x + gap // 2 - text.get_width() // 2, height - 5 - 100 + 10))
            text = font.render(str(self.values[i]), 1, self.border_color)
            surf.blit(text, (x + gap // 2 - text.get_width() // 2, y // 2 - text.get_height() // 2))

        pygame.draw.rect(surf, self.border_color,(100 + base_x, 0 + base_y, 5, height - 100))
        pygame.draw.rect(surf, self.border_color, (100 + base_x, height - 5 - 100 + base_y, width - 100, 5))
