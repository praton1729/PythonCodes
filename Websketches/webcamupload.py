import numpy as np
from matplotlib import pyplot as plt
import cv2
import time
import boto
import boto.s3
import sys
from boto.s3.key import Key
import string

aws_id = 'AKIAIA24HZSR6QOEMURA';
aws_key = '4x9Xgln7exMvIeM+sZQcmMmEk52LA9lVar8X6bmW';

bucket_name = 'tusharsinha-cameraimages';

conn = boto.connect_s3(aws_id,aws_key);

bucket = conn.create_bucket(bucket_name,location = boto.s3.connection.Location.DEFAULT);

# cv2.namedWindow('Feed',cv2.WINDOW_NORMAL);
# cv2.resizeWindow()
i = 0;
vc = cv2.VideoCapture(1);

if vc.isOpened():
    rval, frame = vc.read();
else:
    rval = False;

while rval:
    # cv2.imshow("Feed", frame);
    x = raw_input("Wanna upload? : ");
    if(str(x)=='yes'):
        rval, frame = vc.read();
        i += 1;
        cv2.imwrite('frame' + str(i) + '.jpg',frame)
        time.sleep(5);
        testfile = "/home/praton/Desktop/Pythoncodes/Websketches/frame" + str(i) +".jpg";
        k = Key(bucket);
        k.key = 'pic' + str(i);
        k.set_contents_from_filename(testfile);
    else:
        i = i;
    ekey = cv2.waitKey(20);
    if(ekey==27):
        break;

# cv2.destroyWindow("Feed");
