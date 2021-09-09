'''
Created on 9 wrz 2021

@author: spasz
'''
from helpers.images import DrawTextTTF

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
        self.fonts = ['Roboto.ttf']

    def Annotate(self, image):
        ''' Annotate image inside and return
        image and annotations list.'''
        # Init annotations list
        annotations = []
        # Get image properties
        imheight, imwidth = image.shape[0:2]
        # Row length [ in characters ]
        rowLength = 5
        # Get font size
        fontSize = 40

        # Only one row
        posx = 0
        while (posx < (imwidth)):
            # Get character
            text = self.characters[self.lastCharacter]
            self.lastCharacter += 1
            # Draw character
            image = DrawTextTTF(image, text, (posx, 0), fontSize)

        return image, annotations
