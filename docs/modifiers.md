# Modifiers

Modifiers modify the rendered image in elements and groups.

All modifiers have [properties][props] which can be animated.

All modifiers inherit from `graphics.modifiers.Modifier`
To write your own modifiers, please look at [Extending Graphic Videos][extending].

## Base Modifier API

* `Modifier.__init__`
    * Base modifier init. Other modifiers should have their own init and call `super().__init__()`.
* `Modifier.modify(src, frame)`:
    * This function is called by the scene when rendering. All this function does is remove alpha from the surface and call `modify_raw`.
    * Parameter `src`: Source surface.
    * Parameter `frame`: Frame to modify. This changes property values.
    * Return: `pygame.Surface`
* `Modifier.modify_raw(src, frame)`
    * Empty method. Other modifiers should define their own.
    * This is the method that applies effects to the surface.
    * Parameter `src`: Source surface.
    * Parameter `frame`: Frame to modify. This changes property values.
    * Return: `pygame.Surface`

[Back to documentation home][home]

[home]: https://medilocus.github.io/graphic_videos/
[props]: https://medilocus.github.io/graphic_videos/props
[extending]: https://medilocus.github.io/graphic_videos/extending
