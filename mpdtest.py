from mpd import MPDClient
import time

client = MPDClient()               # create client object
client.timeout = 10                # network timeout in seconds (floats allowed), default: None
client.idletimeout = None          # timeout for fetching the result of the idle command is handled seperately, default: None
client.connect("localhost", 6600)  # connect to localhost:6600
print(client.mpd_version)          # print the MPD version
print(client.find("any", "spillebillen")) # print result of the command "find any house"
client.add("spotify:track:0VR0uoOiCMRtPVwh49dKrq")
print(client.playlist())
client.play()
time.sleep(3)
client.stop()
client.close()                     # send the close command
client.disconnect()
