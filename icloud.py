from pyicloud import PyiCloudService
import asyncio
import sys, getopt

username = "yourusername"

async def icloud():
    api = PyiCloudService(username)
    opts, args = getopt.getopt(sys.argv[1:],"dls:p:",["devices","localization=","status=","playsound="])
    for opt, arg in opts:
        if opt in ("-d", "--devices"):
            print(api.devices)
        elif opt in ("-l", "--localization"):
            print(api.devices[arg].location())
        elif opt in ("-s", "--status"):
            print(api.devices[arg].status())
            #print(arg)
        elif opt in ("-p", "--playsound"):
            print(api.devices[arg].play_sound())

asyncio.run(icloud())
