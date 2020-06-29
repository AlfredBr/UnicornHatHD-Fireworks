#!/usr/bin/env python

import colorsys
import math
import time
import random
import unicornhathd as uhat
from random import randint

def random_color():
    colors_array = []
    colors_array.append((255, 0, 0))
    colors_array.append((255, 0, 0))
    colors_array.append((255, 0, 0))
    colors_array.append((0, 255, 0))
    colors_array.append((0, 255, 0))
    colors_array.append((0, 255, 0))
    colors_array.append((0, 0, 255))
    colors_array.append((0, 0, 255))
    colors_array.append((0, 0, 255))
    colors_array.append((255, 255, 0))
    colors_array.append((0, 255, 255))
    colors_array.append((255, 0, 255))
    colors_array.append((255, 255, 255))
    index = randint(0, len(colors_array)-1)
    return colors_array[index]

def color_shader(color, s):
    shadedcolor = (color[0]*s, color[1]*s, color[2]*s)
    return shadedcolor

def draw_circle(x, y, z, color, d):
    sc = color_shader(color, d)
    uhat.draw_circle(x, y, z, sc[0], sc[1], sc[2])

def burst():
    uhat.clear()
    uhat.set_rotation(90)
    t = 16

    randomcolors = []
    for i in range(t):
        randomcolors.append(random_color())

    xyz = []
    for i in range(t):
        xyz.append((randint(0,8)+4, randint(0,8)+4, randint(0,4)+4, random_color()))

    for loop in range(25):
        uhat.set_brightness(0.5)
        random.shuffle(randomcolors)            
        random.shuffle(xyz)

        for u in range(t):
            ut = max(0, math.cos(math.radians(1-(u*11))))
            uhat.set_all(0, 0, 0)
            for n in range(5):
                draw_circle(xyz[n][0], xyz[n][1], min(xyz[n][2],u), randomcolors[n], ut)
            time.sleep(0.05)
            uhat.show()
        time.sleep(0.5)

def pointc(x, y, color):
    point(x, y, color[0], color[1], color[2])

def point(x, y, r, g, b):
    center = 7
    uhat.safe_set_pixel(y+center, x+center, r, g, b);

def point_xy(x, y, r, g, b):
    uhat.safe_set_pixel(y, x, r, g, b)
    
def launch(pad):
    apogee = randint(5, 10)
    x = pad
    y = 15
    while y > apogee:
        point_xy(x, y, 255, 255, 255)
        point_xy(x, y+1, 127, 127, 127)
        point_xy(x, y+2, 64, 64, 64)
        point_xy(x, y+3, 0, 0, 0)
        uhat.show()
        time.sleep(0.1)
        y=y-1

    point_xy(x, y, 0, 0, 0)
    point_xy(x, y+1, 0, 0, 0)
    point_xy(x, y+2, 0, 0, 0)
    point_xy(x, y+3, 0, 0, 0)

    return apogee
    
def pop(x, y):
    numberOfParticles=randint(5, 12)
    lifespan=randint(30, 60)
    color = random_color()

    x = x - 7
    y = y - 7

    pointc(x, y, color)
    uhat.show();
    time.sleep(0.2)
    
    position=[]
    velocity=[]

    for i in range(0, numberOfParticles):    
        position.append([x,y])
        velocity.append([1,1])

    lives = 0
    while lives <= lifespan:
        for i in range(0, numberOfParticles):
            point(position[i][0], position[i][1], 0, 0, 0)
            #pointc(position[i][0], position[i][1], color_shader(color, 0.05))
            position[i][0]+=velocity[i][0]*math.cos(math.radians(i*360/numberOfParticles))
            position[i][1]+=velocity[i][1]*math.sin(math.radians(i*360/numberOfParticles))
            pointc(position[i][0], position[i][1], color)
        time.sleep(0.05)
        uhat.show()
        lives += 1

def ground_show():
    for x in range(25):
        pad = randint(4,11)
        apogee = launch(pad)
        pop(pad, apogee)

def sky_show():
    burst()

def main():
    uhat.clear()
    uhat.set_rotation(90)
    uhat.show()

    try:
        while True:
            sky_show()
            ground_show()
    except KeyboardInterrupt:
        uhat.off()
        exit()

main()

