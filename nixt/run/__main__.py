# This file is placed in the Public Domain.


"cli"


import os
import sys


from nixt.lib.config  import Config
from nixt.lib.persist import Persist, skel
from nixt.lib.errors  import errors
from nixt.lib.main    import cmnd, enable, scan, wrap
from nixt.lib.parse   import parse
from nixt.lib.utils   import modnames


from nixt import mod


cfg         = Config()
cfg.name    = Config.__module__.rsplit(".", maxsplit=3)[-3]
cfg.mod     = "cmd,err,mod,skl,srv,thr"
cfg.wdr     = os.path.expanduser(f"~/.{cfg.name}")
cfg.pidfile = os.path.join(cfg.wdr, f"{cfg.name}.pid")


Persist.workdir = cfg.wdr


def srv(event):
    "create service file (pipx)."
    import getpass
    if event.args:
        username = event.args[0]
    else:
        username  = getpass.getuser()
    path = os.path.normpath(f"/home/{username}/.local/bin/")
    txt = f"""[Unit]
Description={cfg.name.upper()}
Requires=network-online.target
After=network-online.target

[Service]
Type=simple
User={username}
Group={username}
ExecStartPre={path}/{cfg.name} skl
ExecStart={path}/{cfg.name}s
ExitType=cgroup
KillSignal=SIGKILL
KillMode=control-group
Restart=no

[Install]
WantedBy=default.target"""
    event.reply(txt)


srv.target = "cli"


def wrapped():
    "wrap main."
    wrap(main)
    errors()


def main():
    "main"
    parse(cfg, " ".join(sys.argv[1:]))
    skel()
    enable(print)
    cfg.dis = cfg.sets.dis
    cfg.mod = ",".join(modnames(mod))
    scan(cfg.mod, mod)
    cmnd(cfg.otxt, print)


if __name__ == "__main__":
    wrapped()
