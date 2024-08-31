# This file is placed in the Public Domain.


"service"


import getpass
import os


from nixt.lib.config  import Config
from nixt.lib.persist import Persist, skel
from nixt.lib.main    import init, scan, wrap
from nixt.lib.utils   import forever, pidfile, privileges


cfg         = Config()
cfg.name    = Config.__module__.rsplit(".", maxsplit=3)[-3]
cfg.wdr     = os.path.expanduser(f"~/.{cfg.name}")
cfg.mod     = "cmd,err,mod,skl,srv,thr"
cfg.pidfile = os.path.join(cfg.wdr, f"{cfg.name}.pid")
cfg.user    = getpass.getuser()


Persist.workdir = cfg.wdr


from nixt import mod # pylint: disable=C0413


def wrapped():
    "wrap main"
    wrap(main)
    os._exit(0) # pylint: disable=W0212


initer = init


def main():
    "main"
    cfg.mod += ",irc,rss"
    privileges(cfg.user)
    skel()
    pidfile(cfg.pidfile)
    scan(cfg.mod, mod)
    initer(cfg.mod, mod)
    forever()


if __name__ == "__main__":
    wrapped()
