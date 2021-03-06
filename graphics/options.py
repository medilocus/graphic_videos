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

import os
from math import e


def get_pbola_xmax():
    return PARABOLA_XMAX

def get_font():
    return DEFAULT_FONT

def get_col_palette():
    return COLOR_PALETTE

def get_mb_frames():
    return MB_FRAMES

def get_mb_step():
    return MB_STEP


# Sigmoid is no longer used.
SIGMOID_XRANGE = 3
SIGMOID_COMPENSATION = 1 + e**((1-3**0.5) * SIGMOID_XRANGE)

PARABOLA_XMAX = 2

DEFAULT_FONT = "arial"
COLOR_PALETTE = {}
MB_FRAMES = 14
MB_STEP = 0.25
