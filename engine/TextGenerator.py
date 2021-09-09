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
