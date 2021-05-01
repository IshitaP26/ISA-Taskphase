# Automating the Google Dino Game

In order to automate the Google Dino Game, it is necessary to use pyautogui which can capture screenshots and control the keyboard, as well as use OpenCV for the various image recognition aspects of the process.

A screenshot of the page of the game on greyscale since the game is itself in black and white. After this a black rectangular section is created to detect the cacti and a slightly smaller rectangle is made a little higher, of a slightly lighter color to detect the birds. These rectangles are drawn through a trial and error process so as to fit the size of the screen.

Next a function is created to check whether there are any cacti or birds coming in to collision with the rectangles, and if there is a cacti detected, the space bar is pressed while if there is a bird detected, the down key is pressed. This entire process is iterated over and over to allow the dinosaur to pass all hurdles and move forward.

**References Used**

https://medium.com/analytics-vidhya/automate-chrome-dino-game-using-python-pyautogui-and-pil-eeb839005ccf#:~:text=The%20same%20goes%20for%20birds,game%20is%20automated%20using%20python.
