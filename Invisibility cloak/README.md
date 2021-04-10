# Invisibility Cloak using OpenCV

Through this process, the foreground of any image being shown is removed and in a sense it is made invisible.
There are four main steps as to how the algorithm works:

1. The background frame is captured and stored
2. The cloak is detected based on its color through a color detection algorithm
3. The red colored cloth is segmented out by generating a mask
4. The final augmented output is created

As the main aim is to replace the pixels of the subject in the image with the background pixels, the algorithm works to first capture and store the background. This can be done using a for loop to capture it using multiple frames which allows it to tweak the parameters and take in a high quality image of the background.

Next, if the cloak being used is red, for example, then all the red colored parts in the frame are detected. In order to do this the RGB(Red,Green,Blue) image is transformed to an HSV(Hue,Saturation,Value) color space and a specific range of HSV values is defined so as to detect only the red parts of the image. Using RGB defines the detection only based on primary colors while HSV has the major component of hue which allows the program to detect the cloth in a way more similar to the way the human eye perceives different colors and and their shades.

A mask is generated that determines the regions in the frame that will correspond to the red color, which is then further refined and used to segment out the exact portion of the image in which the red cloth is held.

After this, once the cloak area has been detected, the pixels of that area are replaced with the corresponding pixels of the background, causing the cloak to disappear.