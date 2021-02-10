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
import os
import shutil
import time
import subprocess
import multiprocessing
from typing import Tuple
from hashlib import sha256
import pygame
import cv2
from .scene import Scene
from .printer import printer


def get_tmp_path():
    parent = os.path.realpath(os.path.dirname(__file__))
    get_path = lambda: os.path.join(parent, sha256(str(time.time()).encode()).hexdigest()[:16])
    path = get_path()
    while os.path.isdir(path):
        path = get_path()

    return path


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

    video = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*"mp4v"), fps, resolution)
    abs_start = time.time()
    for i, scene in enumerate(scenes):
        scene_frames = scene.get_frames()
        scene_num_frames = len(scene_frames)
        total_frames = 1
        time_start = time.time()
        for frame in scene_frames:
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


def mc_render(scene, frames, path, res):
    for frame in frames:
        curr_path = os.path.join(path, f"{frame}.png")

        surface = scene.render(res, frame)
        pygame.image.save(surface, curr_path)


def export_mc(resolution: Tuple[int], fps: int, scenes: Tuple[Scene], out_path: str, verbose: bool = True, notify: bool = True) -> None:
    """
    Multi core export. Will write images to disk.
    :param resolution: Resolution of video.
    :param fps: FPS of video.
    :param scenes: List of scenes to export in order of appearance.
    :param path: Output path of final video (must be .mp4 for now).
    :param verbose: Whether to show information prints.
    :param notify: Whether to send a notification after exporting is finished.
    """
    if not out_path.endswith(".mp4"):
        raise ValueError("Path must be an MP4 (.mp4) file.")

    num_cpus = multiprocessing.cpu_count()
    path = get_tmp_path()

    video = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, resolution)
    abs_start = time.time()
    success = True
    processes = []
    try:
        for scene_num, scene in enumerate(scenes):
            os.makedirs(path)
            time_start = time.time()
            processes = []
            frames_to_render = scene.get_frames()

            if len(frames_to_render) < num_cpus:
                p = multiprocessing.Process(target=mc_render, args=(scene, frames_to_render, path, resolution))
                processes.append(p)
            else:
                chunk_size = len(frames_to_render) / num_cpus
                for i in range(num_cpus):
                    start = int(chunk_size * i)
                    end = int(chunk_size * (i+1))
                    frames = frames_to_render[start:end]
                    p = multiprocessing.Process(target=mc_render, args=(scene, frames, path, resolution))
                    processes.append(p)

            for p in processes:
                p.start()

            while True in [p.is_alive() for p in processes]:
                time.sleep(0.05)
                if verbose:
                    num_files = max(1, len(os.listdir(path)))
                    elapse = time.time() - time_start
                    per_frame = elapse / num_files
                    remaining = per_frame * (len(frames_to_render)-num_files)
                    remaining = str(remaining)[:6]
                    printer.clearline()
                    printer.write(f"[GRAPHICS] Exporting: Scene {scene_num+1}/{len(scenes)}: " + \
                        f"Frame {num_files}/{len(frames_to_render)}, {remaining}s remaining.")

            printer.newline()
            time.sleep(0.1)
            for i, frame in enumerate(frames_to_render):
                img_path = os.path.join(path, f"{frame}.png")
                if os.path.isfile(img_path):
                    img = cv2.imread(img_path)
                    video.write(img)

                if verbose:
                    num_done = i + 1
                    elapse = time.time() - time_start
                    per_frame = elapse / num_done
                    remaining = per_frame * (len(frames_to_render)-num_done)
                    remaining = str(remaining)[:6]
                    printer.clearline()
                    printer.write(f"[GRAPHICS] Exporting: Scene {scene_num+1}/{len(scenes)}: " + \
                        f"Encoding {num_done}/{len(frames_to_render)}, {remaining}s remaining.")

            printer.newline()
            shutil.rmtree(path)

    except KeyboardInterrupt:
        for p in processes:
            p.terminate()
        time.sleep(0.1)
        shutil.rmtree(path)
        success = False

    video.release()
    if success:
        if verbose:
            elapse = time.time() - abs_start
            elapse = str(elapse)[:6]
            printer.clearline()
            printer.write(f"[GRAPHICS] Exporting video: Finished in {elapse}s")
            printer.newline()
        if notify:
            notify_done()


def export_ffmpeg(resolution: Tuple[int], fps: int, scenes: Tuple[Scene], out_path: str, verbose: bool = True, notify: bool = True) -> None:
    """
    Single core export.
    :param resolution: Resolution of video.
    :param fps: FPS of video.
    :param scenes: List of scenes to export in order of appearance.
    :param path: Output path of final video (must be .mp4 for now).
    :param verbose: Whether to show information prints.
    :param notify: Whether to send a notification after exporting is finished.
    """
    if not out_path.endswith(".mp4"):
        raise ValueError("Path must be an MP4 (.mp4) file.")

    path = get_tmp_path() + ".mp4"

    video = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*"mp4v"), fps, resolution)
    abs_start = time.time()
    for i, scene in enumerate(scenes):
        scene_frames = scene.get_frames()
        scene_num_frames = len(scene_frames)
        total_frames = 1
        time_start = time.time()
        for frame in scene_frames:
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
    time.sleep(0.1)
    os.system(f"ffmpeg -y -i {path} -c:v libx265 -c:a copy -x265-params crf=25 {out_path}")
    os.remove(path)

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
    elif sys.platform == "darwin":
        os.system("osascript -e 'display notification \"Finished exporting an animation!\" with title \"Graphic Videos\"'")
