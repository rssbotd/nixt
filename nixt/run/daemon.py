# This file is placed in the Public Domain.


"daemon"


import getpass
import os
import sys


from nixt.lib.config  import Config
from nixt.lib.persist import Persist,skel
from nixt.lib.main    import init, scan, wrap
from nixt.lib.utils   import forever, pidfile, privileges


from nixt import mod


cfg         = Config()
cfg.mod     = "cmd,err,mod,skl,srv,thr"
cfg.name    = Config.__module__.rsplit(".", maxsplit=3)[-3]
cfg.wdr     = os.path.expanduser(f"~/.{cfg.name}")
cfg.pidfile = os.path.join(cfg.wdr, f"{cfg.name}.pid")


Persist.workdir = cfg.wdr


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
    cfg.mod += ",irc,rss"
    cfg.user = getpass.getuser()
    daemon()
    privileges(cfg.user)
    skel()
    pidfile(cfg.pidfile)
    scan(cfg.mod, mod)
    init(cfg.mod, mod)
    forever()


if __name__ == "__main__":
    wrapped()
