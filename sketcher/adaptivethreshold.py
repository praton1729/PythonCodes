import cv2 
import numpy as np
from matplotlib import pyplot as plt

i = cv2.imread('gudia.JPG',0);

i = cv2.medianBlur(i,5);

ret,th1 = cv2.threshold(i,127,255,cv2.THRESH_BINARY);

th2 = cv2.adaptiveThreshold(i,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2);

th3 = cv2.adaptiveThreshold(i,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2);

titles = ['original','Global thresholdinng','Mean thresholding','Gaussian thresholding'];

images = [i, th1, th2, th3];

for j in xrange(4):
	plt.subplot(2,2,j+1);
	plt.imshow(images[j]);
	plt.title(titles[j]);
	plt.xticks([]);
	plt.yticks([]);

plt.show();