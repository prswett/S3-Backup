Hi There :)

Please follow the below instructions to build and run the program:

---Important Notice---
For this project I was testing and using it with Windows 10
Please make sure to have python 3.6.7+ downloaded before trying to run the program. Any version after this
should also work although I am not sure what versions before it will work as I used 3.6.7 to create and run
my version. This will handle the default imports such as date,time, sys, and os. Please also make sure to have 
boto3 version 10+ downloaded as you will need this to use the amazon python api. I will attach the download links
below just in case for some reason you do not already have them downloaded.
Python : https://www.python.org/downloads/
Boto3 : https://github.com/boto/boto3
---Important Notice---

1. Please make sure to enter your amazon access key, secret key, and bucket name you wish to save into. You can
do this by opening up backup.py the python script(notepad works). At the top of the script you will see the fields
ACCESS_KEY_ID = 'PLACE ACCESS KEY HERE'
ACCESS_SECRET_KEY = 'PLACE SECERET KEY HERE'
BUCKET_NAME = 'PLACE BUCKET NAME HERE'
Please enter your information between the following quotations as this is where the program will look for your
login and bucket information

2. Place the backup.py file in the directory that you would like to copy into the cloud. It will save everything
in and under the current directory into the s3 bucket and mimic the files and folders that you currently see. The only
difference will be that the starting directory that the backup.py file is currently in will be called currentdir
in the amazon bucket and will be your top level folder in your s3.

3. To run the program open your cmd window and navigate to the current directory that the backup.py file is 
located. Once you are in the current directory that contains the backup.py file you can type the command
"python backup.py" without the quotation marks which will run the program from that current directory.

Additional Notes: I believe you can also just double click the "backup.py script once you have the above installed
as I tried it a couple times and it seemed to work. If this doesn't work just default back to using the cmd commands
in step 3