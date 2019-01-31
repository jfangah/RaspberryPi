cd /home/pi/Desktop
echo "start"
raspistill -t 2000 -w 640 -h 480 -o - > my_life.jpg
cd /home/pi/Desktop
echo "upload"
bypy syncup
echo "end"
