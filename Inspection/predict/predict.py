# -*- coding: utf-8 -*-
'''
Copyright (c) 2017 Yoshihiro Takagi

本ソフトウェアおよび関連文書のファイル（以下「ソフトウェア」）の複製、複製を使用、
複写、変更、結合、掲載、頒布、サブライセンス、販売などの行為を禁止します。

作者または著作権者は、契約行為、不法行為、またはそれ以外であろうと、ソフトウェアに
起因または関連し、あるいはソフトウェアの使用またはその他の扱いによって生じる一切の
請求、損害、その他の義務について何らの責任も負わないものとします。

ソフトウェアはオープンソースプロジェクトのライブラリを使用しております。
開発者の方々に謝意を表します。

'''
from __future__ import print_function
import argparse
import datetime
import json
import multiprocessing
import random
import sys
import os
import threading
import time

import numpy as np
from PIL import Image

import six
import pickle
from six.moves import queue

import chainer
import matplotlib.pyplot as plt
import numpy as np
import math
import chainer.functions as F
import chainer.links as L
from chainer.links import caffe
from matplotlib.ticker import *
from chainer import serializers

from imagenet import nin



# prediction image
ans = (
    2, 2, 1, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3,
    3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2 ,2, 2,
    2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3,
    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
    3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 0, 2,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
    3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 1, 2, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
    3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
    3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3
)

def readImages(path, cropwidth, insize, imgMean):
    '''
        read image multiple function
    '''
    dirList = os.listdir(path)
    file_name = []
    imgList = []
    imgNp = []
    # Acquire image path only
    for file in dirList:
        _, ext = os.path.splitext(file)
        if '.jpg' == ext or '.bmp' == ext or '.png' == ext:
            file_name.append(file)
            imgList.append(path + '/' + file)
            imgNp.append(np.asarray(Image.open(path + '/' + file)).transpose(2, 0, 1))
            #print(file)

    # load image (random crop)
    top = random.randint(0, cropwidth - 1)
    left = random.randint(0, cropwidth - 1)
    bottom = insize + top
    right = insize + left

    # neam image subtraction
    imgNpCrop = []
    for img in imgNp:
        img = img[:, top:bottom, left:right] - imgMean[:, top:bottom, left:right]
        imgBuff = img / 255
        imgNpCrop.append(imgBuff)

    return imgNpCrop,file_name

def predict(net,x):
    '''
        prediction image
    '''
    h = F.max_pooling_2d(F.relu(net.mlpconv1(x)), 3, stride=2)
    h = F.max_pooling_2d(F.relu(net.mlpconv2(h)), 3, stride=2)
    h = F.max_pooling_2d(F.relu(net.mlpconv3(h)), 3, stride=2)
    h = net.mlpconv4(F.dropout(h))
    h = F.reshape(F.average_pooling_2d(h, 6), (x.data.shape[0], 1000))
    return F.softmax(h)

def mainMultiple(meanFilePath, imgPath, modelPath, labelPath):
    '''
        main function multiple mode
    '''
    # model
    model = nin.NIN()
    model.compute_accuracy = False

    # read images
    mean_image = np.load(meanFilePath)
    imgList,file_name = readImages(imgPath, (256 - model.insize), model.insize, mean_image)

    # setup optimizer
    optimizer = chainer.optimizers.Adam()
    optimizer.setup(model)

    # load serializer (learned network)
    # serializers.load_hdf5(modelPath,model)
    serializers.load_npz(modelPath,model)

    # model to cpu
    model.to_cpu()
    inspection_ans = []

    categories = np.loadtxt(labelPath, str, delimiter='\t')
    for image_num,img in enumerate(imgList):
        x = np.ndarray((1,3,model.insize,model.insize),dtype=np.float32)
        x[0] = img
        x = chainer.Variable(np.asarray(x))
        score = predict(model,x)
        top_k = 20
        prediction_zip = zip(score.data[0].tolist(), categories)
        prediction = list(prediction_zip)
        print(file_name[image_num])
        print('%d' % (ans[image_num]))
        inspection_num = 0
        inspection_score = 0
        for rank, (score, name) in enumerate(prediction[:top_k], start=1):
            print('#%d | %s | %4.1f%%' % (rank, name, score * 100))
            if score*100 > inspection_score:
                inspection_num = rank-1
                inspection_score = score*100
                if 30 > inspection_score:
                    inspection_num = 2
        print(' ')
        if 3 == ans[image_num]:
            inspection_num = 3
        inspection_ans.append((inspection_num,inspection_score))

    return inspection_ans


def please_call_me(meanFilePath = '', imgPath = '', modelPath = '', labelPath = ''):
    if '' == imgPath or '' == modelPath:
        print('Path Error')
        return

    inspection_ans = mainMultiple(meanFilePath, imgPath, modelPath, labelPath)

    # for debug
    correct_ma = 0
    correct_ba = 0
    mimatigai = 0
    print('　   正解   　判定')
    for (i,answer) in enumerate(inspection_ans):
        print('%d   %d       %d'%(i, ans[i], answer[0]))
        if 2 == ans[i] and ( 0 == answer[0] or 1 == answer[0]):
            mimatigai +=1
        elif 2 > ans[i] and ans[i] == answer[0]:
            if ans[i] == 0:
                correct_ma += 1
            elif ans[i] == 1:
                correct_ba += 1

    print('正解丸  %d / 12' % (correct_ma))
    print('正解罰  %d / 13' % (correct_ba))
    print('見間違  %d / 557' % (mimatigai))

    #return str(correct) + ' / 582'
    return 0

if __name__ == "__main__":
    please_call_me(meanFilePath = sys.argv[1], imgPath = sys.argv[2], modelPath = sys.argv[3], labelPath = sys.argv[4])

