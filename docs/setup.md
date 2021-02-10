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
* Download the latest commit from the [main branch][latest].

Take the folder named `graphics` and delete everything else.

## File Structure

Setup your files in this format:

```
graphics      # The folder that was downloaded
filename.py   # Python file which will be run
```


[Back to documentation home][dochome]

[dochome]: https://medilocus.github.io/graphic_videos/
[releases]: https://github.com/medilocus/graphic_videos/releases
[latest]: https://github.com/medilocus/graphic_videos/archive/main.zip
