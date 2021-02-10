# Export

Functions that take in your scenes and output a video.

All export functions have these parameters:

* `resolution`: Output resolution.
* `fps`: Output fps.
* `scenes`: List of scenes to export in order.
* `out_path`: Output path. Must be .mp4 file.
* `verbose`: Whether to print out info while exporting.
* `notify`: Whether to notify user after finished exporting via system notification.

## Available Methods

* Single Core: Exports and encodes each frame.
* Multi Core: Exports and encodes each frame on all system cores. Uses many temporary files. MAY BE UNSTABLE.
* FFmpeg: Exports and compresses with FFmpeg. Uses one temporary file.
