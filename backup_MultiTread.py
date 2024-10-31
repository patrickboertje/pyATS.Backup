#!/usr/bin/python3

# Verkenner


from genie.testbed import load
from progress.bar import Bar

import multiprocessing
import os
import datetime


testbed = load('tb.yaml')


def collectInformation(deviceName):
    device = testbed.devices[deviceName]

    device.connect(log_stdout=False)
    configOutput = device.execute('show running-config')
    
    now = datetime.datetime.now()
    
    if not os.path.isdir(f'/opt/python/backup/{now.strftime("%-W")}/'):
        os.mkdir(f'/opt/python/backup/{now.strftime("%-W")}/')

    with open(f'/opt/python/backup/{now.strftime("%-W")}/backup_{now.strftime("%Y%m%d.%H%M")}_{device.name}.txt', 'w') as backupFile:
        backupFile.write(configOutput)
        
    device.disconnect()


def main():
    deviceNames = [device.name for device in testbed.devices.values()]

    with multiprocessing.Pool(processes=len(deviceNames)) as pool:
        pool.map(collectInformation, deviceNames)


if __name__ == '__main__':
    print()
    print(" 🔍 Receiving a back-up of all devices")
    
    main()
    
    print(" 🏁 All backups finished")
    print()
