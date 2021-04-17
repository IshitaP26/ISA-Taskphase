# Ball Detection and Tracking using OpenCV


In this process the ball is first detected on the screen and then its movement across the screen is tracked. The colorspace is converted from the normal RGB space to HSV for a better detection of the colors, with the upper and lower boundaries of the color being used to detect the ball of that specific color, in this case it is yellow.

Once the HSV color space has been established, the image being captured is preprocessed in terms of blurring to reduce the high frequency noise so as to focus only on the ball. Once this has been done the localization of the ball in the frame takes place to create a binary mask which shows the ball as a white circel in a black background, meaning that it has been detected. Erosions and dilations are then performed in order to clear out the mask.

The next part of the process is computing the contour of the ball which is done using the cv2.findContour action. The largest contour is identified and the minimum enclosing circle of the ball is found to then compute the centroid of the ball which is the point to be tracked. The x coordinate of the centroid is found by M10/M00 and the y coordinate is found by M01/M00. This action uses image moment, which is a weighted average of image pixel intensities, and can be used to find some specific properties like the radius, centroid and diameter.

Once the outline of the ball and the centroid have been marked, the contrail, or the path that the ball travels is marked. A deque, which is a list like data structure, is used to maintain the list of the (x,y) locations of the ball. Looping over each of the values in the list, whichever of the points are valid are drawn on the frame with a specified thickness.

The final output can then be projected using the webcam.

**Resources**

1. https://learnopencv.com/find-center-of-blob-centroid-using-opencv-cpp-python/
2. https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
3. https://www.bluetin.io/opencv/object-detection-tracking-opencv-python/


