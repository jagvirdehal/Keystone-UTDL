#from gpiozero import
import json
import drop_box
from gpiozero import DistanceSensor as US
from gpiozero import LED, Servo
from time import sleep

import asyncio

# LEDs
scannerLed = LED(23)
powerLed = LED(20)
openLed = LED(16)

# Servo
latch = Servo(5)

# US Sensors
boxUS = US(trigger=27, echo=22)
lidUS = US(trigger=13, echo=6)
barUS = US(trigger=26, echo=19)

# drop_box.upload("data_upload.json")

def openLatch():
    latch.min()

def closeLatch():
    latch.max()

async def closeOnLid() {
    while (not lidUS.distance * 100 < 10):
        pass
    closeLatch()
}

async def dbxOpen():
    await drop_box.download("data_download.json")
    file = open("data_download.json")
    await data = json.load(file)

    if data.open:
        openLatch()
        await sleep(3)
        await closeOnLid()
        data.open = False
        with open('data_upload.json', 'w') as outfile:
            json.dump(data, outfile)
        drop_box.upload("data_upload.json")

async def scanner():
    while (barUS.distance * 100 < 10):
        scannerLed.on()
        await sleep(.1)
        scannerLed.off()
        await sleep(.1)

def isLatchOpen():
    if latch.value == -1:
        return True
    else
        return False

while True:
    asyncio.run(dbxOpen)
    asyncio.run(scanner)
    asyncio.run(closeOnLid)
    
    print("BoxUS: ", boxUS.distance * 100)
    print("LidUS: ", lidUS.distance * 100)
    print("BarUS: ", barUS.distance * 100)
    sleep(0.1)
