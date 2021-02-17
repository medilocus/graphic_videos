# Setup

This page contains instructions on how to set up your files to use Graphic Videos.

## Python Modules

The required modules for Graphics are:

* pygame
* opencv-python
* numpy
* pillow

Install these with the command `pip install <package>` or use the file `requirements.txt`, and do `pip install -r requirements.txt`

## Download Module

First, you need to download the pre-written Graphic Videos module.

You have two options:

* Download the latest release from the [releases page][releases].
* Download the latest commit from the [main branch][mainbranch].

Take the folder named `graphics` and delete everything else.

## File Structure

Setup your files in this format:

```
graphics      # The folder that was downloaded
filename.py   # Python file which will be run
```

## Pip Wheel File

If you want to install Graphic Videos as a pip module, use the wheel file on the [latest release][latest].

Download the file ending in `.whl`, and install with `pip install graphic_videos-<version>-py3-none-any.whl`

Make sure the file name matches the downloaded file.


[Back to documentation home][dochome]

[dochome]: https://medilocus.github.io/graphic_videos/
[releases]: https://github.com/medilocus/graphic_videos/releases
[mainbranch]: https://github.com/medilocus/graphic_videos/archive/main.zip
[latest]: https://github.com/medilocus/graphic_videos/releases/latest
