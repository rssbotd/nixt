# This file is placed in the Public Domain.


"service"


import getpass
import os


from ..command import Commands
from ..config import Config as Cfg


def srv(event):
    "create service file (pipx)."
    username  = getpass.getuser()
    path = os.path.normpath(f"/home/{username}/.local/bin/")
    txt = f"""[Unit]
Description={Cfg.name.upper()}
After=network-online.target

[Service]
Type=simple
User={username}
Group={username}
ExecStart={path}/{Cfg.name}s

[Install]
WantedBy=multi-user.target"""
    event.reply(txt)


srv.target = "cli"


Commands.add(srv)
