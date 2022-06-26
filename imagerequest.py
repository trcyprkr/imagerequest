import telegram
import cv2
import streamlink
import os
import urllib.request
import time
from datetime import datetime
import requests
from screeninfo import get_monitors
for m in get_monitors():
    #print(str(m))
    monitor = m
    w = monitor.width
    h = monitor.height

TELEGRAM_BOT_TOKEN = '5312232939:AAGxxxxxxxxxxxxxxxxxxxxxxxxxxx'
TELEGRAM_CHAT_ID = '-100xxxxxxxxxxxxxx'
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    
path = r'images/slideshow'
dim = (w, h)

apgarURL = 'https://www.nps.gov/webcams-glac/ApgarVillage.jpg'
missoulaURL = 'https://wingsvirtualtours.com/webcams/missoula_valley/public_html/cam/streaming/mp/current.jpg'
aspenURL = 'https://coloradowebcam.net/webcam/aspenmtn/current.jpg'
boulderURL = 'https://coloradowebcam.net/webcam/boulder/current.jpg'
soprisURL = 'https://coloradowebcam.net/webcam/sopris/current.jpg'
glacierbasinURL = 'https://www.nps.gov/webcams-romo/glacier_basin.jpeg'
woodparkURL = 'https://coloradowebcam.net/webcam/pikespeak/current.jpg'
pagosaURL = 'https://live5.brownrice.com/cam-images/wolfcreeksummit.jpg'
ourayURL = 'https://coloradowebcam.net/webcam/ouraynet-town/current.jpg'
longpeakURL = 'https://www.nps.gov/webcams-romo/longs_peak.jpg'
#**************************************************************************
apgar = r'images/slideshow/apgar.jpg'
missoula = r'images/slideshow/missoula.jpg'
aspen = r'images/slideshow/aspen.jpg'
boulder = r'images/slideshow/boulder.jpg'
sopris = r'images/slideshow/sopris.jpg'
glacierbasin = r'images/slideshow/glacierbasin.jpg'
woodpark = r'images/slideshow/woodpark.jpg'
pagosa = r'images/slideshow/pagosa.jpg'
ouray = r'images/slideshow/ouray.jpg'
longpeak = r'images/slideshow/longpeak.jpg'
#***************************************************************************
#print(time.localtime())
while True:
    r = time.localtime()
    h = r.tm_hour
    m = r.tm_min
    s = r.tm_sec
    if h >= 7 and h <= 21:
        print("Requesting")
#####################################################################
        url = 'https://youtu.be/1EiC9bvVGnk'  ##This can be changed to whatever live stream you want
        streams = streamlink.streams(url)
        cap = cv2.VideoCapture(streams["best"].url)
        ret, frame = cap.read()
        rsframe = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA) #width=1600, height=900
        cv2.imwrite(r"images\slideshow\jacksonhole.jpg", rsframe)
        jacksonhole = r'images\slideshow\jacksonhole.jpg'
        print("jackson hole")
        bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(jacksonhole, 'rb'), caption='jacksonhole')
        cap.release()
        cv2.destroyAllWindows()
#########################################################################
        apgarData = requests.get(apgarURL).content
        with open(apgar, 'wb') as handler:
            handler.write(apgarData)
            print("apgar")
        bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(apgar, 'rb'), caption='apgar')
#####################################################################            
        missoulaData = requests.get(missoulaURL).content
        with open(missoula, 'wb') as handler:
            handler.write(missoulaData)
            print("missoula")
        bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(missoula, 'rb'), caption='missoula')
#####################################################################            
        aspenData = requests.get(aspenURL).content
        with open(aspen, 'wb') as handler:
            handler.write(aspenData)
            print("aspen")
        bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(aspen, 'rb'), caption='aspen')
#####################################################################            
        boulderData = requests.get(boulderURL).content
        with open(boulder, 'wb') as handler:
            handler.write(boulderData)
            print("boulder")
        bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(boulder, 'rb'), caption='boulder')
#####################################################################            
        soprisData = requests.get(soprisURL).content
        with open(sopris, 'wb') as handler:
            handler.write(soprisData)
            print("sopris")
        bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(sopris, 'rb'), caption='sopris')
#####################################################################
        glacierbasinData = requests.get(glacierbasinURL).content
        with open(glacierbasin, 'wb') as handler:
            handler.write(glacierbasinData)
            print("glacier basin")
        bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(glacierbasin, 'rb'), caption='glacierbasin')
####################################################################
        woodparkData = requests.get(woodparkURL).content
        with open(woodpark, 'wb') as handler:
            handler.write(woodparkData)
            print("woodpark")
        bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(woodpark, 'rb'), caption='woodpark')
#####################################################################
        pagosaData = requests.get(pagosaURL).content
        with open(pagosa, 'wb') as handler:
            handler.write(pagosaData)
            print("pagosa")
        bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(pagosa, 'rb'), caption='pagosa')
###############################################################################
        ourayData = requests.get(ourayURL).content
        with open(ouray, 'wb') as handler:
            handler.write(ourayData)
            print("ouray")
        bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(ouray, 'rb'), caption='ouray')
################################################################################
        longpeakData = requests.get(longpeakURL).content
        with open(longpeak, 'wb') as handler:
            handler.write(longpeakData)
            print("longpeak")
        bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(longpeak, 'rb'), caption='longpeak')
################################################################################
        print("Resizing Images ...")
        for root, subFolder, files in os.walk(path):
            for item in files:
                fileNamePath = os.path.join(root, item)
                img = cv2.imread(fileNamePath) #, cv2.IMREAD_UNCHANGED
                #size = img.shape
                height = img.shape[0]
                width = img.shape[1]
                if (width != w) and (height != h):
                    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                    cv2.imwrite(fileNamePath, resized)
                    print("Resized ", fileNamePath)
                else:
                    skipped = fileNamePath
                    print("Skipped ", fileNamePath)
                    continue
                    bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(skipped, 'rb'), caption='skipped')
                    
################################################################
        print("Done")
        print(time.asctime())
        for i in range(3600,0,-1):
            time.sleep(1)
            print("Sleeping for", i, "seconds", '\r', end='')
