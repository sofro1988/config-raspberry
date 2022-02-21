#deleting photos
import subprocess
import datetime
def delete_all():
    sel2 = input("Are you sure? Do you want to delete every photo? N/y ")
    if sel2 == "y":
        subprocess.run(["rm -Rf /home/pi/photos/*", "rm -Rf /home/pi/backup/*"])
        print("All the photos were deleted")
    else:
        pass
def delete_range():
    format = '%Y%m%d'
    while True:
        startdate = input("Range starting? format YYYYMMDD: ")
        try:
            checkdate = datetime.datetime.strptime(startdate,format)
            break
        except ValueError:
            print("Incorrect data format, should be YYYYMMDD")
    while True:
        finishdate = input("Range over? format YYYYMMDD: ")
        try:
            checkdate = datetime.datetime.strptime(finishdate,format)
            break
        except ValueError:
            print("Incorrect data format, should be YYYYMMDD")
    rlst = range(int(startdate),int(finishdate),1)
    rlst2 = []
    for i in rlst:
        a=str(i)
        try:
            datetime.datetime.strptime(a,format)
            rlst2.append(a)
        except ValueError:
            continue
    for n in rlst2:
        subprocess.run(["rm -Rf /home/pi/photos/" + n + "*"])


    print("All the photos in the range were deleted")
