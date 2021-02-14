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
import numpy as np
from . import BaseElement
from ..props import *
from ..options import *
import random
pygame.init()


class BarGraphVert(BaseElement):
    """Vertical Bar Graph element."""

    loc: VectorProp
    size: VectorProp
    categories: Tuple[StringProp]
    values: Tuple[IntProp]
    text_color: VectorProp
    colors: Tuple[VectorProp]
    border: IntProp
    border_color: VectorProp

    def __init__(self, loc: Tuple[int] = (0, 0), size: Tuple[int] = (200, 200), categories: Tuple[str] = ("a", "b"),
            values: Tuple[int] = (1, 2), text_color: Tuple[int] = "AUTO", colors: Tuple[Tuple[int]] = "AUTO", border: int = 4,
            border_color: int = (0, 0, 0, 255)) -> None:
        """
        Initializes vertical bar graph.
        :param loc: Top left corner location (pixels) of vertical bar graph.
        :param size: Size (x, y) pixels of vertical bar graph.
        :param categories: The name of each category of vertical bar graph. This will be a column.
        :param values: The initializing values for each category.
        :param text_color: The color of the text on a bar, as well as the color on the axis. If it is set to auto, the text color for the axis would be black, and it will choose between black and white for the text color on the bar depending on the color of the bar. NOTE: Auto doesn't have transparency.
        :param colors: Colors (rgba, 0 to 255) of each choice of vertical bar graph. The ALPHA will be set to 255 if no alpha is given. Auto will make all colors random.
        :param border: Border width (pixels) of the axes of vertical bar graph.
        :param border_color: Border color of vertical bar graph.
        """
        super().__init__()
        if isinstance(colors, str) and colors.lower() == "auto":
            colors = [VectorProp(4, IntProp, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(1, 255))) for _ in range(len(categories))]
        else:
            colors = [VectorProp(4, IntProp, (*get_color(colors[i]), 255) if len(get_color(colors[i])) == 3 else get_color(colors[i])) for i in range(len(colors))]
        if not (len(categories) == len(values) == len(colors)):
            raise ValueError(f"The length of categories ({len(categories)}) must be equal to the length of values ({len(values)}) as well as the length of colors ({len(self.colors)})")
        self.colors = colors
        self.loc = VectorProp(2, IntProp, loc)
        self.size = VectorProp(2, IntProp, size)
        self.categories = [StringProp(categories[i]) for i in range(len(categories))]
        self.values = [IntProp(values[i]) for i in range(len(values))]
        if isinstance(text_color, str):
            self.text_color = StringProp(text_color.upper())
        else:
            self.text_color = VectorProp(4, IntProp, text_color)
        self.border = IntProp(border)
        self.border_color = VectorProp(4, IntProp, border_color)

    def render(self, res: Tuple[int], frame: int) -> pygame.Surface:
        # Initialize surface
        surf = pygame.Surface(res, pygame.SRCALPHA)
        font = pygame.font.SysFont(get_font(), 20)
        surf.fill((0, 0, 0, 0))

        # Get current values
        base_x, base_y = self.loc.get_value(frame)
        width, height = self.size.get_value(frame)
        border = self.border.get_value(frame)
        border_color = self.border_color.get_value(frame)
        text_color = self.text_color.get_value(frame)
        gap = (width - 5 - len(self.categories) * 5) // len(self.categories)

        # Draw bars and text for each bar
        for i in range(len(self.categories)):
            # Get values for bar
            color = self.colors[i].get_value(frame)
            value = self.values[i].get_value(frame)
            category = self.categories[i].get_value(frame)
            val_h = np.interp(value, (0, max(self.values, key=lambda val: val.get_value(frame)).get_value(frame) + 1), (3, height - 100 - 5))

            # Calculate x and y for bar
            x = 5 + gap*i + i*5 + base_x
            y = height - 5 - 50 - val_h + base_y

            # Draw bar
            pygame.draw.rect(surf, color, (x, y, gap, val_h))

            # Set text color for category text
            if text_color == "AUTO":
                text_color = (0,)*3
            # Create text
            text = font.render(category, 1, text_color)
            # Draw text
            surf.blit(text, (x + gap // 2 - text.get_width() // 2, height - 5 - 50 + 10))
            # Set text color for value text
            if text_color == "AUTO" and sum(color) < 120:
                text_color = (255,)*3
            # Create text
            text = font.render(str(value), 1, text_color)
            # Draw text
            surf.blit(text, (x + gap // 2 - text.get_width() // 2, y + val_h//2 - text.get_height() // 2))

        # Draw graph borders
        pygame.draw.rect(surf, border_color, (base_x, 0 + base_y, border, height - 50))
        pygame.draw.rect(surf, border_color, (base_x, height - border - 50 + base_y, width, border))

        return surf


class BarGraphHoriz(BaseElement):
    """Horizontal Bar Graph element."""

    loc: VectorProp
    size: VectorProp
    categories: Tuple[StringProp]
    values: Tuple[IntProp]
    text_color: VectorProp
    colors: Tuple[VectorProp]
    border: IntProp
    border_color: VectorProp

    def __init__(self, loc: Tuple[int] = (0, 0), size: Tuple[int] = (200, 200), categories: Tuple[str] = ("a", "b"),
            values: Tuple[int] = (1, 2), text_color: Tuple[int] = "AUTO", colors: Tuple[Tuple[int]] = "AUTO",
            border: int = 4, border_color: int = (0, 0, 0, 255)):
        """
        Initializes horizontal bar graph.
        :param loc: Top left corner location (pixels) of horizontal bar graph.
        :param size: Size (x, y) pixels of horizontal bar graph.
        :param categories: The name of each category of horizontal bar graph. This will be a column.
        :param values: The initializing values for each category.
        :param text_color: The color of the text on a bar, as well as the color on the axis. If it is set to auto, the text color for the axis would be black, and it will choose between black and white for the text color on the bar depending on the color of the bar. NOTE: Auto doesn't have transparency.
        :param colors: Colors (rgba, 0 to 255) of each choice of horizontal bar graph. The ALPHA will be set to 255 if no alpha is given. Auto will make all colors random.
        :param border: Border width (pixels) of the axes of horizontal bar graph.
        :param border_color: Border color of horizontal bar graph.
        """
        super().__init__()
        if isinstance(colors, str) and colors.lower() == "auto":
            colors = [VectorProp(4, IntProp, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(1, 255))) for _ in range(len(categories))]
        else:
            colors = [VectorProp(4, IntProp, (*get_color(colors[i]), 255) if len(get_color(colors[i])) == 3 else get_color(colors[i])) for i in range(len(colors))]
        if not (len(categories) == len(values) == len(colors)):
            raise ValueError(f"The length of categories ({len(categories)}) must be equal to the length of values ({len(values)}) as well as the length of colors ({len(self.colors)})")
        self.colors = colors
        self.loc = VectorProp(2, IntProp, loc)
        self.size = VectorProp(2, IntProp, size)
        self.categories = [StringProp(categories[i]) for i in range(len(categories))]
        self.values = [IntProp(values[i]) for i in range(len(values))]
        if isinstance(text_color, str):
            self.text_color = StringProp(text_color.upper())
        else:
            self.text_color = VectorProp(4, IntProp, text_color)
        self.border = IntProp(border)
        self.border_color = VectorProp(4, IntProp, border_color)

    def render(self, res: Tuple[int], frame: int) -> pygame.Surface:
        # Initialize surface
        surf = pygame.Surface(res, pygame.SRCALPHA)
        font = pygame.font.SysFont(get_font(), 20)
        surf.fill((0, 0, 0, 0))

        # Get current values
        base_x, base_y = self.loc.get_value(frame)
        width, height = self.size.get_value(frame)
        border = self.border.get_value(frame)
        border_color = self.border_color.get_value(frame)
        text_color = self.text_color.get_value(frame)
        gap = (height - 5 - len(self.categories) * 5) // len(self.categories)

        # Draw bars and text for each bar
        for i in range(len(self.categories)):
            # Get values for bar
            color = self.colors[i].get_value(frame)
            value = self.values[i].get_value(frame)
            category = self.categories[i].get_value(frame)
            val_w = np.interp(value, (0, max(self.values, key=lambda val: val.get_value(frame)).get_value(frame) + 1), (3, height - 100 - 5))

            # Calculate x and y for bar
            x = 5 + 50 + base_x
            y = (gap + 5)*i + base_y

            # Draw bar
            pygame.draw.rect(surf, color, (x, y, val_w, gap))

            # Set text color for category text
            if text_color == "AUTO":
                text_color = (0,)*3
            # Create text
            text = font.render(category, 1, text_color)
            # Draw text
            surf.blit(text, (x - 10 - text.get_width(), y + gap // 2 - text.get_height() // 2))
            # Set text color for value text
            if text_color == "AUTO" and sum(color) < 120:
                text_color = (255,)*3
            # Create text
            text = font.render(str(value), 1, text_color)
            # Draw text
            surf.blit(text, (x + val_w // 2 - text.get_width() // 2, y + gap // 2 - text.get_height() // 2))

        # Draw graph borders
        pygame.draw.rect(surf, border_color, (base_x + 50, base_y, border, height))
        pygame.draw.rect(surf, border_color, (base_x + 50, height - border + base_y, width, border))

        return surf
