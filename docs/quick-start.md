# Quick Start

This page contains instructions on how to export your first video.

Before using, please follow the [setup][setup] guide.

## Scenes

Scenes are the building blocks of each video.
In each video, one or more scenes are defined and exported in sequence into one video file.

You can think of scenes like a section of your full video. Detailed documentation is available [here][scenedoc].

## Elements

Elements are parts of scenes. Each scene has a list of elements, which can be appended to.
There are many simple pre-written elements, such as polygons, circles, text, and images.
There are also many advanced elements, like text effects.

Detailed documentation [here][elementdoc].

## Keyframes

Keyframes are used to add changes in your elements over time.
Each element has many animatable properties which are animated with keyframes.

As an example, a circle has a size property, which defines its radius. This can be animated with keyframes.

Detailed documentation is [here][keyframedoc].

## Sample Code

Example code which exports a simple video.

This will only work if your files are correctly [set up][setup].

``` python
import graphics

scene = graphics.Scene(0, 60)

rect = graphics.elements.simple.Rect((0, 0), (200, 150), (255, 255, 255))
rect.loc.keyframe((0, 0), 0)
rect.loc.keyframe((500, 300), 30)
rect.loc.keyframe((100, 500), 60)

scene.add_element(rect)

graphics.export.export_sc((1920, 1080), 30, [scene], "out.mp4")
```


[Back to documentation home][dochome]

[dochome]: https://medilocus.github.io/graphic_videos/
[setup]: https://medilocus.github.io/graphic_videos/setup
[scenedoc]: https://medilocus.github.io/graphic_videos/scene
[elementdoc]: https://medilocus.github.io/graphic_videos/elements
[keyframedoc]: https://medilocus.github.io/graphic_videos/keyframes
