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

Here is an example:

``` python
import graphics

my_prop = graphics.props.IntProp(4)

# You can get the value of the property by calling it.
# The parameter represents what frame you are getting.
value = my_prop(5)
print(value)
```

Right now, `my_prop` has no keyframes.
The value we pass in when initializing it is it's default value.
The property will return it's default value when it has no keyframes.

In this case, the program will print `5`.

``` python
import graphics

my_prop = graphics.props.IntProp(4)

# The arguments are keyframe(value, frame)
my_prop.keyframe(2, 0)

print(my_prop(0))
```

Now we keyframed the property to have a value of 2 at frame 0.
The program will print `2` at frame 0.

[Back to documentation home][home]

[home]: https://medilocus.github.io/graphic_videos/
