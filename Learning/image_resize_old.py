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

args = sys.argv


def main():
    filePath = args[1]
    fileList = os.listdir(filePath)
    savePath = args[2]
    if not os.path.exists(savePath):
        os.mkdir(savePath)
    cont = 0
    for file in fileList:
        img1 = Image.open(str(filePath) + u'/' + file)
        # 左右反転
        img2 = img1.transpose(Image.FLIP_LEFT_RIGHT)
        # 上下反転
        img3 = img1.transpose(Image.FLIP_TOP_BOTTOM)
        # 90°回転
        img4 = img1.transpose(Image.ROTATE_90)
        # 180°回転
        img5 = img1.transpose(Image.ROTATE_180)
        # 270°回転
        img6 = img1.transpose(Image.ROTATE_270)

        img7 = img4.transpose(Image.FLIP_LEFT_RIGHT)
        img8 = img4.transpose(Image.FLIP_TOP_BOTTOM)
        img9 = img5.transpose(Image.FLIP_LEFT_RIGHT)
        img10 = img5.transpose(Image.FLIP_TOP_BOTTOM)
        img11 = img6.transpose(Image.FLIP_LEFT_RIGHT)
        img12 = img6.transpose(Image.FLIP_TOP_BOTTOM)

        reImg1 = img1.resize((256,256))
        reImg2 = img2.resize((256,256))
        reImg3 = img3.resize((256,256))
        reImg4 = img4.resize((256,256))
        reImg5 = img5.resize((256,256))
        reImg6 = img6.resize((256,256))
        reImg7 = img7.resize((256,256))
        reImg8 = img8.resize((256,256))
        reImg9 = img9.resize((256,256))
        reImg10 = img10.resize((256,256))
        reImg11 = img11.resize((256,256))
        reImg12 = img12.resize((256,256))

        reImg1.save(str(savePath) + u'/' + str("{0:07d}".format(cont)) + '.jpg' , \
                   'JPEG' , quality = 100, optimize = True)
        cont +=1
        reImg2.save(str(savePath) + u'/' + str("{0:07d}".format(cont)) + '.jpg' , \
                   'JPEG' , quality = 100, optimize = True)
        cont +=1
        reImg3.save(str(savePath) + u'/' + str("{0:07d}".format(cont)) + '.jpg' , \
                   'JPEG' , quality = 100, optimize = True)
        cont +=1
        reImg4.save(str(savePath) + u'/' + str("{0:07d}".format(cont)) + '.jpg' , \
                   'JPEG' , quality = 100, optimize = True)
        cont +=1
        reImg5.save(str(savePath) + u'/' + str("{0:07d}".format(cont)) + '.jpg' , \
                   'JPEG' , quality = 100, optimize = True)
        cont +=1
        reImg6.save(str(savePath) + u'/' + str("{0:07d}".format(cont)) + '.jpg' , \
                   'JPEG' , quality = 100, optimize = True)
        cont +=1

        reImg7.save(str(savePath) + u'/' + str("{0:07d}".format(cont)) + '.jpg' , \
                   'JPEG' , quality = 100, optimize = True)
        cont +=1

        reImg8.save(str(savePath) + u'/' + str("{0:07d}".format(cont)) + '.jpg' , \
                   'JPEG' , quality = 100, optimize = True)
        cont +=1

        reImg9.save(str(savePath) + u'/' + str("{0:07d}".format(cont)) + '.jpg' , \
                   'JPEG' , quality = 100, optimize = True)
        cont +=1

        reImg10.save(str(savePath) + u'/' + str("{0:07d}".format(cont)) + '.jpg' , \
                   'JPEG' , quality = 100, optimize = True)
        cont +=1

        reImg11.save(str(savePath) + u'/' + str("{0:07d}".format(cont)) + '.jpg' , \
                   'JPEG' , quality = 100, optimize = True)
        cont +=1
        
        reImg12.save(str(savePath) + u'/' + str("{0:07d}".format(cont)) + '.jpg' , \
                   'JPEG' , quality = 100, optimize = True)
        cont +=1
        
# def please_call_me():
#     args = sys.argv
#     filePath = args[1]
#     fileList = os.listdir(filePath)
#     savePath = args[2]
#     if not os.path.exists(savePath):
#         os.mkdir(savePath)
    
#     for cont,file in enumerate(fileList):
#         img = Image.open(str(filePath) + u'/' + file)
#         reImg = img.resize((256,256))
#         reImg.save(str(savePath) + u'/' + str(cont) + '.jpg' , \
#                    'JPEG' , quality = 100, optimize = True)
#     # main()

if __name__ == '__main__':
    main()