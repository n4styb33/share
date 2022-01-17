import sys
import cv2
from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
import numpy as np

def cropMargin(image_original):
    print('crop state')
    x,y = image_original.size
    crop_x_start  = 0
    crop_y_start  = 0
    crop_x_end    = x/4
    crop_y_end    = y
    print('crop end')
    return image_original.crop((crop_x_start, crop_y_start, crop_x_end, crop_y_end))

def zero_one(image):

    output_width = 620 #横文字数
    font_aspect = 1.0 #縦pixel調整
    ikichi = 180

    im_gray = cv2.imread(image, 0)#グレー化

    height = im_gray.shape[0] #高さの取得
    width = im_gray.shape[1] #幅の取得

    if width > output_width: #出力幅より写真が大きいとき
        im_resized = cv2.resize(im_gray,(output_width,int((output_width/width)*height/font_aspect)))
    else:
        im_resized = cv2.resize(im_gray,(width,int(height/font_aspect)))

    ret,th = cv2.threshold(im_resized, ikichi, 255, cv2.THRESH_BINARY) #二値化

    th[th != 0] = 1 #この場合白色部分は1に変換

    f = open('..\imageresize\write.txt', 'w') #読み込み開始

    for array in th: #各行について

        row = map(str,array)

        line = "".join(row)

        line.replace("[","")
        line.replace("]","")
        line.replace(" ","")
        f.write(line)
        f.write("\n")

    f.close() #閉じる

def write(file):
    counter = 0
    file = open('..\imageresize\write.txt','r')
    Allf = file.read()

    text = Allf.replace('\n','')
    lines = text.replace('\r','')

    for line in lines:
        if line.find("1"): #>= 0
            break
        else :
            counter += 1
            #print (counter)
    width = counter % 620
    hight = counter //620

    #620はimage.pyの横文字数が620の場合
    print ('width={0}'.format(width)) #横
    print ('hight={0}'.format(hight)) #縦

    #affine文
    print('affin state')
    img = cv2.imread(sys.argv[1],1)
    #rows,cols = img.shape
    size = tuple(np.array([img.shape[1], img.shape[0]]))
    move_x = width - 123
    move_y = hight - 343

    M = np.float32([[1,0,move_x],[0,1,move_y]])
    img_afn = cv2.warpAffine(img,M,size)

    # 表示
    cv2.imwrite('affine.jpg', img_afn)
    print('affin end')
#def affine(img):

    #rows,cols = img.shape
    #move_x = output_hight - 190
    #move_y = output_width - 123

    #M = np.float32([[1,0,move_x],[0,1,move_y]])
    #img_afn = cv2.warpAffine(move_img,M,(cols,rows))

    # 表示
    #cv2.imwrite('affine.jpg', img_afn)

print("start")

if __name__ == '__main__':
    image_path = sys.argv[1]
    img = cropMargin(Image.open(image_path))
    img.save('croped.jpg')
    zero_one("croped.jpg")
    write(open('write.txt','r'))
    #affine(cv2.imread(sys.argv[1],0))

print('end')
