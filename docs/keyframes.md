# Keyframes

Keyframes are used to add change in elements.

## Properties

In the `graphics` module, many types of animatable properties are defined as classes.
Examples include `BoolProp` for boolean, `IntProp` for integer, `FloatProp` for floating point numbers, and `StringProp` for strings.

Each instance of a property has its own keyframes.

## How Keyframes Work

Here is a code block showing the process of adding keyframes.

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