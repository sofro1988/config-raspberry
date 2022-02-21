#V 1.0.0 Raspberry configuration
import fileinput
import subprocess
from rbconfig import rb_name
#updating crontab
def crontab_updates ():
    cl_name = rb_name[0:4]
    for line in fileinput.input("crontab_update.sh", inplace=True):
        line = line.rstrip()
        if keyword in line:
            line = line.replace(keyword, cl_name)
        print(line)
#updating del_rb_photos
def del_rb_photos ():
    cl_name = rb_name[0:4]
    for line in fileinput.input("del_rb_photos.sh", inplace=True):
        line = line.rstrip()
        if keyword in line:
            line = line.replace(keyword, cl_name)
        print(line)
#updating dhcpcd
def dhcpcd ():
    ip = "192.168.8.1"
    cl_name = int(rb_name[5:6])
    l = rb_name [6:7]
    if cl_name == 1:
        return dhcpcd()
    elif cl_name == 2:
        if l == "A":
            for line in fileinput.input("dhcpcd.conf", inplace=True):
                line = line.rstrip()
                if ip in line:
                    line = line.replace(ip, "192.168.8.2")
                print(line)
        else:
            for line in fileinput.input("dhcpcd.conf", inplace=True):
                line = line.rstrip()
                if ip in line:
                    line = line.replace(ip, "192.168.8.3")
                print(line)
    elif cl_name == 3:
        if l == "A":
            for line in fileinput.input("dhcpcd.conf", inplace=True):
                line = line.rstrip()
                if ip in line:
                    line = line.replace(ip, "192.168.8.4")
                print(line)
        else:
            for line in fileinput.input("dhcpcd.conf", inplace=True):
                line = line.rstrip()
                if ip in line:
                    line = line.replace(ip, "192.168.8.5")
                print(line)
    elif cl_name == 4:
        if l == "A":
            for line in fileinput.input("dhcpcd.conf", inplace=True):
                line = line.rstrip()
                if ip in line:
                    line = line.replace(ip, "192.168.8.6")
                print(line)
        else:
            for line in fileinput.input("dhcpcd.conf", inplace=True):
                line = line.rstrip()
                if ip in line:
                    line = line.replace(ip, "192.168.8.7")
                print(line)
    elif cl_name == 5:
        if l == "A":
            for line in fileinput.input("dhcpcd.conf", inplace=True):
                line = line.rstrip()
                if ip in line:
                    line = line.replace(ip, "192.168.8.8")
                print(line)
        else:
            for line in fileinput.input("dhcpcd.conf", inplace=True):
                line = line.rstrip()
                if ip in line:
                    line = line.replace(ip, "192.168.8.9")
                print(line)
    elif cl_name == 6:
        if l == "A":
            for line in fileinput.input("dhcpcd.conf", inplace=True):
                line = line.rstrip()
                if ip in line:
                    line = line.replace(ip, "192.168.8.10")
                print(line)
        else:
            for line in fileinput.input("dhcpcd.conf", inplace=True):
                line = line.rstrip()
                if ip in line:
                    line = line.replace(ip, "192.168.8.11")
                print(line)
#updating dropbox_rb_update
def dropbox_rb_update ():
    cl_name = rb_name[0:4]
    for line in fileinput.input("dropbox_rb_update.sh", inplace=True):
        line = line.rstrip()
        if keyword in line:
            line = line.replace(keyword, cl_name)
        print(line)
#updating dropbox_uploader1
def dropbox_uploader1 ():
    cl_name = rb_name[2:4]
    clu = "01"
    for line in fileinput.input("dropbox_uploader1.sh", inplace=True):
        line = line.rstrip()
        if clu in line:
            line = line.replace(clu, cl_name)
        print(line)
#updating hostapd
def hostapd ():
    cl_name = rb_name[3:4]
    clu = "Redmigp"
    new_clu = clu+cl_name
    if cl_name == 1:
        return hostapd()
    else:
        for line in fileinput.input("hostapd.conf", inplace=True):
            line = line.rstrip()
            if clu in line:
                line = line.replace(clu, new_clu)
            print(line)
#updating hostname
def hostname ():
    for line in fileinput.input("hostname", inplace=True):
        line = line.rstrip()
        if keyword2 in line:
            line = line.replace(keyword2, rb_name)
        print(line)
#updating hosts
def hosts ():
    cl_name = rb_name[0:4]
    for line in fileinput.input("hosts", inplace=True):
        line = line.rstrip()
        if keyword3 in line:
            line = line.replace(keyword3, rb_name)
        print(line)
    for line in fileinput.input("hosts", inplace=True):
        line = line.rstrip()
        if keyword in line:
            line = line.replace(keyword, cl_name)
        print(line)
#updating wpa_supllicant
def wpa_supplicant ():
    cl_name = rb_name[3:4]
    clu = "Redmigp"
    new_clu = clu + cl_name
    if cl_name == 1:
        return wpa_supplicant()
    else:
        for line in fileinput.input("wpa_supplicant.conf", inplace=True):
            line = line.rstrip()
            if clu in line:
                line = line.replace(clu, new_clu)
            print(line)
#copy the files to rb
def runscript ():
    subprocess.run(["cp -f crontab_update.sh /home/pi/","cp -f del_rb_photos.sh /home/pi/",
                    "cp -f dhcpcd.conf /etc/","cp -f dnsmasq.conf /etc/","cp -f hostapd.conf /etc/hostapd/",
                    "cp -f hosts /etc/","cp -f hostname /etc/",
                    "cp -f photos.sh /home/pi/","cp -f wpa_supplicant.conf /etc/wpa_supplicant/",
                    "cp -f dropbox_rb_update.sh /home/pi/",
                    "cp -f dropbox_uploader1.sh /home/pi/","cp -f .dropbox_uploader /home/pi/"])
    print("Well done!")
    pass
def CopySTDfiles ():
    subprocess.run(["cp -f Backupfiles/crontab_update.sh crontab_update.sh"])
    pass
#reboot to apply settings
def restart ():
    a = input("Please press a key to reboot the raspberry  ")
    if a == "y":
        subprocess.run(["sudo reboot"])
    else:
        restart()
keyword = "CL01"
keyword2 = "CL0101A"
keyword3 = "127.0.1.1 CL0101A"

