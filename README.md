## Converting a Video to a GIF using MoviePy

This is a simple Python script that uses the moviepy library to convert a video file to a GIF image.
Requirements

This script requires the following Python libraries:

* moviepy
* ffmpeg (optional)

You can install the moviepy library using pip:

pip install moviepy

If you encounter any issues with the script, you may need to install ffmpeg. Y
ou can download it from the official website: https://www.ffmpeg.org/

Usage

1. Clone the repository or copy the code to a local file.
2. Replace input_path and output_path with the appropriate file paths for your system.
3. Run the script using a Python interpreter.

Here is an example usage:

```
from moviepy.editor import *

input_path = "test.mov"
output_path = "output.gif"

# Load the input video file
video = VideoFileClip(input_path)

# Convert the video to a GIF and save it to the output file path
video.write_gif(output_path)

# Close the video file
video.close()

```
This script loads the video file at input_path using VideoFileClip class from moviepy library.
It then uses the write_gif method of the VideoFileClip object to convert the video to a GIF and save it to the output file path specified in output_path. 
Finally, it closes the video file to free up system resources.
License

This project is licensed under the MIT License - see the LICENSE.md file for details.
Acknowledgments

This script was inspired by the MoviePy documentation.
