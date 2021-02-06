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
import time
import pygame
import cv2
from . import options
from .scene import Scene
from .printer import printer


def export_sc(resolution: Tuple, fps: int, scenes: Tuple[Scene], path: str, print: bool = True) -> None:
    """
    Single core export.
    :param resolution: Resolution of video.
    :param fps: FPS of video.
    :param scenes: List of scenes to export in order of appearance.
    :param path: Output path of final video (must be .mp4 for now).
    :param print: Whether to show information prints.
    """
    if not path.endswith(".mp4"):
        raise ValueError("Path must be an MP4 (.mp4) file.")

    video = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*"MPEG"), fps, resolution)
    total_frames = 0
    for i, scene in enumerate(scenes):
        scene_num_frames = len(scene.get_frames())
        for frame in scene.get_frames():
            if print:
                printer.clearline()
                printer.write(f"[GRAPHICS] Exporting video: Scene {i+1}/{len(scenes)}: {total_frames}/{scene_num_frames} frames encoded.")
            total_frames += 1

            surface = scene.render(resolution, frame)
            surface = pygame.transform.rotate(pygame.transform.flip(surface, False, True), -90)
            image = cv2.cvtColor(pygame.surfarray.array3d(surface), cv2.COLOR_RGB2BGR)
            video.write(image)

        if print:
            printer.newline()

    video.release()
    if print:
        printer.clearline()
        printer.write("[GRAPHICS] Exporting video: Finished\n")
