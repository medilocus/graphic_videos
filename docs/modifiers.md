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

## Pre-written Modifiers

Examples include Blur, Flip, and Brighten.

* Flip
* MixSolidColor
* GaussianBlur
* Grayscale
* Bright
* Contrast
* ColorEnhance
* Sharpen
* Invert

[Back to documentation home][home]

[home]: https://medilocus.github.io/graphic_videos/
[props]: https://medilocus.github.io/graphic_videos/props
[extending]: https://medilocus.github.io/graphic_videos/extending

[flip]: https://medilocus.github.io/graphic_videos/modifiers/flip
[mix-solid-color]: https://medilocus.github.io/graphic_videos/modifiers/mix-solid-color
[gaussian-blur]: https://medilocus.github.io/graphic_videos/modifiers/gaussian-blur
[grayscale]: https://medilocus.github.io/graphic_videos/modifiers/grayscale
[bright]: https://medilocus.github.io/graphic_videos/modifiers/bright
[contrast]: https://medilocus.github.io/graphic_videos/modifiers/contrast
[color-enhance]: https://medilocus.github.io/graphic_videos/modifiers/color-enhance
[sharpen]: https://medilocus.github.io/graphic_videos/modifiers/sharpen
[invert]: https://medilocus.github.io/graphic_videos/modifiers/invert
