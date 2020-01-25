# Dependencies
python3, pygame

# How it works
There are three (by default) fixed red points set up as a triangle, as well as a 1px wide black point in the middle of the screen. 
At each iteration, a random red point is selected and a new black point is created halfway between the red point and the black point of the previous iteration. This creates a Sierpinski triangle.

# Controls

* Space: start/stop
* R: reset
* Left click: add a new point
* Up/down: increase/decrease ratio (default is 0.5: each iteration, a new point is added 50% of the way between the previous point and a random red point)
