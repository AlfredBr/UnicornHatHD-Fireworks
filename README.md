# unicornhathd-fireworks
A simple demo of fireworks on the UnicornHatHD.

I included my own version of unicornhathd.py that adds safe_set_pixel(), draw_line() and draw_circle().

* safe_set_pixel() is forgiving if x or y are out of range for the UnicornHatHD

* draw_line() algorithm adaped from:
https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm

* draw_circle() algorithm adapted from:
https://www.geeksforgeeks.org/bresenhams-circle-drawing-algorithm/

* draw_rect() and fill_rect() are built from draw_line()

Fireworks algorithm adapted from:
https://www.101computing.net/fireworks-display/

![Made with Python](https://forthebadge.com/images/badges/made-with-python.svg)
