#!/usr/bin/python3

# Verkenner


from genie.testbed import load
from progress.bar import Bar

import os
import datetime


testbed = load('tb.yaml')

collection = {}


print(" ## Netwerk verkenner ##")
print()

print(" 🔍 Receiving a back-up of all devices")

with Bar(' Processing... ', max=len(testbed.devices)) as Bar:
    for step, device in enumerate(testbed):
        Bar.next()
        
        device.connect(log_stdout=False)
        configOutput = device.execute('show running-config')
        
        now = datetime.datetime.now()
        
        if not os.path.isdir(f'/opt/python/backup/{now.strftime("%-W")}/'):
            os.mkdir(f'/opt/python/backup/{now.strftime("%-W")}/')

        with open(f'/opt/python/backup/{now.strftime("%-W")}/backup_{now.strftime("%Y%m%d.%H%M")}_{device.name}.txt', 'w') as backupFile:
            backupFile.write(configOutput)
            
        device.disconnect()

print()
