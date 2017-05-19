import boto
import boto.s3
import sys
from boto.s3.key import Key

aws_id = 'AKIAIA24HZSR6QOEMURA';
aws_key = '4x9Xgln7exMvIeM+sZQcmMmEk52LA9lVar8X6bmW';

bucket_name = aws_id.lower() + '-cameraupload';

conn = boto.connect_s3(aws_id,aws_key);

bucket = conn.create_bucket(bucket_name,location = boto.s3.connection.Location.DEFAULT);

testfile = "/home/praton/Desktop/Pythoncodes/Websketches/frame10.jpg";
print("uploading %s to %s bucket"%(testfile,bucket_name));

def percent_cb(complete, total):
    sys.stdout.write('.');
    sys.stdout.flush();

k = Key(bucket);

k.key = 'my second pic';

k.set_contents_from_filename(testfile,cb = percent_cb, num_cb = 10);
