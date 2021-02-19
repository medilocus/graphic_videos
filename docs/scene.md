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
    * Return: `None`
* `Scene.add_element(element)`
    * Appends an element to the internal list.
    * Parameter `element`: Element to append.
    * Return: `None`
* `Scene.extend_elements(elements)`
    * Adds a list of elements to the internal list.
    * Parameter `elements`: List of elements to append.
    * Return: `None`
* `Scene.render_frame(res, frame)`
    * Renders raw frame.
    * Parameter `res`: Output resolution.
    * Parameter `frame`: Frame to render.
    * Return: `pygame.Surface`
* `Scene.render(res, frame)`
    * Renders post-processed frames. Applies effects like motion blur.
    * Parameter `res`: Output resolution.
    * Parameter `frame`: Frame to render.
    * Return: `pygame.Surface`

## Motion Blur

You have the option of enabling motion blur in specific scenes.
Motion blur creates simple blurring to improve frames with fast motion.

The current motion blur works by rendering many frames nearby the target frame
and combining them with a linear falloff.

This slows down rendering drastically though, so it is not recommended to use motion blur.

[Back to documentation home][home]

[home]: https://medilocus.github.io/graphic_videos/
