'''
Created on 10 paź 2020

@author: spasz
'''
from pathlib import Path
import hashlib
import datetime
import cv2
import logging
import numpy as np
from PIL import ImageFont, ImageDraw, Image


def CreateImage(width=1, height=1, depth=3):
    ''' Creates new opencv/numpy image.'''
    return np.zeros((height, width, depth), np.uint8)


def SaveImage(im, filepath):
    ''' Save image file.'''
    cv2.imwrite(filepath, im)


def DrawTextTTF(image, text, anchor, fontSize=80):
    ''' Draw TrueTypeFont text.'''
    # Pass the image to PIL
    pil_im = Image.fromarray(image)
    draw = ImageDraw.Draw(pil_im)
    # use a truetype font
    font = ImageFont.truetype('PAPYRUS.ttf', fontSize)
    # Draw the text
    draw.text(anchor, text, font=font)
    # Get back the image to OpenCV
    return cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)


def GetResizedHeightToWidth(width, height, maxWidth=1280):
    ''' Returns resized values.'''
    if (width > maxWidth):
        ratio = maxWidth/width
        height = int(ratio*height)-1
        width = maxWidth

    return width, height


def ResizeToWidth(image, maxWidth=1280):
    ''' Resize image with handling aspect ratio.'''
    height, width = image.shape[:2]
    # Resize only if broader than max width
    if (width > maxWidth):
        width, height = GetResizedHeightToWidth(width, height, maxWidth)
        return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

    # Otherwise return original image
    return image
