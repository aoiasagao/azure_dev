# 参考にしたサイト
# https://code-graffiti.com/blending-images-with-opencv-in-python/
# https://www.mathpython.com/ja/opencv-image-add/
# https://qiita.com/Gyutan/items/5e62420cc8f6bb106bed

# 画像合成関連のimport
import cv2
import matplotlib.pyplot as plt
import numpy as np

# pdf変換関連のimport
from pathlib import Path
from pdf2image import convert_from_path


# PDFファイルのパス
pdf_path = Path("pdf-PDF-Invoice3.pdf")


#この1文で変換されたjpegファイルが、imageホルダー内に作られます。
#convert_from_path(pdf_path, output_folder='./' ,fmt='jpeg',output_file='henkan_gazou.jpg')

# PDFをImage に変換(pdf2imageの関数)
pages = convert_from_path(pdf_path)

# 画像ファイルが１ページだけある前提で保存
for i, page in enumerate(pages):
    page.save("henkan_gazou.jpg", fmt='jpeg')



# 画像の読み込み
img1 = cv2.imread('henkan_gazou.jpg') # 元画像
img2 = cv2.imread('gazou_add.png') # 合成したい小さい画像

# 画像のサイズを確認
print(img1.shape)
print(img2.shape)

# 画像のサイズを変更（お好みで）
img2 =cv2.resize(img2,(300,300))


'''
yt:yb,xl:xr
yt ... y 座標の上
yb ... y 座標の下
xl ... x 座標の左
xr ... x 座標の右
'''
height, width = img2.shape[:2]
img1[250:height+250, 1000:width+1000] = img2

cv2.imwrite('new.jpg', img1)




