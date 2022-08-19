from pyicloud import PyiCloudService
import asyncio
import sys, getopt

username = "yourusername"

async def icloud():
    api = PyiCloudService(username)
    opts, args = getopt.getopt(sys.argv[1:],"dl:s:p:",["devices","localization=","status=","playsound="])
    print(f'{{')
    for opt, arg in opts:
        if opt in ("-d", "--devices"):
            print("devices:")
            print(api.devices)
        elif opt in ("-l", "--localization"):
            print("localization:")
            print(api.devices[arg].location())
        elif opt in ("-s", "--status"):
            print("status:")
            print(api.devices[arg].status())
        elif opt in ("-p", "--playsound"):
            print(api.devices[arg].play_sound())
    print(f"}}")

asyncio.run(icloud())
