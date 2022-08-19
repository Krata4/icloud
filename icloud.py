from pyicloud import PyiCloudService
import asyncio
import sys, getopt
import requests

username = "yourusername"
item_name = "yoouritemname"

async def icloud():
    api = PyiCloudService(username)
    opts, args = getopt.getopt(sys.argv[1:],"dul:s:p:",["devices","upload","localization=","status=","playsound="])
    upload = False
    loc = ""
    print(f'{{')
    for opt, arg in opts:
        if opt in ("-d", "--devices"):
            print("devices:")
            print(api.devices)
            print(",")
        elif opt in ("-l", "--localization"):
            print("localization:")
            loc = api.devices[arg].location()
            print(loc)
            print(",")
        elif opt in ("-s", "--status"):
            print("status:")
            print(api.devices[arg].status())
            print(",")
        elif opt in ("-p", "--playsound"):
            print(api.devices[arg].play_sound())
        elif opt in ("-u", "--upload"):
            upload = True
    print(f"}}")
    if upload:
        loc_gps = str(loc['latitude']) + "," + str(loc['longitude'])
        requests.put('http://openhab:8080/rest/items/'+item_name+'/state', str(loc_gps), headers={'Content-type': 'text/plain'})
asyncio.run(icloud())
