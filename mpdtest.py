from mpd import MPDClient
import time

client = MPDClient()               # create client object
client.timeout = 10                # network timeout in seconds (floats allowed), default: None
client.idletimeout = None          # timeout for fetching the result of the idle command is handled seperately, default: None
client.connect("192.168.1.242", 6600)  # connect to localhost:6600
print(client.mpd_version)          # print the MPD version
print(client.find("any", "spillebillen")) # print result of the command "find any house"
client.clear()
client.setvol(50)
client.add("spotify:track:4QWRvlXU8dRUobH9YCDrIY")
print(client.playlist())
client.play()
time.sleep(15)
client.stop()
client.close()                     # send the close command
client.disconnect()
