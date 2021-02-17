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

import time
import pygame
from constants import *
pygame.init()


def main():
    pygame.display.set_caption("Graphic Videos - GUI")
    surface = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

    clock = pygame.time.Clock()
    width, height = 1280, 720
    last_width, last_height = 1280, 720
    resized = False

    while True:
        clock.tick(FPS)
        pygame.display.update()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.init()
                return

            elif event.type == pygame.VIDEORESIZE:
                last_width, last_height = width, height
                width, height = event.w, event.h
                resized = True

            elif event.type == pygame.ACTIVEEVENT and resized and width != last_width and height != last_height:
                surface = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                resized = False

        surface.fill(BLACK)


main()
