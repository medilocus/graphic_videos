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

import pygame
import graphics
pygame.init()
graphics.options.DEFAULT_FONT = "font.ttf"

scene = graphics.Scene(0, 1)

scene.add_element(graphics.elements.simple.Text((960, 150), text="Graphic Videos", size=64))
scene.add_element(graphics.elements.simple.Text((960, 300), text="An API for creating graphic videos in Python."))

for x in range(3):
    for y in range(4):
        loc = (60+60*x, 100+95*y)
        size = (50, 85)
        rect = graphics.elements.simple.Rect(loc, size, color=3*(int((y+1)/4*255),))
        scene.add_element(rect)

scene.add_element(graphics.elements.simple.Line((1550, 50), (1750, 200), 2))
scene.add_element(graphics.elements.simple.Line((1920, 200), (1700, 400), 2))
scene.add_element(graphics.elements.simple.Circle((1674, 100), 35, (220, 160, 160)))

pygame.image.save(scene.render((1920, 480), 0), "images/banner.png")
pygame.image.save(scene.render((1920, 480), 0), "images/banner.jpg")
