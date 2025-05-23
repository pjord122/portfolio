'''
The purpose of this program is to create a screen recorder in python. This program shows my understanding
of importing python modules and using them to simplify the coding process.
'''

# The first thing I need to do is install the required modules to complete this task.
# I opened the terminal and did pip install to install numpy, pyautogui, and opencv-python.

# Next I have to import the required packages
import pyautogui
import cv2
import numpy as np

# I have to create a VideoWriter object and also specify the output file name, video codec, FPS, and resolution.
# In the video codec, I also have to specify and 4-byte code like XVID.

# specifies resolution
resolution = (1920, 1080)

# specifies video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# specifies Output file name
filename = "Recording.avi"

# specifies framerate
fps = 30.0

# creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# I want to display the recording in realtime, so I have to create an empty window and resize it.

# creates empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# resizes empty window
cv2.resizeWindow("Live", 480, 270)

# To record the screen, I will be using an infinite loop and in each iteration, a screenshot will be taken
# and written to the output file with the help of the video writer.

while True:
    # uses pyautogui to take a screenshot
    img = pyautogui.screenshot()

    # converts the screenshot to a numpy array
    frame = np.array(img)

    # converts it from BGR (Blue, Green, Red) to RGB (Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # writes it to the output file
    out.write(frame)

    # displays the recording screen
    cv2.imshow("Live", frame)

    # stops recording when "q" is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# after everything is done, the video writer will be released and the windows opened by OpenCV will be destroyed

# releases the Video writer
out.release()

# destroys all windows()
cv2.destroyAllWindows()