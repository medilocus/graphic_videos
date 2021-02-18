# Scenes

Scenes are sections of a final video.
Each scene contains a start and end frame and an internal list of elements included.

A scene object is stored at `graphics.Scene`

## Scene API

* `Scene.__init__(start, end, step, bg_col, before_pause, after_pause, motion_blur)`
    * Initializes scene object.
    * Parameter `start`: Starting frame of export. Usually is 0.
    * Parameter `end`: Ending frame of export.
    * Parameter `step=1`: Frame step during export.
    * Parameter `before_pause=30`: Number of black frames before content starts.
    * Parameter `after_pause=30`: Number of black frames after content ends.
    * Parameter `motion_blur=False`: Whether to use Motion Blur. See below for more info.

[Back to documentation home][home]

[home]: https://medilocus.github.io/graphic_videos/