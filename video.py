from moviepy.editor import *

input_path = "test2.mov"
output_path = "output.gif"

# Load the input video file
video = VideoFileClip(input_path)

# Convert the video to a GIF and save it to the output file path
video.write_gif(output_path)

# Close the video file
video.close()

