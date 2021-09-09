'''
Created on 9 wrz 2021

@author: spasz
'''
from helpers.images import DrawTextTTF, GetTTFontSize
from random import randint

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
        self.fonts = ['FiraCode-Light.ttf']

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
        return fontSize

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
        fontSize = self.CalculateFontSize(imwidth, rowLength, fontName)

        # Only one row
        posx = 0
        while (posx < (imwidth)):
            # Get character
            text = self.characters[self.lastCharacter]
            self.lastCharacter += 1
            # Uppercase if needed
            if (self.config['Uppercase']):
                text = text.upper()
            # Draw character
            image, textWidth, textHeight = DrawTextTTF(
                image, text, (posx, 0), fontName, fontSize)
            # Move right
            posx += textWidth

        return image, annotations
