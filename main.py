import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

import api

user = 0
game = 5685

json = api.get(user,game)
print(json)
json = api.get(user+1,game)
print(json)