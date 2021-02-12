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

import graphics

scene = graphics.Scene(0, 60)

rect = graphics.elements.simple.Rect((0, 0), (200, 150), (255, 255, 255))
rect.loc.keyframe((0, 0), 0)
rect.loc.keyframe((500, 300), 30)
rect.loc.keyframe((100, 500), 60)

scene.add_element(rect)

graphics.export.export_sc((1280, 720), 30, [scene], "out.mp4")
