import numpy as np
import cv2

#Load image in grayscale 
im=cv2.imread('SutetCat.jpg',0)

#Get image size h & w
h,w = im.shape[:2]

#Set threshold number
th=0.7

#Let image as array
i=np.array(im)

#Using double data type
i=np.float64(im)/255 

#Thresholding
i[i>th]=1
i[i<=th]=0

#Back to uint8 data type
imth=np.uint8(i)*255 

#Show thresholding image
th=np.hstack((im,imth))
cv2.imshow('Thresholding',th)

#press ESC to exit
k=cv2.waitKey(0)
if k == 27:
        cv2.destroyAllWindows()
