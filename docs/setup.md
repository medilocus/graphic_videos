# Setup

## Pip Package

Graphic Videos is not published on PyPI (the official python package index),
but all releases contain a pip installable wheel file.

To download the wheel file, go to the [latest release][latest],
and download the file ending in `.whl`.

The file will likely be named `graphic_videos-0.1.4-py3-none-any.whl`.
Version numbers may vary.

Next, open a terminal or command prompt in the location of the download.

Locations for common operating systems:

* Linux: `~/Downloads`
* Windows: `C:\Users\username\Downloads`

Once there, type this command and press enter:

`pip install graphic_videos-0.1.4-py3-none-any.whl`

## Portable Directory

You may also choose to install Graphic Videos as a portable folder,
which you can copy and paste anywhere.

Every release contains a zip file named `graphics.zip` with the source code of Graphic Videos.

Download the file named `graphics.zip` in the [latest release][latest].
Extract it to get the folder.

Next, for every project involving Graphic Videos, set up your folders like this:

```
project_folder
|__ graphics    # folder downloaded from release
|__ main.py     # file that will be run to export the video
```

[Back to documentation home][home]

[home]: https://medilocus.github.io/graphic_videos/
[latest]: https://github.com/medilocus/graphic_videos/releases/latest
