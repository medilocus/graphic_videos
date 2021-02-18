# Groups

Groups are elements that can contain other elements.

Groups can be found at `graphics.Group`

Groups have location and size properties,
which can be animated and used to move all internal
elements the same amount.

# Group API

* `Group.add_element(element)`
    * Appends an element to the internal list.
    * Parameter `element`: Element to append.
    * Return: `None`
* `Group.extend_elements(elements)`
    * Adds a list of elements to the internal list.
    * Parameter `elements`: List of elements to append.
    * Return: `None`
* `Group.add_modifier(modifier)`
    * Appends a modifier to the internal list.
    * Parameter `modifier`: Modifier to append.
    * Return: `None`
* `Group.extend_modifiers(modifiers)`
    * Adds a list of modifiers to the internal list.
    * Parameter `modifiers`: List of modifiers to append.
    * Return: `None`

[Back to documentation home][home]

[home]: https://medilocus.github.io/graphic_videos/
