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


def CreateImage(width=1, height=1, depth=3, color=(0, 0, 0)):
    ''' Creates new opencv/numpy image.'''
    return np.full((height, width, depth), color, np.uint8)


def SaveImage(im, filepath):
    ''' Save image file.'''
    cv2.imwrite(filepath, im)


def FillImage(im, color):
    ''' Fill image with color.'''
    h, w, d = im.shape
    return CreateImage(w, h, d, color)


def GetTTFontSize(text, fontName='Roboto.ttf', fontSize=20):
    ''' Draw TrueTypeFont text.'''
    # Pass the image to PIL
    font = ImageFont.truetype(fontName, fontSize)
    # Get width and height of text
    return font.getsize(text)


def DrawTextTTF(image, text, anchor, fontName='Roboto.ttf', fontSize=80, color=(255, 255, 255)):
    ''' Draw TrueTypeFont text.'''
    # Pass the image to PIL
    pil_im = Image.fromarray(image)
    draw = ImageDraw.Draw(pil_im)
    # use a truetype font
    font = ImageFont.truetype(fontName, fontSize)
    # Get width and height of text
    width, height = font.getsize(text)
    # Draw the text
    draw.text(anchor, text, font=font, fill=color)
    # Get back the image to OpenCV
    return cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR), width, height


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
