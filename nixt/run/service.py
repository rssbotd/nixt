# This file is placed in the Public Domain.


"service"


import os


from nixt.lib.persist import skel
from nixt.lib.main    import init, scan, wrap
from nixt.lib.runtime import cfg


from . import modules


cfg         = Config()
cfg.name    = Config.__module__.rsplit(".", maxsplit=3)[-3]
cfg.wdr     = os.path.expanduser(f"~/.{cfg.name}")
cfg.mod     = "cmd,err,mod,skl,srv,thr"
cfg.pidfile = os.path.join(cfg.wdr, f"{cfg.name}.pid")


Persist.workdir = cfg.wdr



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
    scan(cfg.mod, modules)
    initer(cfg.mod, modules)
    forever()


if __name__ == "__main__":
    wrapped()
