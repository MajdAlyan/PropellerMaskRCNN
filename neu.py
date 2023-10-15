from math import cos, sin, pi 
from canvas import Canvas 
from matrices import Matrix 
from vectors import Vector 
from smiley import *

def draw (c):
    c.clear()
    c.drawGrid()
    drawPoints(c, smileyPoints())