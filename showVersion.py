#!/usr/bin/python3

# Verkenner


from genie.testbed import load
from pprint import pprint
from progress.bar import Bar


testbed = load('tb.yaml')

collection = {}


print(" ## Netwerk verkenner ##")
print()

print(" 🔍 Collection show version of environment")

with Bar(' Processing... ', max=len(testbed.devices)) as Bar:
    for step, device in enumerate(testbed):
        Bar.next()
        
        device.connect(log_stdout=False)
        checkVersion = device.parse('show version')

        collection[device.name] = checkVersion

        device.disconnect()

print()

print(f"{'Hostname':20} {'Hardware':20} {'Platform':25} {'Versie':12}")

for host in collection:
    print(f"{host:20} {collection[host]['version']['chassis']:20} {collection[host]['version']['platform']:<25} {collection[host]['version']['version']:<12}")

print()
