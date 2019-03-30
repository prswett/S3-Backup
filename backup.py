import os
import boto3
from botocore.client import Config
import sys
import time
import datetime

try:
    ACCESS_KEY_ID = 'PLACE ACCESS KEY HERE'
    ACCESS_SECRET_KEY = 'PLACE SECERET KEY HERE'
    BUCKET_NAME = 'PLACE BUCKET NAME HERE'

    s3 = boto3.resource('s3',
        aws_access_key_id = ACCESS_KEY_ID,
        aws_secret_access_key = ACCESS_SECRET_KEY,
        config=Config(signature_version='s3v4')
        )

    bucket = s3.Bucket(BUCKET_NAME)
except Exception:
    print("Sorry an error has occured. This is most likely because of an incorrect ACCESS_KEY_ID, ACCESS_SECRET_KEY, or BUCKET_NAME. Please check these fields and try again.")

def lookThroughBucket (bucket, local_path, myFilePath):
    for key in bucket.objects.all():
        mydate = time.strftime('%m/%d/%Y/%H/%M/%S', time.gmtime(os.path.getmtime(myFilePath)))
        theirdate = key.last_modified.strftime('%m/%d/%Y/%H/%M/%S')
        if(key.key == local_path and mydate < theirdate):
            return True
    return False


try:
    print("Attempting Backup")
    rootDir = '.'
    for dirName, subdirList, fileList in os.walk(rootDir):
        directory_path = dirName + "/"
        directory_path = directory_path.replace('\\', '/')
        directory_path = directory_path.replace('.', 'currentdir')
        s3.Object(BUCKET_NAME, directory_path).put()
        for fname in fileList:
            local_path  = os.path.join(dirName,fname)
            if(not lookThroughBucket(bucket,directory_path + fname,local_path)):
                s3.Object(BUCKET_NAME, directory_path + fname).put(Body=open(local_path, "rb"))
except Exception:
    print("Sorry an error has occured. This is most likely because of an incorrect ACCESS_KEY_ID, ACCESS_SECRET_KEY, or BUCKET_NAME. Please check these fields and try again.")

