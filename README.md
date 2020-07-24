# Invisible_cloak
A short project that involved the masking technique using openCV that as represented in Harry Potter.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Setup/Requirements
The code is written in Python.
And for the better performance requirements turn out to the latest version of python i.e. Python3.5 or above

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# You need the following libraries

## numpy 
## OpenCV
## time

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Installation for Numpy

Open Command Prompt (Windows) or Terminal (Linux) and type in the following command:

     pip install numpy


# Installation for OpenCV

Open Command Prompt (Windows) or Terminal (Linux) and type in the following command:

     pip install opencv-python     [OR]     pip3 install opencv-python
     
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Algorithm

Convert RGB to HSV and select a range, which is used to segment the color

Create a mask with the segmented HSV color

Apply Morphological Operations (Closing) to fill out holes in the mask. Make sure you use appropiate kernel/filter size. 10 works for my case.

Find all the contours using OpenCV function and then arrange them in descending order in terms of Area.

Select the largest contour and create a complete mask of that using polynomial fill function.

With that mask, create object and background masks.

Bitwise NOT the background and object masks in order to replace the object of interest with the background

Repeat this for every frame.

That's it , you are done to test.
