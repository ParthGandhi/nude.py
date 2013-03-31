nude.py
=======

Nudity detection in Python

This python script allows a user to analyze an image for nudity. 
It also allows a user to color all skin pixels in an image a given color. 

Inspired by nude.js and based on the following paper : 
https://sites.google.com/a/dcs.upd.edu.ph/csp-proceedings/Home/pcsc-2005/AI4.pdf?attredirects=0


Run as : python nude.py filename [-c]
The flag '-c' makes it color the image and save to file. 

TODO:
Currently works only for .jpg images. Get it to work for all kinds of images, including urls. 
It is currently a fairly slow program. I am open to any suggestions for performance improvements.
Write tests and find the statistical accuracy of script.
