# Properties

Properties are animatable attributes,
which can be used to change the appearance of elements over time.

For example, a Circle has a radius and location attribute.
Those define it's radius and center, and can be changed over time.

The way Graphic Videos implements properties is quite complicated,
so please take the time to read this whole page.

## Base Property

The base property class, located at `graphics.props.Property`,
contains the internal interpolation code of all properties.
Other props, like BoolProp and IntProp extend off of this class.

## Common Properties

These properties are used commonly in elements.

* BoolProp: Boolean property.
* IntProp: Integer property.
* FloatProp: Floating point property.
* StringProp: String property.

## Keyframes

Keyframes are used to animate properties. Each keyframe contains three values:

* Frame: The frame which the keyframe represents.
* Value: The value of the property at the frame.
* Interpolation: The way to transition from this keyframe to the next.

[Back to documentation home][home]

[home]: https://medilocus.github.io/graphic_videos/
