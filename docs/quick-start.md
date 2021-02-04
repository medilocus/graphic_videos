# Quick Start

## Setting Up Files
1. Download the [latest zip file][latestzip] and extract it somewhere.
2. Inside the extracted zip, you will find a folder titled **graphics**.
3. Make a new folder for a new animation.
4. Copy the graphics folder from the zip into the new folder.
5. Make a new Python file in the new folder.
Your folder structure should look like this:
```
new_folder     # The new folder you created
|__ graphics   # The copied folder from the zip
|__ main.py    # New Python file.
```

## Inside the main Python file
<!-- Add info links. -->
Follow this structure:
``` python
import graphics   # This imports the copied folder.

frame_start = 0
frame_end = 60
frame_step = 1

rectangle = graphics.elements.simple.Rect((10, 10), (300, 100), (255, 255, 255))
rectangle.loc.keyframe((10, 10), 0)
rectangle.loc.keyframe((500, 100), 60)

scene = graphics.Scene(frame_start, frame_end, frame_step)
scene.add_element(rectangle)

graphics.export.export_sc((1280, 720), 30, [scene], "out.mp4")
```


[latestzip]: https://github.com/medilocus/graphic_videos/archive/main.zip
