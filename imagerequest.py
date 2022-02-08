import urllib.request
import time
from datetime import datetime
import requests


apgarURL = 'https://www.nps.gov/webcams-glac/ApgarVillage.jpg'
missoulaURL = 'https://wingsvirtualtours.com/webcams/missoula_valley/public_html/cam/streaming/mp/current.jpg'
aspenURL = 'https://coloradowebcam.net/webcam/aspenmtn/current.jpg'
boulderURL = 'https://coloradowebcam.net/webcam/boulder/current.jpg'
soprisURL = 'https://coloradowebcam.net/webcam/sopris/current.jpg'
#**************************************************************************
apgar = r'\Users\trcyp\Downloads\PiClock-Python3-SerBrynden\PiClock-Python3-SerBrynden\Clock\images\slideshow\apgar.jpg'
missoula = r'\Users\trcyp\Downloads\PiClock-Python3-SerBrynden\PiClock-Python3-SerBrynden\Clock\images\slideshow\missoula.jpg'
aspen = r'\Users\trcyp\Downloads\PiClock-Python3-SerBrynden\PiClock-Python3-SerBrynden\Clock\images\slideshow\aspen.jpg'
boulder = r'\Users\trcyp\Downloads\PiClock-Python3-SerBrynden\PiClock-Python3-SerBrynden\Clock\images\slideshow\boulder.jpg'
sopris = r'\Users\trcyp\Downloads\PiClock-Python3-SerBrynden\PiClock-Python3-SerBrynden\Clock\images\slideshow\sopris.jpg'
#***************************************************************************
print(time.asctime())

while True:
    r = time.localtime()
    h = r.tm_hour
    m = r.tm_min
    s = r.tm_sec
    if h >= 7 and h <= 19:
        #time.sleep(1800)
        print("Requesting")
        apgarData = requests.get(apgarURL).content
        with open(apgar, 'wb') as handler:
            handler.write(apgarData)
        missoulaData = requests.get(missoulaURL).content
        with open(missoula, 'wb') as handler:
            handler.write(missoulaData)
        aspenData = requests.get(aspenURL).content
        with open(aspen, 'wb') as handler:
            handler.write(aspenData)
        boulderData = requests.get(boulderURL).content
        with open(boulder, 'wb') as handler:
            handler.write(boulderData)
        soprisData = requests.get(soprisURL).content
        with open(sopris, 'wb') as handler:
            handler.write(soprisData)
            
        print("Done")
