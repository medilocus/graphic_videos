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

# A new instance of a property is created.
# The argument specifies its default value.
# Right now, the instance has no keyframes.
my_prop = graphics.props.IntProp(1)

# We can access the property's value with the get_value method.
# The argument specifies the frame we want.
# In this case, the frame does not matter because no keyframes exist.
# The property will return its default value (which is 1).
print(my_prop.get_value(0))

# We can add keyframes with the keyframe method.
# The first argument specifies the value.
# The second argument specifies the frame.
my_prop.keyframe(0, 0)

# Now that there is a keyframe on frame 0, the value at frame 0 will be 0 (as keyframed above).
print(my_prop.get_value(0))

# We can add a second keyframe the same way.
# In this case, keyframing the value 10 on frame 5.
my_prop.keyframe(10, 5)

# The value at frame 0 will still be 0,
# because adding a second keyframe did not overwrite the first one.
print(my_prop.get_value(0))

# The value at frame 5 will be 10, due to the second keyframe.
print(my_prop.get_value(5))

# What will the value at frame 2 be?
# Read the section "Interpolation" below to find out.
print(my_prop.get_value(2))
```

## Interpolation

As stated above, it is uncertain what the value of the property will be on frame 2.

The `graphics` module supports many types of interpolations.

Interpolation is the way of moving from one value to another.
Linear interpolation, for example, is moving at the exact same speed the whole time.
The `graphics` module supports a few types of interpolation, stated below.

The documentation below for different types of interpolation is written based on this setup:

``` python
import graphics

my_prop = graphics.props.IntProp(1)

my_prop.keyframe(0, 0)
my_prop.keyframe(5, 10)

for i in range(6):
    # Print the value of each frame from 0 to 5.
    print(my_prop.get_value(i), end=" ")
```

* Constant Interpolation
    * Will remain at the first value until the frame reaches the second.
    * Output: `0 0 0 0 0 10`
* Linear Interpolation
    * Rises from the values at a constant speed.
    * Output: `0 2 4 6 8 10`
* Quadratic Interpolation
    * Starts slow, rises fast in the middle, and ends slow. Creates a smooth motion.
    * Output: `TODO write output`

Some props do not support some interpolations.
For example, StringProp does not support Linear or Quadratic,
because it is unclear how to interpolate between two strings.

To control the type of interpolation, pass it as an argument while keyframing:

``` python
my_prop.keyframe(0, 0, "LINEAR")
```

[Back to documentation home][home]

[home]: https://medilocus.github.io/graphic_videos/
