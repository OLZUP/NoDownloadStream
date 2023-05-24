# importing libraries
import cv2
import numpy as np

# Create a VideoCapture object and read from input file
#NOTE - You must have the link to an actual video file hosted online for this to work.
#It can't be a normal link like a youtube link. The file type should be in the link like ".mp4" as shown below!
now = cv2.VideoCapture('example url - https://www.example.com/filename.mp4/file')

# Check if camera opened successfully
if (now.isOpened()== False):
	print("Error opening video file")

# Read until video is completed
while(now.isOpened()):

# Capture frame-by-frame
	ret, frame = now.read()
	if ret == True:
	# Display the resulting frame
		cv2.imshow('Frame', frame)

	# Press Q on keyboard to exit
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break

# Break the loop
	else:
		break

# When everything done, release
# the video capture object
now.release()

# Closes all the frames
cv2.destroyAllWindows()
