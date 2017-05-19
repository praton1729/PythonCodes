import cv2
import urllib2
import numpy as np
import sys

# host = "100.82.92.79:8080";
# host = "192.168.0.103:8080";
host = "192.168.234.1:80";

if len(sys.argv)>1:
	host = sys.argv[1];


# hoststr = 'http://' + host + '/video'
# hoststr = 'http://192.168.234.1/web/index.html#'
hoststr = 'http://' + host;

print("Streaming " + hoststr)

stream = urllib2.urlopen(hoststr);

bytes = '';
j = 1 ;
try:
	while True:
		
		bytes += stream.read(1024);
		a = bytes.find('\xff\xd8');
		b = bytes.find('\xff\xd9');
		if (a!=-1 and b!=-1):
			jpg = bytes[a:b+2]
			bytes = bytes[b+2:]
			i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR);
			cv2.imshow(hoststr, i);
			j += 1;
			if(np.mod(j,10)== 0):
				cv2.imwrite('frame' + str(j) +'.jpg',i);
			if(cv2.waitKey(1) == 27):
				exit(0);

except (KeyboardInterrupt, SystemExit):
	print('\nkeyboardinterrupt found!')
	print('\n...Program Stopped Manually!')
raise