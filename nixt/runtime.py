# This file is placed in the Public Domain.


"runtime"


import getpass
import os
import time


from .default import Default
from .persist import Persist


STARTTIME = time.time()


class Config(Default): # pylint: disable=R0903

    "configuration"

    def __init__(self):
        Default.__init__(self)
        self.name    = Config.__module__.rsplit(".", maxsplit=2)[-2]
        self.user    = getpass.getuser()
        self.mod     = "cmd,err,mod,skl,srv,thr"
        self.wdr     = os.path.expanduser(f"~/.{self.name}")
        self.pidfile = os.path.join(self.wdr, f"{self.name}.pid")


Cfg = Config()


Persist.workdir = Cfg.wdr
