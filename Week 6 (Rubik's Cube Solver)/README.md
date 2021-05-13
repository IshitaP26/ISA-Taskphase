# Rubik's Cube Solver

Using the Kociemba library in python, a program can be created to detect the current state of the Rubik's cube and solve it using Herbert Kociemba's two phase algorithm. The package has the one main function of solve() into which the cube definition string must be inputed to receive a solution string which will be in the standard notation of U, D, F, R, B, L, where 

F - front

B - back

R - right

L - left 

D - down

U - up

These letters signify the various facelet positions of the cube and instruct the user to make the changes accordingly. A single letter by itself signifies a clockwise rotation of 90 degrees, a letter followed by an apostrophe, such as F', means the face needs to be turned counterclockwise by 90 degrees and a letter followed by a 2, such as F2, means that the face needs to be turned twice.

So in order to create a program which is able to give the final result of the series of turns required to solve the cube, the machine must first detect the cube, find the contours of the cube and the individual squares within the cube.


