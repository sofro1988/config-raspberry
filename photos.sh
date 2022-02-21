#taking pictures
raspistill -w 1280 -h 1024 -q 75 -o image.jpg
mv image.jpg /home/pi/img/$(hostname)$(date -d "today" +"%Y%m%d%H%M").jpg

