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
from .elements import FrameText, Slider
from ..options import get_font
pygame.init()

FPS = 60


def launch(resolution: Tuple[int], scenes: Tuple[Scene], resizable: bool = True) -> None:
    clock = pygame.time.Clock()
    width, height = 1600, 900
    flags = pygame.RESIZABLE if resizable else 0
    window = pygame.display.set_mode((width, height), flags)
    pygame.display.set_caption("Graphic Videos - Preview")
    frame_text = FrameText()
    frame_text.text = "0"
    slider = Slider(0, (0, sum([len(s.get_frames()) for s in scenes])))
    resized = playing = False
    curr_frame = 0
    bottom_bar_height = 25

    while True:
        clock.tick(FPS)
        window.fill((0, 0, 0))
        events = pygame.event.get()
        font = pygame.font.SysFont(get_font(), bottom_bar_height-5)
        text_size = font.size("Frame: " + frame_text.text + "9"*(5-len(frame_text.text)))
        frame_text.draw(window, events, width, height, text_size, font)
        if slider.update(window, events, width, height, width-text_size[0]-15, bottom_bar_height) or slider.dragging or playing:
            curr_frame = slider.value
            frame_text.text = str(curr_frame)

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.K_SPACE:
                playing = not playing

            if resizable:
                if event.type == pygame.VIDEORESIZE:
                    resized = True
                    width, height = event.size

                elif event.type == pygame.ACTIVEEVENT and resized:
                    window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                    resized = False


        pygame.display.update()
