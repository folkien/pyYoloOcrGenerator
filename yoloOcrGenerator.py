
#!/usr/bin/python3
import logging
import argparse
import sys
from helpers.images import CreateImage, SaveImage
from helpers.files import RenameToSha1Filepath, FixPath, GetFilepath

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
parser.add_argument('-v', '--verbose', action='store_true',
                    required=False, help='Show verbose finded and processed data')
args = parser.parse_args()

# Enabled logging
if (__debug__ is True):
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
else:
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logging.debug('Logging enabled!')

for i in range(args.nsamples):
    im = CreateImage(args.yolowidth, args.yoloheight)
    # Draw text on image

    # Create filename image and annotations
    imgpath = RenameToSha1Filepath('1.png', FixPath(args.output))
    txtpath = GetFilepath(imgpath) + '.txt'
    # Save image with text data
    SaveImage(im, imgpath)
    # Save annotations