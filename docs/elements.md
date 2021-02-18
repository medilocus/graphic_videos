# Elements

Elements make up all objects in a video.
Some are very simple, like circles and polygons.
Others are sophisticated, like text effects.

All element classes inherit from `BaseElement`, found at `graphics.elements.BaseElement`
To learn how to create your custom elements, see [Extending Graphic Videos][extending].

## BaseElement API

* `BaseElement.__init__()`
    * BaseElement initialize. Other elements should have their own `__init__` and call `super().__init__()`
* `BaseElement.add_element(modifier)`
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

[Back to documentation home][home]

[home]: https://medilocus.github.io/graphic_videos/
[extending]: https://medilocus.github.io/graphic_videos/extending
