# Elements

Elements make up all objects in a video.
Some are very simple, like circles and polygons.
Others are sophisticated, like text effects.

Elements have many animatable properties, which are documented [here][props].

All element classes inherit from `BaseElement`, found at `graphics.elements.BaseElement`
To learn how to create your custom elements, see [Extending Graphic Videos][extending].

## BaseElement API

* `BaseElement.__init__()`
    * BaseElement initialize. Other elements should have their own `__init__` and call `super().__init__()`
* `BaseElement.add_modifier(modifier)`
    * Appends a modifier to the internal list.
    * Parameter `modifier`: Modifier to append.
    * Return: `None`
* `BaseElement.extend_modifiers(modifiers)`
    * Adds a list of modifiers to the internal list.
    * Parameter `modifiers`: List of modifiers to append.
    * Return: `None`
* `BaseElement.render(res, frame)`
    * Renders element and applies all modifiers.
    * Parameter `res`: Output resolution.
    * Parameter `frame`: Frame to render.
    * Return: `pygame.Surface`
* `BaseElement.render_raw(res, frame)`
    * Placeholder method, other elements should define their own.
    * Renders without any modifiers.
    * Parameter `res`: Output resolution.
    * Parameter `frame`: Frame to render.
    * Return: `pygame.Surface`

## Simple Elements

Simple elements are simple shapes, which can be combined to create complex visuals.

Examples include rectangles, circles, and text.

These elements can be found at `graphics.elements.simple.MyElement`

* [Rectangles][rect]
* [Circles][circle]
* [Ellipses][ellipse]
* [Lines][line]
* [Polygons][polygon]
* [Arcs][arc]
* [Text][text]
* [Image][image]
* [Video][video]

[Back to documentation home][home]

[home]: https://medilocus.github.io/graphic_videos/
[props]: https://medilocus.github.io/graphic_videos/props
[extending]: https://medilocus.github.io/graphic_videos/extending

[rect]: https://medilocus.github.io/graphic_videos/elements/rect
[circle]: https://medilocus.github.io/graphic_videos/elements/circle
[ellipse]: https://medilocus.github.io/graphic_videos/elements/ellipse
[line]: https://medilocus.github.io/graphic_videos/elements/line
[polygon]: https://medilocus.github.io/graphic_videos/elements/polygon
[arc]: https://medilocus.github.io/graphic_videos/elements/arc
[text]: https://medilocus.github.io/graphic_videos/elements/text
[image]: https://medilocus.github.io/graphic_videos/elements/image
[video]: https://medilocus.github.io/graphic_videos/elements/video
