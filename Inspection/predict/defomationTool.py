# -*- coding: utf-8 -*-
'''
Copyright (c) 2017 Yoshihiro Takagi

本ソフトウェアおよび関連文書のファイル（以下「ソフトウェア」）の複製、複製を使用、
複写、変更、結合、掲載、頒布、サブライセンス、販売などの行為を禁止します。

作者または著作権者は、契約行為、不法行為、またはそれ以外であろうと、ソフトウェアに
起因または関連し、あるいはソフトウェアの使用またはその他の扱いによって生じる一切の
請求、損害、その他の義務について何らの責任も負わないものとします。

'''

import sys
from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
import numpy as np

# def inclinationCorrection(image_original, x1, y1, np_x, np_y):
#     '''
#         TODO:傾き補正の実装
#         TODO:要デバッグ
#     '''
#     # 回転行列算出
#     # ( xnew ) = ( cos(θ) -sin(θ) )
#     # ( ynew )   ( sin(θ)  cos(θ) )
#     theta = np.rad2deg(np.arctan(x1/y1))  # 現在の角度
#     theta_rad = np.radians(90 - theta) # 補正のための回転角度（ラジアン法）
    
#     # 回転行列
#     rotate_matrix = np.array(                         \
#         [ np.cos(theta_rad), -1*(np.sin(theta_rad))], \
#         [ np.sin(theta_rad), np.cos(theta_rad)]       \
#                             )
#     image_original_np = np.asarray(image_original)
#     image_buff_np = np.asarray(Image.new('RGB', (np_x + 400, np_y + 400), 0)) # 傾きを考えて元データよりちょい大きい空画像を作成
#     image_original_np.flags.writable = True
#     image_buff_np.flags.writable = True

#     for y in np_y:
#         for x in np_x:
#             old_point = np.array((x, y))
#             old_point = np.reshape(old_point,(2,1))
#             new_point = rotate_matrix * old_point
#             x_new, y_new = new_point[0][0], new_point[1][0]
#             image_buff_np[y_new][x_new] = image_original_np[y][x]
    
#     image_buff = Image.fromarray(np.uint8(image_buff_np))

#     return image_buff

# def cropMargin(image_original, inclination_correction_flag = False):
#     '''
#      余白部分のクロップ
#      文字の部分（長方形の中）のみ取り出す
#      arg    : テスト画像，傾き補正のON or OFF
#      return : クロップ後テスト画像
#     '''

#     # エッジの強調，二値化
#     image_glay = image_original.filter(ImageFilter.FIND_EDGES)
#     image_glay = image_glay.convert('L')

#     # PIL -> Numpy convert
#     image_glay_np = np.asarray(image_glay)
#     np_y, np_x = image_glay_np.shape

#     # 座標保存用
#     left_line_point_1   = [] # 左直線用
#     left_line_point_2   = [] 
#     right_line_point_1  = [] # 右直線用
#     top_line_point_1    = [] # 上直線用
#     bottom_line_point_1 = [] # 下直線用

#     # 左直線調査
#     y = int(np_y/3)
#     for x in range(int(np_x/3)):
#         # point 1
#         if 100 < image_glay_np[y][x] and 100 > image_glay_np[y][x+1]:
#             left_line_point_1.append((x,y))
#         # point 2
#         if 100 < image_glay_np[y*2][x] and 100 > image_glay_np[y*2][x+1]:
#             left_line_point_2.append((x,y))
    
#     x1, y1 = left_line_point_1[2 if 2 <= len(left_line_point_1) else 1]
#     x2, _ = left_line_point_2[2 if 2 <= len(left_line_point_2) else 1]
    
#     x_l = x1

#     # 傾き補正
#     if inclination_correction_flag and x1 != x2:
#         image_original = inclinationCorrection(image_original, x1, y1, np_x, np_y)
#         # もっかい左の傾き，切片を算出しなおす
#         # エッジの強調，二値化
#         image_glay = image_original.filter(ImageFilter.FIND_EDGES)
#         image_glay = image_original.convert('L')
        
#         # PIL -> Numpy convert
#         image_glay_np = np.asarray(image_glay)
#         np_y, np_x = image_glay_np.shape

