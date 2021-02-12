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

import random
import colorsys
import pygame
import graphics
pygame.init()

scene = graphics.Scene(0, 1, before_pause=0, after_pause=0)

for x in range(4):
    for y in range(4):
        if y == 0:
            hidden = random.random() > 0.5
        elif y == 1:
            hidden = random.random() > 0.75
        elif y == 2:
            hidden = random.random() > 0.85
        else:
            hidden = False

        if not hidden:
            loc = (x*256, y*256)
            color = colorsys.hsv_to_rgb((x+y)/12, 0.8, 0.9)
            color = [255*x for x in color]
            rect = graphics.elements.simple.Rect((loc[0]+16, loc[1]+16), (224, 224), color)
            scene.add_element(rect)

img = scene.render((1024, 1024), 0)

for res in (1024, 256, 64, 32):
    for ftype in (".jpg", ".png"):
        curr_img = pygame.transform.scale(img, (res, res))
        path = f"images/logo_{res}{ftype}"
        pygame.image.save(curr_img, path)
