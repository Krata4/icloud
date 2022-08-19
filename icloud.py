from pyicloud import PyiCloudService
import asyncio
import sys, getopt

username = "yourusername"

async def run():
    api = PyiCloudService(username)
    opts, args = getopt.getopt(sys.argv[1:],"dlsp:",["devices","localization=","status=","play_sound="])
    for opt, arg in opts:
        if opt in ("-d", "--devices"):
            print(api.devices)
        elif opt in ("-l", "--localization"):
            print(api.devices[arg].location())
        elif opt in ("-s", "--status"):
            print(api.devices[arg].status())
        elif opt in ("-p", "--play_sound"):
            print(api.devices[arg].play_sound())

asyncio.run(run())
