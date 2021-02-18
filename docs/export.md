# Export

Exporting is creating the final video from your scenes.

You could write a program yourself to render each frame in a scene and compile a video,
but Graphic Videos has a few built in functions to do that.

# Single Core Export

`graphics.export.export_sc`

This function uses one CPU core to render and encode each frame, one at a time.

It is extremely reliable, and fits for almost any situation.

* Parameter `resolution`: (x, y) resolution of final video.
* Parameter `fps`: FPS (frames per second) of video.
* Parameter `scenes`: List of scenes to export in order.
* Parameter `path`: Output path of video. Must end with `.mp4`
* Parameter `verbose`: Whether to display progress via stdout while exporting.
* Parameter `notify`: Whether to send a notification after finished.

[Back to documentation home][home]

[home]: https://medilocus.github.io/graphic_videos/
