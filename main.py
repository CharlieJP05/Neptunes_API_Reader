import sys
import random
import time
import json

import api
from window import WindowManager
wm = WindowManager()

wm.load()
user = 0
game = 5685

json = api.get(user,game)
json = api.get(user+1,game)
print(type(json["stars"]))
wm.update_map(json["stars"])


wm.app_exec()
time.sleep(5)