import numpy as np
import cv2
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from timeit import default_timer as t

t0 = t()

src0 = Image.new('RGB', (720, 720))
width, height = src0.size

font = ImageFont.truetype('src/img/WHITRABT.TTF', size=20)
draw = ImageDraw.Draw(src0)

#tr_2 = '\n'.join([ str_entrada[ i*50 : 50*(i+1)] for i in range(barraN+1) ])
str_2 = 'dkasdkdaksdkkaddasdasdassd\nssdsasdadssdasda\\n\sadasdasdasdasd\n\asssn\n\nds'

draw.text((30, 100),str_2, font=font, fill = '#3f3')
#draw.text((290, 280),str_2[0:len(str_2)//3] , font=font, fill = '#3f3')
#src0.show()

src0 = src0.filter(ImageFilter.BoxBlur(20))
#src0.show()

draw = ImageDraw.Draw(src0)
draw.text((30, 100),str_2, font=font, fill = '#3f3')
#draw.text((290, 280),str_2[0:len(str_2)//3] , font=font, fill = '#3f3')

src = np.array(src0)


'''cv2.imshow('src',src) 

cv2.waitKey(0)
cv2.destroyAllWindows()'''

#src = cv2.GaussianBlur( src, (3,3), 0)



green_lines = np.zeros((height, width, 3), dtype='uint8')

for y in range(height):
    if y%10==0: 
        for k in range(5):
            green_lines[y-k,0:width] = ((k)*30+90,(k)*30+130,(k)*30+90)

vignette = cv2.resize(cv2.imread('src/img/vig3.png',1), (width,height))


light = cv2.resize(cv2.imread('src/img/light2.png',1), (width,height))

img = cv2.addWeighted(src, 0.7, green_lines, 0.2, 0)
img = cv2.GaussianBlur( img, (7,7), 0)

light = cv2.normalize(light, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
img = cv2.normalize(img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
vignette = cv2.normalize(vignette, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)


kk = ((light+0.4)*img*vignette*255).astype('uint8')

img = cv2.addWeighted(src, 0.3, kk, 0.9, 0)

'''cv2.imshow('src',img) 

cv2.waitKey(0)
cv2.destroyAllWindows()'''

distCoeff = np.zeros((4,1),np.float64)

# TODO: add your coefficients here!
k1 = 1.0e-6; # negative to remove barrel distortion
k2 = 1.0e-6;
p1 = 1.0e-5;
p2 = 1.0e-5;

distCoeff[0,0] = k1;
distCoeff[1,0] = k2;
distCoeff[2,0] = p1;
distCoeff[3,0] = p2;

# assume unit matrix for camera
cam = np.eye(3,dtype=np.float32)

cam[0,2] = width/2.0  # define center x
cam[1,2] = height/2.0 # define center y
cam[0,0] = 30.        # define focal length x
cam[1,1] = 30.        # define focal length y

# here the undistortion will be computed
dst = cv2.undistort(img,cam,distCoeff)

cv2.namedWindow("dst", cv2.WINDOW_NORMAL)
cv2.resizeWindow("dst", int(1*dst.shape[1]), int(1*dst.shape[0]))


dst = cv2.normalize(dst, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
print(t()-t0)

cv2.imshow('dst',dst +(0.2,0.4,0.2)*light/4)

cv2.waitKey(0)
cv2.destroyAllWindows()