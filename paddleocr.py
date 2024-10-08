# -*- coding: utf-8 -*-
"""PaddleOCR.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nS7iGLOP4xTiuQ7Pp02r51J4PNNycA24
"""

!python3 -m pip install paddlepaddle-gpu

!pip install paddleocr

from paddleocr import  PaddleOCR, draw_ocr

ocr = PaddleOCR(use_angle_cls= True, lang='en')

from google.colab.patches import cv2_imshow
import cv2

img_path= '/content/invoice.png'

img= cv2.imread(img_path, -1)
cv2_imshow(img)

result = ocr.ocr(img, cls=True)

for line in result:
  print(result)

from PIL import Image, ImageDraw, ImageFont

image= Image.open(img_path).convert('RGB')

bounding_boxes= [res[0][0] for res in result]
text= [res[0][1][0] for res in result]
scores = [res[0][1][1] for res in result]

print(scores, ' + ', text, '+' ,bounding_boxes)

font= ImageFont.load_default()
im_show= draw_ocr(image, bounding_boxes, text, scores, font_path='/content/dejavu-sans-bold.ttf')
im_show= Image.fromarray(im_show)
im_show.save('output.jpg')

# To be continued ..........
