import cv2 
import numpy as np
from matplotlib import pyplot as plt

# i = cv2.imread('gudia.JPG',0);
i = cv2.imread('shivansh.JPG',0);

e = cv2.Canny(i,0,125);

plt.subplot(121);
plt.imshow(i,cmap='gray');
plt.title('original');
plt.xticks([]);
plt.yticks([]);
plt.subplot(122);
plt.imshow(e,cmap='gray');
plt.title('edges');
plt.xticks([]);
plt.yticks([]);

plt.show();