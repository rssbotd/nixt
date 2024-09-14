# This file is placed in the Public Domain.
# pylint: disable=C0413,W0611


"prompt"


import getpass
import os
import readline
import sys
import termios


sys.path.insert(0, os.getcwd())


from .thread import errors
from .object import Default, construct, fmt
from .main   import Broker, Client, Commands, Config, Event
from .main   import command, forever, modnames, parse, wrap
from .mods   import face


Cfg = Config("objbot")
Cfg.mod = ",".join(modnames(face))


class CLI(Client):

    def raw(self, txt):
        print(txt)


def wrapped():
    wrap(main)
    errors(print)


def main():
    "main"
    parse(Cfg, " ".join(sys.argv[1:]))
    if Cfg.txt:
        evt = Event()
        parse(evt, Cfg.otxt)
        clt = CLI()
        command(clt, evt)


if __name__ == "__main__":
    wrapped()
