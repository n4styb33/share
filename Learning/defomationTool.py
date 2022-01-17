#-*- coding: utf-8 -*-
'''
Copyright (c) 2017 kishi

This module is an image processing function 
    for processing program of dementia diagnosis test.
'''

from PIL import Image
from PIL import ImageOps
import numpy as np
from matplotlib import pylab as plt


def ImageDformation(DEBUG = False, oriImagePath = '../../photoData/image1_ori.bmp', scanImagePath = '../../photoData/image1.bmp'):
    """Image file open and transformation"""
    # open Image
    img1Ori = Image.open(oriImagePath) # image 1 test result
    img1Scan = Image.open(scanImagePath)    # iamge 1 original image
    
    # Image binarazation
    imgArrayBinary = np.asarray(img1Scan) - np.asarray(img1Ori)
    imgPilBinary =  ImageOps.invert(Image.fromarray(np.uint8(imgArrayBinary)))

    # A word px size = 100px * 100px
    wordSize = 100
    # Test word position on test paper 2
    cropPositionImage1 = (
        ( 617,  204), ( 737,  204), ( 433,  273),
        ( 905,  273), (1131,  355), ( 666,  420),
        ( 608,  589), ( 722,  737), (1123, 1006),
        (1237, 1006), (1355, 1006), ( 497, 1067),
        ( 489, 1387), ( 957, 1387), ( 435, 1453),
        (  91, 1526), ( 213, 1526), ( 565, 1600),
        (1009, 1723), ( 837, 1797), (1229, 1797),
        ( 207, 2020), ( 197, 2105), ( 965, 2105),
        (1361, 2105))

    # Test word position on test paper1
    #cropPositionImage2= ()
    # Cropped image file list
    cropImageListImage1 = [] # cropped images of Image1
    #cropImageListImage2 = []  # cropped images of Image2 
    # crop Image
    for count,i in enumerate(cropPositionImage1):
        x,y = i # crop position
        # crop (x_start_pos, y_start_pos, x_end_pos , y_end_pos)
        cropImg = imgPilBinary.crop((x, y, x + wordSize, y + wordSize)) 
        #cropImageListImage1.append(cropImg)
        #cropImg.resize((100, 100)).save('../../photoData/crop2/a'+str(count)+'.png')
        cropImg.convert('RGB')
        cropImg.resize((256, 256)).save('../photoData/crop2/'+str(count)+'.jpg')

    
    # show images (debug) 
    if DEBUG:
        print("DEBUG MODE Enable")
        #plt.imshow(cropImg)
        plt.imshow(imgPilBinary)
        plt.show()

def please_call_me():
    ImageDformation(DEBUG = True, oriImagePath = '../../photoData/image1_ori.bmp', scanImagePath = '../../photoData/image1.bmp')
    print("('・ω・`)")
