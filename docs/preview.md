# Preview

Use this tool to preview your animation before taking a long time to [export][export].

Preview is located at [`graphics/preview/`][preview]

The function launch requires the following parameters:

* `resolution`: Resolution of preview.
* `fps`: Framerate of preview. Preview might have a lower framerate than the one given if your animation has many elements.
* `scenes`: List of scenes to export in order.
* `resizable`: Do you want your window resizable? Default: `True`

## Example

```py
# Import module
import graphics

# Create scene
scene = graphics.Scene(0, 60)

# Create element
rect = graphics.elements.simple.Rect((0, 0), (200, 150), (255, 255, 255))

# Animate element
rect.loc.keyframe((0, 0), 0)
rect.loc.keyframe((500, 300), 30)
rect.loc.keyframe((100, 500), 60)

# Add element to scene
scene.add_element(rect)

# Preview scene
graphics.preview.launch((1920, 1080), 30, [scene])
```

[Back to documentation home][dochome]

[dochome]: https://medilocus.github.io/graphic_videos/
[export]: https://medilocus.github.io/graphic_videos/export/
[preview]: https://github.com/medilocus/graphic_videos/tree/main/graphics/preview/
