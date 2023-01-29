# Import moviepy editor library, which gives us the editing functions
from moviepy.editor import *

sample_dict = [{0: 0.89, 1: 0.94, 2: 0.92, 3: 0.33, 4: 0.01, 5: 0.24, 6: 0.12, 7: 0.04}]

# Function to read the file of opacity inputs
def read_input():
    # Defining and array of the opacity levels for each clip
    opacities = []
    # Iterates through file inputs
    for i in range(len(sample_dict[0])):
        # Parses the input format and stores in variable
        placeholder = sample_dict[0][i]
        # Appends list of video opacities with appropriate float
        opacities.append(placeholder)
    # Finally, returns our array of opacities
    return opacities

# Initializes list of video clips
videos = []
# Takes list of opacity levels from input function
opacities = read_input()
# Iterates through videos and assigns opacities
for i in range(len(opacities)): 
    # Initializes video clip from file
    videos.append(VideoFileClip("video_" + str(i+1) + ".webm"))
    # Sets the opacity level of the video
    videos[i] = videos[i].set_opacity(opacities[i])
# Combines our array of videos into a composite clip
final_video = CompositeVideoClip(videos) 
# Writes our final video to a .webm file
final_video.write_videofile("final_video.webm")