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
import sys
import os
from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
import numpy as np
import predict

sys.path.append('./predict/')

if __name__ == '__main__':
    image_path = sys.argv[1]
    result_path = sys.argv[2]

    DEMENTIA_ROOT_PATH   = '../'
    DEMENTIA_DATA_PATH   = './datas'
    
    sys.path.append(DEMENTIA_ROOT_PATH + '/Pycode/inspection')
    from predict import defomationTool
    from predict import image_resize
    from predict import predict
    
    image_original_path = DEMENTIA_DATA_PATH + '/original.jpg'
    
    # 画像のオープン，余白のクロップ
    image_cropped = defomationTool.openImage(imagePath = image_path, imageOriginalPath = image_original_path)

    # 一文字づつクロップ
    crop_font_list = defomationTool.cropFont(imageCropped = image_cropped, resultPath = result_path)
    imageResizePath = image_resize.please_call_me(result_path)
    # correct_ans = predict.please_call_me(meanFilePath = DEMENTIA_DATA_PATH + '/mean.npy', imgPath = imageResizePath, modelPath = DEMENTIA_DATA_PATH + '/model.npz', labelPath = DEMENTIA_DATA_PATH + '/labels.txt')
    correct_ans = predict.please_call_me(meanFilePath = DEMENTIA_DATA_PATH + '/mean.npy', imgPath = imageResizePath, modelPath = DEMENTIA_DATA_PATH + '/model_iter_10900', labelPath = DEMENTIA_DATA_PATH + '/labels.txt')
