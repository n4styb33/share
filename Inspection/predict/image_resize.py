# -*- coding: utf-8 -*-
'''
Copyright (c) 2017 kishi

first argv  : Image File Directry
second argv : Save Directry
'''
import os.path
import os
import sys
from PIL import Image
from PIL import ImageOps

args = sys.argv


def please_call_me(filePath):
    fileList = os.listdir(filePath)
    fileList.sort()
    savePath = filePath + "/resize"
    if not os.path.exists(savePath):
        os.mkdir(savePath)
    
    for cont,file in enumerate(fileList):
        root, ext = os.path.splitext(file)
        if ext == '.png':
            img = Image.open(str(filePath) + u'/' + file)
            reImg = img.resize((256,256))
            reImg = reImg.crop((13,13,243,243))
            reImg = reImg.resize((256,256))
            #reImg = ImageOps.invert(reImg)
            reImg.save(str(savePath) + u'/' + str("{0:04d}".format(cont)) + '.png' , \
                    'JPEG' , quality = 100, optimize = True)
    return savePath
    # main()

