'''
Created on 9 wrz 2021

@author: spasz
'''
import logging
from helpers.images import DrawTextTTF, GetTTFontSize
from random import randint
from helpers.Annotation import CreateAnnotationfromDetection, ToRelative
from helpers.colors import GetNextTableColor, GetRandomBlackWhite,\
    GetRandomPlateColor
from reportlab.platypus.tables import _rowLen

# Diffrent characters lists
charactersLists = ['1234567890',
                   'qwertyuiopasdfghjklzxcvbnm',
                   '1234567890qwertyuiopasdfghjklzxcvbnm',
                   '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                   ]


class TextGenerator:
    '''
    classdocs
    '''

    def __init__(self,
                 characterListNumber=3,
                 rowLength=2,
                 uppercase=True,
                 annotationOffset=0,
                 ):
        '''
        Constructor
        '''
        # Configuration
        self.config = {'Uppercase': uppercase,  # All letters will be uppercase
                       'RowLength': rowLength,  # Max number of rows
                       'AnnotationOffset': annotationOffset,  # Offset of annotation numbers
                       }
        # Used characters list
        self.characters = list(charactersLists[characterListNumber])
        # Uppercase if needed
        if (self.config['Uppercase']):
            self.characters = [char.upper() for char in self.characters]
        # Last used character number
        self.lastCharacter = 0
        # List of used fonts
        self.fonts = ['Autobabahn.ttf',
                      'Kenteken.ttf',
                      'LicensePlate.ttf',
                      'PlatNomor.ttf',
                      'Uknumberplate.ttf',
                      'din1451alt.ttf',
                      'Roboto-Light.ttf',
                      'Verdana.ttf',
                      ]

        # Spacing - 5px
        self.spacing = 5
        # Margin
        self.margin = 5
        # Cache
        self.cache = dict()

    def GetMaxCharsetFontSize(self, charset, fontName='Roboto.ttf', fontSize=20):
        ''' Draw TrueTypeFont text.'''
        # 1. Chech cache entry and return
        keyCache = '%s%u' % (fontName, fontSize)
        if (keyCache in self.cache.keys()):
            return self.cache[keyCache]

        # 2. Manually calculate
        maxwidth, maxheight = 0, 0
        for letter in charset:
            width, height = GetTTFontSize(letter, fontName, fontSize)
            maxwidth = max(maxwidth, width)
            maxheight = max(maxheight, height)

        # 3. Save in cache
        self.cache[keyCache] = (maxwidth, maxheight)
        return maxwidth, maxheight

    def CalculateFontSize(self, imwidth, rowLength, fontName):
        ''' Calculate used font size.'''
        # Calculate for font size 20
        fontSize = 20
        width, height = self.GetMaxCharsetFontSize(
            self.characters, fontName, fontSize)
        ratio = int(imwidth/(width*rowLength))
        fontSize = int(fontSize * ratio)
        # Return new font width and height
        width, height = self.GetMaxCharsetFontSize(
            self.characters, fontName, fontSize)
        return fontSize, width, height

    def Annotate(self, image):
        ''' Annotate image inside and return
        image and annotations list.'''
        # Init annotations list
        annotations = []
        # Get image properties
        imheight, imwidth = image.shape[0:2]
        # Get font name
        fontName = self.fonts[randint(0, len(self.fonts)-1)]
        # Get font size
        fontSize, fontWidth, fontHeight = self.CalculateFontSize(
            imwidth, self.config['RowLength'], fontName)

        # Set start position
        posy = self.margin
        # Draw characters in whole image
        while (posy < (imheight-fontHeight-self.margin)):
            posx = self.margin

            # Draw characters line in loop
            while (posx < (imwidth-fontWidth-self.spacing-self.margin)):
                # 1. Drawing
                # --------------------------
                # Get character
                text = self.characters[self.lastCharacter]
                # Uppercase if needed
                if (self.config['Uppercase']):
                    text = text.upper()
                # Draw character
                image, textWidth, textHeight = DrawTextTTF(image,
                                                           text,
                                                           (posx, posy),
                                                           fontName,
                                                           fontSize,
                                                           color=GetRandomPlateColor())

                # 2. Annotating
                # --------------------------
                x1, y1, x2, y2 = posx, posy, posx+textWidth, posy+textHeight
                rectRel = ToRelative((x1, y1, x2, y2), imwidth, imheight)
                annotations.append(CreateAnnotationfromDetection(
                    (self.lastCharacter+self.config['AnnotationOffset'], 1.0, rectRel)))

                # 3. Move right and next line. Forward character number
                posx += textWidth + self.spacing
                self.lastCharacter += 1
                self.lastCharacter %= len(self.characters)

            # Increment row
            posy += textHeight + self.spacing

        logging.debug('(TextGenerator) Annotated image.')
        return image, annotations
