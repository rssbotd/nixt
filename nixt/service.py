# This file is placed in the Public Domain.


"service"


import os


from .persist import skel
from .main    import init, scan, wrap
from .runtime import Cfg
from .utils   import forever, pidfile, privileges


from . import modules


def wrapped():
    "wrap main"
    wrap(main)
    os._exit(0) # pylint: disable=W0212


initer = init

def main():
    "main"
    Cfg.mod += ",irc,rss"
    privileges(Cfg.user)
    skel()
    pidfile(Cfg.pidfile)
    scan(Cfg.mod, modules)
    initer(Cfg.mod, modules)
    forever()


if __name__ == "__main__":
    wrapped()
