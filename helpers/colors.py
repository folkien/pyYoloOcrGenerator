'''
Created on 23 lis 2020

@author: spasz
'''

from random import randint

# Colors standard in OpenCV is
# B-G-R
white = (255, 255, 255)
darkgray = (64, 64, 64)
gray = (128, 128, 128)
lightgray = (192, 192, 192)
black = (0, 0, 0)
red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
pink = (0, 255, 255)  # pink ~= magenta
cyan = (255, 255, 0)
yellow = (255, 0, 255)
orange = (0, 140, 255)
brown = (19, 69, 139)
indigo = (130, 0, 75)


# Color table used for next table color method
__colorTable = [
    red,
    blue,
    yellow,
    green,
    pink,
    orange,
    indigo,
    cyan,
    brown
]
__colorTableIndex = 0


def GetNextTableColor():
    '''
        Returns next color from predefinied
        table of example based colors.
    .'''
    global __colorTableIndex
    # Acquire color
    color = __colorTable[__colorTableIndex]
    # Increment index
    __colorTableIndex += 1
    if (__colorTableIndex == len(__colorTable)):
        __colorTableIndex = 0
    return color


def GetRandomBlackWhite():
    '''
        Returns next color from predefinied
        table of example based colors.
    .'''
    colors = [(0, 0, 0), (33, 33, 33), (200, 200, 200), (255, 255, 255)]
    return colors[randint(0, len(colors)-1)]


def GetOpposedColor(color):
    ''' Returns opposed color.'''
    r, g, b = color
    return (255-r, 255-g, 255-b)


def GetRandomColor():
    ''' Returns random color.'''
    return (randint(0, 255), randint(0, 255), randint(0, 255))
