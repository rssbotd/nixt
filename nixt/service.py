# This file is placed in the Public Domain.
# pylint: disable=C0413,W0212


"daemon"


import getpass
import os
import sys


sys.path.insert(0, os.getcwd())


from .thread import errors
from .main   import Config, forever, initer, pidfile, privileges, wrap
from .mods   import face


Cfg = Config("nixt")
Cfg.user = getpass.getuser()
Cfg.mod = "cmd,err,mod,irc,rss,thr"


def main():
    "main"
    privileges(Cfg.user)
    pidfile(Cfg.pidfile)
    initer(Cfg.mod, face)
    forever()


def wrapper():
    wrap(main)
    errors(print)
    

if __name__ == "__main__":
    wrapper()
