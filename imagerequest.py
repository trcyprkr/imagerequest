import telegram
import cv2
import streamlink
import os
import time
import datetime as dt
import requests
from screeninfo import get_monitors
for m in get_monitors():
    #print(str(m))
    monitor = m
    w = monitor.width
    h = monitor.height

TELEGRAM_BOT_TOKEN = '5312xxxxxxxxxxxxxxxxxxxxxx'
TELEGRAM_CHAT_ID = '-10xxxxxxxxxxxxxx'
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

def get_sleeptime(minute, second):
    now = dt.datetime.now()
    sched = now.replace(minute=minute, second=second)
    sleeptime = (sched - now).total_seconds()
    if sleeptime < 0:
        sleeptime += 3600
    return sleeptime
    
path = 'images/slideshow/'
dim = (w, h)
r = time.localtime()
hr = r.tm_hour
m = r.tm_min
s = r.tm_sec
#####################################################################
burl = [
    'https://copyrighted.seejh.com/townsquarecache/townsquarecache.jpg',
    'https://copyrighted.seejh.com/townsquare/townsquare.jpg',
    'https://copyrighted.seejh.com/townsquarebw/townsquarebw.jpg',
    'https://www.nps.gov/webcams-glac/ApgarVillage.jpg',
    'https://wingsvirtualtours.com/webcams/missoula_valley/public_html/cam/streaming/mp/current.jpg',
    'https://coloradowebcam.net/webcam/aspenmtn/current.jpg',
    'https://coloradowebcam.net/webcam/boulder/current.jpg',
    'https://coloradowebcam.net/webcam/sopris/current.jpg',
    'https://www.nps.gov/webcams-romo/glacier_basin.jpeg',
    'https://coloradowebcam.net/webcam/pikespeak/current.jpg',
    'https://live5.brownrice.com/cam-images/wolfcreeksummit.jpg',
    'https://coloradowebcam.net/webcam/ouraynet-town/current.jpg',
    'https://www.nps.gov/webcams-romo/longs_peak.jpg',
    'https://pixelcaster.com/live/yosemite/halfdome.jpg',
    'https://s3.us-west-2.amazonaws.com/public.pixelcaster.com/snapshots/grandcanyon-2/latest.jpg',
    'https://www.nps.gov/webcams-romo/alpine_visitor_center.jpg',
    'https://www.nps.gov/webcams-glac/ApgarLookout-01.jpg',
    'http://stl.seejh.com/tetonrange/tetonrange.jpg',
    'https://copyrighted.seejh.com/dornans/dornans.jpg',
    'https://copyrighted.seejh.com/jennylake/jennylake.jpg',
    'https://livefromiceland.is/posters/akureyri.jpg',
    'https://www.nps.gov/webcams-glac/MiddleForkBridge.jpg',
    'https://www.nps.gov/webcams-glac/TwoMedicinePTZ.jpg',
    'https://www.nps.gov/webcams-glac/StMaryPTZ.jpg'
    ]
length = len(burl)
i = 0
#####################################################################
name = [
        'Jacksonsquare1',
        'Jacksonsquare2',
        'Jacksonsquarebw',
        'ApgarVillage',
        'missoula',
        'aspen',
        'boulder',
        'sopris',
        'glacierbasin',
        'woodlandpark',
        'pagosasprings',
        'ouray',
        'longspeak',
        'halfdome',
        'grandcanyon',
        'alpine_visitor_center',
        'ApgarLookout',
        'tetonrange',
        'dornans',
        'jennylake',
        'akureyri',
        'MiddleForkBridge',
        'TwoMedicinePTZ',
        'StMaryPTZ'
        ]
#####################################################################
place = [
        'images/slideshow/townsquarecache.jpg',
        'images/slideshow/townsquare.jpg',
        'images/slideshow/townsquarebw.jpg',
        'images/slideshow/ApgarVillage.jpg',
        'images/slideshow/missoula.jpg',
        'images/slideshow/aspen.jpg',
        'images/slideshow/boulder.jpg',
        'images/slideshow/sopris.jpg',
        'images/slideshow/glacierbasin.jpg',
        'images/slideshow/woodpark.jpg',
        'images/slideshow/pagosa.jpg',
        'images/slideshow/ouray.jpg',
        'images/slideshow/longpeak.jpg',
        'images/slideshow/halfdome.jpg',
        'images/slideshow/grandcanyon.jpg',
        'images/slideshow/alpine_visitor_center.jpg',
        'images/slideshow/ApgarLookout.jpg',
        'images/slideshow/tetonrange.jpg',
        'images/slideshow/dornans.jpg',
        'images/slideshow/jennylake.jpg',
        'images/slideshow/akureyri.jpg',
        'images/slideshow/MiddleForkBridge.jpg',
        'images/slideshow/TwoMedicinePTZ.jpg',
        'images/slideshow/StMaryPTZ.jpg'
        ]
#####################VIDEOS##############################################
vurl = [
    'https://www.youtube.com/watch?v=Nu15hl3Eu7U', 
    'https://www.youtube.com/watch?v=81RScKzXZPw'
    ]
vlength = len(vurl)
v = 0
vname = ['Geiranger', 'Lodalen Loen']
#####################################################################
if hr >= 5 and hr <= 21:
    print("Requesting")
#####################################################################
    vlength = len(vurl)
    v = 0
    while v < vlength:
        streams = streamlink.streams(vurl[v])
        cap = cv2.VideoCapture(streams["best"].url)
        ret, frame = cap.read()
        rsframe = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA) #width=1600, height=900
        fname = (str(path) + str(vname[v]) + ".jpg")
        cv2.imwrite(fname, rsframe)    
        bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(fname, 'rb'), caption=vname[v])
        print(vname[v])
        cap.release()
        cv2.destroyAllWindows()
        time.sleep(1)
        v += 1
########################################################################
    while i < length:
        Data = requests.get(burl[i]).content
        with open(place[i], 'wb') as handler:
            handler.write(Data)
            print(name[i])
            bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(place[i], 'rb'), caption=name[i])
        time.sleep(1)
        i += 1
    print("Resizing Images ...")
    for root, subFolder, files in os.walk(path):
        for item in files:
            fileNamePath = os.path.join(root, item)
            img = cv2.imread(fileNamePath) #, cv2.IMREAD_UNCHANGED
            height = img.shape[0]
            width = img.shape[1]
            if (width != w) and (height != h):
                resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                cv2.imwrite(fileNamePath, resized)
                print("Resized ", fileNamePath)
            else:
                print("Skipped ", fileNamePath)
                continue
        
    print("Sleeping...")
    print(time.asctime())
    time.sleep(1)
    time.sleep(get_sleeptime(0, 0))
