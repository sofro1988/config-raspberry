#V 1.0.1
#copying crontab settings to others raspberry
crontab -l > /home/pi/crontab.bak
sshpass -p Rucola01! scp /home/pi/crontab.bak pi@CL0102A:/home/pi
sshpass -p Rucola01! ssh pi@CL0102A crontab /home/pi/crontab.bak
sshpass -p Rucola01! scp /home/pi/crontab.bak pi@CL0102S:/home/pi
sshpass -p Rucola01! ssh pi@CL0102S crontab /home/pi/crontab.bak
sshpass -p Rucola01! scp /home/pi/crontab.bak pi@CL0103A:/home/pi
sshpass -p Rucola01! ssh pi@CL0103A crontab /home/pi/crontab.bak
sshpass -p Rucola01! scp /home/pi/crontab.bak pi@CL0103S:/home/pi
sshpass -p Rucola01! ssh pi@CL0103S crontab /home/pi/crontab.bak
sshpass -p Rucola01! scp /home/pi/crontab.bak pi@CL0104A:/home/pi
sshpass -p Rucola01! ssh pi@CL0104A crontab /home/pi/crontab.bak
sshpass -p Rucola01! scp /home/pi/crontab.bak pi@CL0104S:/home/pi
sshpass -p Rucola01! ssh pi@CL0104S crontab /home/pi/crontab.bak
sshpass -p Rucola01! scp /home/pi/crontab.bak pi@CL0105A:/home/pi
sshpass -p Rucola01! ssh pi@CL0105A crontab /home/pi/crontab.bak
sshpass -p Rucola01! scp /home/pi/crontab.bak pi@CL0105S:/home/pi
sshpass -p Rucola01! ssh pi@CL0105S crontab /home/pi/crontab.bak
sshpass -p Rucola01! scp /home/pi/crontab.bak pi@CL0106A:/home/pi
sshpass -p Rucola01! ssh pi@CL0106A crontab /home/pi/crontab.bak
sshpass -p Rucola01! scp /home/pi/crontab.bak pi@CL0106S:/home/pi
sshpass -p Rucola01! ssh pi@CL0106S crontab /home/pi/crontab.bak
