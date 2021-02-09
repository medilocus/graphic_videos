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

import sys
import time
import subprocess
from typing import Tuple
import pygame
import cv2
from .scene import Scene
from .printer import printer


def export_sc(resolution: Tuple[int], fps: int, scenes: Tuple[Scene], path: str, verbose: bool = True, notify: bool = True) -> None:
    """
    Single core export.
    :param resolution: Resolution of video.
    :param fps: FPS of video.
    :param scenes: List of scenes to export in order of appearance.
    :param path: Output path of final video (must be .mp4 for now).
    :param verbose: Whether to show information prints.
    :param notify: Whether to send a notification after exporting is finished.
    """
    if not path.endswith(".mp4"):
        raise ValueError("Path must be an MP4 (.mp4) file.")

    video = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*"MPEG"), fps, resolution)
    abs_start = time.time()
    for i, scene in enumerate(scenes):
        scene_num_frames = len(scene.get_frames())
        total_frames = 1
        time_start = time.time()
        for frame in scene.get_frames():
            if verbose:
                elapse = time.time() - time_start
                per_frame = elapse / total_frames
                remaining = per_frame * (scene_num_frames-total_frames)
                remaining = str(remaining)[:6]
                printer.clearline()
                printer.write(f"[GRAPHICS] Exporting: Scene {i+1}/{len(scenes)}: Frame {total_frames}/{scene_num_frames}, {remaining}s remaining.")
            total_frames += 1

            surface = scene.render(resolution, frame)
            surface = pygame.transform.rotate(pygame.transform.flip(surface, False, True), -90)
            image = cv2.cvtColor(pygame.surfarray.array3d(surface), cv2.COLOR_RGB2BGR)
            video.write(image)

        if verbose:
            printer.newline()

    video.release()
    if verbose:
        elapse = time.time() - abs_start
        elapse = str(elapse)[:6]
        printer.clearline()
        printer.write(f"[GRAPHICS] Exporting video: Finished in {elapse}s")
        printer.newline()
    if notify:
        notify_done()


def notify_done():
    if sys.platform == "linux":
        subprocess.Popen(["notify-send", "Graphic Videos", "Finished exporting an animation!"]).wait()
    elif sys.platform == "windows":
        from win10toast import ToastNotifier
        ToastNotifier().show_toast("Graphic Videos", "Finished exporting an animation!", duration=10)
