#
#
#This script changes the wallpaper at set times based on the command line
#arguement
#
#also changes the color of the terminal to gray or smth
#cmd line arguments upper bound hr lowerbound hr
#
import sys
import os
import datetime
if sys.version_info[0] <3:
    raise BaseException('Run in python3')
image1_dir="~/Pictures/qe2inu65ag471.png"
image2_dir="~/Pictures/xe5fbhxvbd571.png"

if len(sys.argv) ==1:
    lbound=datetime.datetime.now().replace(hour=8,minute=0)

    hbound=datetime.datetime.now().replace(hour=23,minute=0)
elif len(sys.argv) ==3:
    if((int(sys.argv[1])) < (int(sys.argv[2]))<24):
        lbound=datetime.datetime.now().replace(hour=int(sys.argv[1]),minute=0)

        hbound=datetime.datetime.now().replace(hour=int(sys.argv[2]),minute=0)
    else:
        RaiseException("Bounds aren't correct")
else:
    RaiseException("Wrong number of arguments")
def set_wallpaper(img):
    #time is the morning time
    cmd="feh --bg-scale {}".format(img)

    os.system(cmd) 
def change_bar(state):
    cmd="polybar example -c /home/arnav/.config/polybar/config{}".format(state)
    os.system("killall polybar")
    os.system(cmd)


nochange= True
while True:
    now =datetime.datetime.now()
    if hbound>now and lbound<now:
        if nochange:
            continue
        else:
            set_wallpaper(image1_dir)
            change_bar("")
            nochange=True
    else:
        if not nochange:
            continue
        else:
            set_wallpaper(image2_dir)
            change_bar("2")
            nochange=False


