import urllib.request
import time
import datetime as dt

def get_sleeptime(minute, second):
    now = dt.datetime.now()
    sched = now.replace(minute=minute, second=second)
    sleeptime = (sched - now).total_seconds()
    if sleeptime < 0:
        sleeptime += 3600
    return sleeptime

apgar = r'\Users\trcyp\Downloads\PiClock-Python3-SerBrynden\PiClock-Python3-SerBrynden\Clock\images\slideshow\apgarvillage.jpg'
apgarURL = 'https://www.nps.gov/webcams-glac/ApgarVillage.jpg'

missoula = r'\Users\trcyp\Downloads\PiClock-Python3-SerBrynden\PiClock-Python3-SerBrynden\Clock\images\slideshow\missoula.jpg'
missoulaURL = 'https://wingsvirtualtours.com/webcams/missoula_valley/public_html/cam/streaming/mp/current.jpg'

while True:
    print("Waiting...")
    time.sleep(get_sleeptime(0, 0))
    print("Requesting")
    urllib.request.urlretrieve(apgarURL, apgar)
    time.sleep(10)
    urllib.request.urlretrieve(missoulaURL, missoula)
    time.sleep(5)
    print("Done")
