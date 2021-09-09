'''
Created on 16 lis 2020

@author: spasz
'''
import os
import logging
from helpers.files import GetExtension
from helpers.Annotation import CreateAnnotationfromYoloTxt


def ReadAnnotations(filepath):
    '''Read annotations from file.'''
    annotations = []
    if (os.path.exists(filepath)):
        # YOLO format
        if (GetExtension(filepath) == '.txt'):
            # Read yolo format
            with open(filepath, 'r') as f:
                for line in f:
                    annotations.append(CreateAnnotationfromYoloTxt(line))
        else:
            logging.error('Unknown annotations format!')

    return annotations


def SaveAnnotations(filepath, annotations):
    '''Save annotations for file.'''
    with open(filepath, 'w') as f:
        for note in annotations:
            f.write(note.toYoloTxt())
