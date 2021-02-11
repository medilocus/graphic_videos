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

import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="graphic-videos",
    version="1.1",
    author="Medilocus",
    author_email="huangpatrick16777216@gmail.com",
    description="An API for creating graphic videos in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/medilocus/graphic_videos",
    py_modules=["graphics"],
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy",
        "pillow",
        "pygame",
        "opencv-python",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
)
