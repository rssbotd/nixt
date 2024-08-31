# This file is placed in the Public Domain.


"prompt"


import os
import readline
import sys
import termios


from nixt.lib.config  import Config
from nixt.lib.console import Console
from nixt.lib.errors  import errors
from nixt.lib.persist import Persist,skel
from nixt.lib.main    import cmnd, enable, init, scan
from nixt.lib.parse   import parse
from nixt.lib.utils   import forever, modnames, spl


cfg         = Config()
cfg.name    = Config.__module__.rsplit(".", maxsplit=3)[-3]
cfg.wdr     = os.path.expanduser(f"~/.{cfg.name}")
cfg.pidfile = os.path.join(cfg.wdr, f"{cfg.name}.pid")
cfg.mod     = "cmd,err,mod,skl,srv,thr"


Persist.workdir = cfg.wdr


from nixt import mod # pylint: disable=C0413


if os.path.exists("mods"):
    import mods as MODS # pylint: disable=E0401
else:
    MODS = None


def wrap(func):
    "reset console."
    old3 = None
    try:
        old3 = termios.tcgetattr(sys.stdin.fileno())
    except termios.error:
        pass
    try:
        func()
    except (KeyboardInterrupt, EOFError):
        print("")
    finally:
        if old3:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old3)


def main():
    "main"
    parse(cfg, " ".join(sys.argv[1:]))
    readline.redisplay()
    enable(print)
    skel()
    cfg.dis = cfg.sets.dis
    mods = modnames(mod, MODS)
    cfg.mod = ",".join(mods)
    if cfg.dis:
        cfg.mod = ",".join(set(mods) - set(spl(cfg.dis)))
    scan(cfg.mod, mod, MODS)
    csl = Console(print, input)
    if "i" in cfg.opts:
        init(cfg.mod, mod, MODS)
    csl.start()
    cmnd(cfg.otxt, print)
    forever()


def wrapped():
    "wrap main function."
    wrap(main)
    errors()


if __name__ == "__main__":
    wrapped()