#         # 左直線調査
#         y = int(np_y/3)
#         for x in range(int(np_x/3)):
#             # point 1
#             if 100 < image_glay_np[y][x] and 100 > image_glay_np[y][x+1]:
#                 left_line_point_1.append((x,y))

#         x_l, _ = left_line_point_1[2 if 2 < len(left_line_point_1) else 1]

#     # 右直線調査
#     y = int(np_y/3)
#     for x in range(np_x-1, int(np_x/3)*2, -1):
#         # point 1
#         if 100 > image_glay_np[y][x] and 100 < image_glay_np[y][x-1]:
#             right_line_point_1.append((x,y))

#     x_r, _ = right_line_point_1[1 if 2 < len(right_line_point_1) else 0]

#     # 上直線調査
#     x = int(np_x/3)
#     for y in range(int(np_y/3)):
#         # point 1
#         if 100 < image_glay_np[y][x] and 100 > image_glay_np[y+1][x]:
#             top_line_point_1.append((x,y))

#     _, y_t = top_line_point_1[2 if 2 <= len(top_line_point_1) else 1]

#     # 下直線調査
#     x = int(np_x/3)
#     for y in range(np_y-1, int(np_y/3)*2, -1):
#         # point 1
#         if 100 > image_glay_np[y][x] and 100 < image_glay_np[y-1][x]:
#             bottom_line_point_1.append((x,y))

#     _, y_b = bottom_line_point_1[1 if 2 < len(bottom_line_point_1) else 0]

#     crop_x_start  = x_l
#     crop_y_start  = y_t
#     crop_x_end    = x_r
#     crop_y_end    = y_b
#     # print(crop_x_start, crop_y_start, crop_x_end, crop_y_end)
#     return image_original.crop((crop_x_start, crop_y_start, crop_x_end, crop_y_end))

def cropMargin(image_original):
    crop_x_start  = 170
    crop_y_start  = 375
    crop_x_end    = 2270
    crop_y_end    = 3770
    return image_original.crop((crop_x_start, crop_y_start, crop_x_end, crop_y_end))


def cropFont(imageCropped, resultPath):
    '''
        crop font
    '''

    image_size_x, image_size_y = imageCropped.size
    wordsize_x = image_size_x/26
    wordsize_y = image_size_y/28
    count = 0

    crop_font_list = []

    for hight in range(28):
        for width in range(26):
            crop_x_start = wordsize_x*width - wordsize_x/4 if 0 < wordsize_x*width - wordsize_x/4 else 0
            crop_y_start = wordsize_y*hight - wordsize_y/8 if 0 < wordsize_y*hight - wordsize_y/8 else 0
            crop_x_end   = wordsize_x*(width+1) + wordsize_x/4 if image_size_x > wordsize_x*(width+1) + wordsize_x/8 else image_size_x
            crop_y_end   = wordsize_y*(hight+1) + wordsize_y/8 if image_size_y > wordsize_y*(hight+1) + wordsize_y/8 else image_size_y
            crop = imageCropped.crop((crop_x_start, crop_y_start, crop_x_end, crop_y_end))
            crop.save(resultPath + '/' + str("{0:04d}".format(count)) + '.png')
            crop_font_list.append(resultPath + '/' + str("{0:04d}".format(count)) + '.png')
            count+=1

    return crop_font_list

def openImage(imagePath, imageOriginalPath):
    '''
        crop font image
    '''
    # 画像の展開
    image = Image.open(imagePath).convert('L')
    image_original = Image.open(imageOriginalPath).convert('L')
    image = cropMargin(image)
    image = image.resize((2550, 3500))
    image_original = cropMargin(image_original)
    image_original = image_original.resize((2550, 3500))
    # 余白のクロップ
    image_np = np.asarray(ImageOps.invert(image.filter(ImageFilter.BLUR))) & np.asarray(image_original.filter(ImageFilter.BLUR))
    image =  Image.fromarray(np.uint8(image_np))
    image = image.point(filter)
    image = ImageOps.invert(image)
    image = Image.merge('RGB',(image, image, image))
    return image

def filter(col):
    return 0 if 170 > col else 255

if __name__ == '__main__':
    image_path = sys.argv[1]
    result_path = sys.argv[2]
    image_cropped = openImage(imagePath = image_path, imageOriginalPath = 'original.png')
    crop_font_list = cropFont(imageCropped = image_cropped, resultPath = result_path)
