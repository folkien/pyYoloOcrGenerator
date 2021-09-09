'''
Created on 17 lis 2020

@author: spasz
'''


def ToRelative(box, width, height):
    '''Rescale all coordinates
       of rect to relative.'''
    x1, y1, x2, y2 = box
    x1 = x1/width
    x2 = x2/width
    y1 = y1/height
    y2 = y2/height
    return (x1, y1, x2, y2)


def ToAbsolute(box, width, height):
    '''Rescale all coordinates of
       rect to absolute.'''
    x1, y1, x2, y2 = box
    x1 = int(x1*width)
    x2 = int(x2*width)
    y1 = int(y1*height)
    y2 = int(y2*height)
    return (x1, y1, x2, y2)


def BboxToRect(bbox):
    """
    From bounding box yolo format
    to corner points cv2 rectangle
    """
    x, y, w, h = bbox
    xmin = (x - (w / 2))
    xmax = (x + (w / 2))
    ymin = (y - (h / 2))
    ymax = (y + (h / 2))
    return xmin, ymin, xmax, ymax


def RectToBbox(rect):
    """
    From bounding box yolo format
    to corner points cv2 rectangle
    """
    xmin, ymin, xmax, ymax = rect
    x, y = (xmin+xmax)/2, (ymin+ymax)/2
    w = xmax-xmin
    h = ymax-ymin
    return x, y, w, h


def CreateAnnotationfromYoloTxt(line):
    ''' Creates Annotation from txt annote.'''
    txtAnnote = (line.rstrip('\n').split(' '))
    classNumber = int(txtAnnote[0])
    box = (float(txtAnnote[1]), float(txtAnnote[2]),
           float(txtAnnote[3]), float(txtAnnote[4]))
    box = BboxToRect(box)
    return Annotation(box, classNumber)


def CreateAnnotationfromDetection(detection):
    ''' Creates Annotation from txt annote.'''
    classNumber, confidence, box = detection
    return Annotation(box, classNumber, confidence=confidence)


class Annotation():
    '''
    classdocs
    '''

    def __init__(self,
                 box,
                 classNumber=None,
                 confidence=1.00):
        '''
        Constructor
        '''
        self.box = box
        self.confidence = confidence
        self.classNumber = classNumber

    def GetClassNumber(self):
        ''' Returns class number.'''
        return self.classNumber

    def GetClassName(self):
        ''' Returns class name.'''
        return self.className

    def GetBox(self):
        ''' Returns box.'''
        return self.box

    def GetConfidence(self):
        ''' Returns confidence.'''
        return self.confidence

    def toYoloTxt(self):
        ''' Creates txt annote from object Annotation.'''
        box = RectToBbox(self.box)
        return '%u %2.6f %2.6f %2.6f %2.6f\n' % \
            (self.classNumber,
             box[0], box[1], box[2], box[3])
