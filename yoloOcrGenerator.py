#!/usr/bin/python3
import logging
import argparse
import sys
from helpers.images import CreateImage, SaveImage
from helpers.colors import GetRandomColor
from engine.TextGenerator import TextGenerator
from helpers.files import RenameToSha1Filepath, FixPath, GetFilepath,\
    GetNotExistingSha1Filepath
from helpers.hashing import GetRandomSha1
from helpers.Annotations import SaveAnnotations

# Arguments and config
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', type=str,
                    required=True, help='Output path')
parser.add_argument('-yw', '--yolowidth', type=int, nargs='?', const=416, default=416,
                    required=False, help='Yolo width, default 416')
parser.add_argument('-yh', '--yoloheight', type=int, nargs='?', const=416, default=416,
                    required=False, help='Yolo height, default 416')
parser.add_argument('-n', '--nsamples', type=int, nargs='?', const=25, default=25,
                    required=False, help='Number of generated samples')
parser.add_argument('-an', '--offset', type=int, nargs='?', const=0, default=0,
                    required=False, help='Offset of annotations numbers')
parser.add_argument('-cs', '--characterSet', type=int, nargs='?', const=3, default=3,
                    required=False, help='Number of characters set')
parser.add_argument('-rl', '--rowLength', type=int, nargs='?', const=5, default=5,
                    required=False, help='Row length in characters')
parser.add_argument('-v', '--verbose', action='store_true',
                    required=False, help='Show verbose finded and processed data')
args = parser.parse_args()

# Enabled logging
if (__debug__ is True):
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
else:
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logging.debug('Logging enabled!')

logging.info('Images creation started!')
generator = TextGenerator(characterListNumber=args.characterSet,
                          rowLength=args.rowLength,
                          annotationOffset=args.offset)
for i in range(args.nsamples):
    im = CreateImage(args.yolowidth, args.yoloheight, color=GetRandomColor())
    # Generate annotations on image
    im, annotations = generator.Annotate(im)
    # Create filename image and annotations
    _name, imgpath = GetNotExistingSha1Filepath(
        GetRandomSha1()+'.png', FixPath(args.output))
    txtpath = GetFilepath(imgpath) + '.txt'
    # Save image with text data
    SaveImage(im, imgpath)
    # Save annotations
    SaveAnnotations(txtpath, annotations)

logging.info('Images creation finished.')
