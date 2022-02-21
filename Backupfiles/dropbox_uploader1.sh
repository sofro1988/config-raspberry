#uploading to Dropbox
cd /home/pi/Dropbox-Uploader
bash dropbox_uploader.sh -s upload /home/pi/img/CL*.jpg /Cluster01
cd ..
cp /home/pi/img/*.jpg /home/pi/backup
