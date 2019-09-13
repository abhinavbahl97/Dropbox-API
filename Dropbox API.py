
import dropbox
import time
import os

access_token = '******'

def uploadfile(source_file, destination_file):
	dbx = dropbox.Dropbox(access_token)
	start = time.time()
	with open(source_file, 'rb') as f:
		dbx.files_upload(f.read(), destination_file)
	end = time.time()
	duration = (end-start)/1000
	bitsloaded = os.path.getsize(source_file)*8
	speedBps = (bitsloaded / duration);
	speedKbps = (speedBps / 1024);
	speedMbps = (speedKbps / 1024);
	print ("Your approximate upload speed is:", speedKbps, " Kilobits per second",
			" or ", speedMbps, " Megabits per second!\n")

def downloadfile(source_file, destination_file):
	dbx = dropbox.Dropbox(access_token)
	start = time.time()
	os.chmod(source_file, 0o777)
	with open(source_file, 'wb') as f:
		metadata, res = dbx.files_download(destination_file)
		f.write(res.content) 
	end = time.time()
	duration = (end-start)/1000
	bitsloaded = os.path.getsize(source_file)*8
	speedBps = (bitsloaded / duration);
	speedKbps = (speedBps / 1024);
	speedMbps = (speedKbps / 1024);
	print ("Your approximate download speed is:", speedKbps, " Kilobits per second",
			" or ", speedMbps, " Megabits per second!\n")

def main():

	upload_source_file =  '/Data.docx'
	upload_destination_file = '/Destination.docx'

	download_source_file  = '/Data.txt'
	download_destination_file = '/Destination.docx'

	downloadfile(download_source_file, download_destination_file)
	uploadfile(upload_source_file, upload_destination_file);


if __name__ == '__main__':
    main()
