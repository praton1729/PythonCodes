#!/usr/bin/env python
import cv2
import time
import boto
import boto.s3
import sys
from boto.s3.key import Key
import string
from datetime import datetime

aws_id = 'AKIAIA24HZSR6QOEMURA';
aws_key = '4x9Xgln7exMvIeM+sZQcmMmEk52LA9lVar8X6bmW';

bucket_name = 'tusharsinha-cameraimages';

conn = boto.connect_s3(aws_id,aws_key);

existence = conn.lookup(bucket_name);

if(existence is None):
    bucket = conn.create_bucket(bucket_name,location = boto.s3.connection.Location.DEFAULT);
else:
    bucket = conn.get_bucket(bucket_name);

vc = cv2.VideoCapture(1);
if vc.isOpened():
    rval, frame = vc.read();
else:
    rval = False;

if(rval == True):
    rval, frame = vc.read();
    ctime = str(datetime.now().time());
    cv2.imwrite('frame:' + ctime + '.jpg',frame);
    time.sleep(2);
    testfile = '/home/praton/Desktop/Pythoncodes/Websketches/frame:' + ctime +'.jpg';
    k = Key(bucket);
    k.key = 'pic:' + ctime;
    k.set_contents_from_filename(testfile);
