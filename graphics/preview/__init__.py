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


def draw_current(res, scenes, frame, image):
    image.fill((0, 0, 0, 0))
    for scene in scenes:
        if frame in scene.get_frames():
            image.blit(scene.render(res, frame), (0, 0))


def launch(resolution: Tuple[int], fps, scenes: Tuple[Scene], resizable: bool = True) -> None:
    clock = pygame.time.Clock()
    width, height = 1600, 900
    last_width, last_height = 1280, 720
    flags = pygame.RESIZABLE if resizable else 0
    window = pygame.display.set_mode((width, height), flags)
    pygame.display.set_caption("Graphic Videos - Preview")
    frame_text = FrameText()
    frame_text.text = "0"
    frames = set([f for s in scenes for f in s.get_frames()])
    end = max(frames)
    slider = Slider(min(frames), (min(frames), end))
    resized = playing = False
    bottom_bar_height = 30
    image = pygame.Surface(resolution, pygame.SRCALPHA)
    draw_current(resolution, scenes, slider.value, image)

    while True:
        clock.tick(fps)
        window.fill((0, 0, 0))
        events = pygame.event.get()
        font = pygame.font.SysFont(get_font(), bottom_bar_height-5)
        text_size = font.size("Frame: " + frame_text.text + "9"*(5-len(frame_text.text)))
        draw_frame = lambda: draw_current(resolution, scenes, slider.value, image)
        if frame_text.draw(window, events, width, height, text_size, font):
            slider.set(int(frame_text.text))
            frame_text.text = str(slider.value)
            draw_frame()
        if slider.update(window, events, width, height, width-text_size[0]-15, bottom_bar_height-5) or slider.dragging or playing:
            frame_text.text = str(slider.value)
            draw_frame()
            if playing:
                slider.set(slider.value + 1)

        window.blit(pygame.transform.scale(image, (width, height-bottom_bar_height-5)), (0, 0))

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pygame.mouse.get_pos()[1] < height - bottom_bar_height:
                        playing = not playing

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing
                    if playing and slider.value == end:
                        slider.set(slider.range[0])
                
                elif event.key == pygame.K_LEFT:
                    slider.set(slider.value - 1)
                    frame_text.text = str(slider.value)
                    draw_frame()
                
                elif event.key == pygame.K_RIGHT:
                    slider.set(slider.value + 1)
                    frame_text.text = str(slider.value)
                    draw_frame()

            if resizable:
                if event.type == pygame.VIDEORESIZE:
                    resized = True
                    draw_frame()
                    last_width, last_height = width, height
                    width, height = event.size
                    resized = True

                elif event.type == pygame.ACTIVEEVENT and resized and width != last_width and height != last_height:
                    window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                    resized = False

        if playing and slider.value == end:
            playing = False

        pygame.display.update()
