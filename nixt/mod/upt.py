# This file is placed in the Public Domain.


"uptime"


import time


from nixt.lib.runtime import STARTTIME
from nixt.lib.utils   import laps


def upt(event):
    "show uptime."
    event.reply(laps(time.time() - STARTTIME))
