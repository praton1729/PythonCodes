import cv2
import numpy as np
from matplotlib import pyplot as plt

ci = cv2.imread('gudia.JPG',1);
# cv2.imshow('FRAME',ci)
# cv2.waitKey(0);
# cv2.destroyAllWindows();

i = cv2.cvtColor(ci, cv2.COLOR_RGB2GRAY);
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image',i);
# cv2.waitKey(0);
# cv2.destroyAllWindows();

ret,thresh1 = cv2.threshold(i,127,255,cv2.THRESH_BINARY);
ret,thresh2 = cv2.threshold(i,127,255,cv2.THRESH_BINARY_INV);
ret,thresh3 = cv2.threshold(i,127,255,cv2.THRESH_TRUNC);
ret,thresh4 = cv2.threshold(i,127,255,cv2.THRESH_TOZERO);
ret,thresh5 = cv2.threshold(i,127,255,cv2.THRESH_TOZERO_INV);

titles = ['original','binary','inverted binary','truncated','to zero','inverted to zero'];
images = [i,thresh1,thresh2,thresh3,thresh4,thresh5];

for j in xrange(6):
	plt.subplot(2,3,j+1);
	plt.imshow(images[j],'gray');
	plt.title(titles[j]);
	plt.xticks([]);
	plt.yticks([]);

plt.show();
