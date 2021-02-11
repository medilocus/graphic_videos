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
from ..scene import Scene
from ..options import get_font
from .elements import FrameText
pygame.init()

FPS = 60

def launch(resolution: Tuple[int], scenes: Tuple[Scene]) -> None:
    clock = pygame.time.Clock()
    width, height = 1600, 900
    window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    frame_text = FrameText()
    resized = False
    playing = False
    curr_frame = 0

    while True:
        clock.tick(FPS)
        window.fill((0, 0, 0))
        events = pygame.event.get()
        frame_text.draw(window, events, width, height)
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.VIDEORESIZE:
                resized = True
                width, height = event.size

            elif event.type == pygame.ACTIVEEVENT and resized:
                window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                resized = False

        pygame.display.update()
