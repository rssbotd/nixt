# This file is placed in the Public Domain.


"daemon"


import os
import sys


from .persist import skel
from .main    import init, scan, wrap
from .runtime import Cfg
from .utils   import forever, pidfile, privileges


from . import modules


def daemon(verbose=False):
    "switch to background."
    pid = os.fork()
    if pid != 0:
        os._exit(0) # pylint: disable=W0212
    os.setsid()
    pid2 = os.fork()
    if pid2 != 0:
        os._exit(0) # pylint: disable=W0212
    if not verbose:
        with open('/dev/null', 'r', encoding="utf-8") as sis:
            os.dup2(sis.fileno(), sys.stdin.fileno())
        with open('/dev/null', 'a+', encoding="utf-8") as sos:
            os.dup2(sos.fileno(), sys.stdout.fileno())
        with open('/dev/null', 'a+', encoding="utf-8") as ses:
            os.dup2(ses.fileno(), sys.stderr.fileno())
    os.umask(0)
    os.chdir("/")
    os.nice(10)


def wrapped():
    "wrap main"
    wrap(main)
    os._exit(0) # pylint: disable=W0212


def main():
    "main"
    Cfg.mod += ",irc,rss"
    daemon()
    privileges(Cfg.user)
    skel()
    pidfile(Cfg.pidfile)
    scan(Cfg.mod, modules)
    init(Cfg.mod, modules)
    forever()


if __name__ == "__main__":
    wrapped()
