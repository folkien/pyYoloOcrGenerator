'''
Created on 9 wrz 2021

@author: spasz
'''
import logging
from helpers.images import DrawTextTTF, GetTTFontSize
from random import randint
from helpers.Annotation import CreateAnnotationfromDetection, ToRelative

# Diffrent characters lists
charactersLists = ['12345678890',
                   'qwertyuiopasdfghjklzxcvbnm',
                   '12345678890qwertyuiopasdfghjklzxcvbnm'
                   ]


class TextGenerator:
    '''
    classdocs
    '''

    def __init__(self,
                 characterListNumber=2,
                 rows=2,
                 uppercase=True):
        '''
        Constructor
        '''
        # Configuration
        self.config = {'Uppercase': uppercase,  # All letters will be uppercase
                       'Rows': rows,  # Max number of rows
                       }
        # Used characters list
        self.characters = list(charactersLists[characterListNumber])
        # Last used character number
        self.lastCharacter = 0
        # List of used fonts
        self.fonts = ['Autobabahn.ttf',
                      'Kenteken.ttf',
                      'LicensePlate.ttf',
                      'PlatNomor.ttf',
                      'Uknumberplate.ttf', ]

        # Spacing - 5px
        self.spacing = 5
        # Margin
        self.margin = 5

    def CalculateFontSize(self, imwidth, rowLength, fontName):
        ''' Calculate used font size.'''
        # Use first character
        text = self.characters[0]
        if (self.config['Uppercase']):
            text = text.upper()

        # Calculate for font size 20
        fontSize = 20
        width, height = GetTTFontSize(text, fontName, fontSize)
        ratio = int(imwidth/(width*rowLength))
        fontSize = int(fontSize * ratio)

        # Read again and return
        width, height = GetTTFontSize(text, fontName, fontSize)
        return fontSize, width, height

    def Annotate(self, image):
        ''' Annotate image inside and return
        image and annotations list.'''
        # Init annotations list
        annotations = []
        # Get image properties
        imheight, imwidth = image.shape[0:2]
        # Row length [ in characters ]
        rowLength = 5
        # Get font name
        fontName = self.fonts[randint(0, len(self.fonts)-1)]
        # Get font size
        fontSize, fontWidth, fontHeight = self.CalculateFontSize(
            imwidth, rowLength, fontName)

        # Set start position
        posx = self.margin
        posy = self.margin
        # Draw characters in whole image
        while (posy < (imheight-fontHeight-self.margin)):

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
                image, textWidth, textHeight = DrawTextTTF(
                    image, text, (posx, posy), fontName, fontSize)

                # 2. Annotating
                # --------------------------
                x1, y1, x2, y2 = posx, posy, posx+textWidth, posy+textHeight
                rectRel = ToRelative((x1, y1, x2, y2), imwidth, imheight)
                annotations.append(CreateAnnotationfromDetection(
                    (self.lastCharacter, 1.0, rectRel)))

                # 3. Move right and next line. Forward character number
                posx += textWidth + self.spacing
                self.lastCharacter += 1
                self.lastCharacter %= len(self.characters)

            # Increment row
            posy += textHeight

        logging.debug('(TextGenerator) Annotated image.')
        return image, annotations
