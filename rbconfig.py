# V 1.0.0 Raspberry configuration
import os
import del_photos
import settings
gui = open("home.txt", "r")
#Checking if user run as sudo
def check_privileges():
    if not os.environ.get("SUDO_UID") and os.geteuid() != 0:
        raise PermissionError("You need to run this script with sudo or as root.")
        exit()
def home():
    print(gui.read())
    print("Welcome, what would you like to do?")
    print("1.  Raspberry configuration")
    print("2.  Deleting photos range WIP")
    print("3.  Deleting all the photos WIP")
    print("4:  Update the sofwtare")
    pass
def menu_selection():
    while True:
        try:
            sel = int(input("Press the right numeber:  "))
            return sel
        except ValueError:
            print("Please type a number")
home()
#check_privileges()
#n = menu_selection()
while True:
    n = menu_selection()
    if n == 1:
        rb_name = input("Type the raspberry name: ")
        settings.crontab_updates()
        settings.del_rb_photos()
        settings.dhcpcd()
        settings.dropbox_rb_update()
        settings.dropbox_uploader1()
        settings.hostapd()
        settings.hostname()
        settings.hosts()
        settings.wpa_supplicant()
        settings.runscript()
        settings.restart()
    elif n == 2:
        print("Working in progress")
        #del_photos.delete_range()
        menu_selection()
    elif n == 3:
        #del_photos.delete_all()
        print("Working in progress")
        menu_selection()
    elif n == 4:
        menu_selection()
    else:
        print("Please type the right number")
        menu_selection()