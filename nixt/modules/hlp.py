# This file is placed in the Public Domain.


"help"


from ..command import Commands
from ..config import Config


nme = Config.name


DESCR = "NIXT does nothing, write your own commands!"
TXT = f"""SYNOPSIS

    {nme} <cmd> [key=val] [key==val]
    {nme}c
    {nme}d
    {nme}s

DESCRIPTION

    {DESCR}

INSTALL

    $ pipx install {nme}
    $ pipx ensurepath

USAGE

    without any argument nixt does nothing

    $ {nme}
    $

    see list of commands

    $ {nme} cmd
    cmd,err,hlp,mod,srv,thr,upt

    start a console

    $ {nme}c
    >

    use -i to run init on modules

    $ {nme}c -i
    >

    start daemon

    $ {nme}td
    $

    start as service

    $ {nme}s
    <waits till ctrl-c>

COMMANDS

    cmd - commands
    err - show errors
    hlp - show help
    mod - available modules
    srv - create service file
    thr - show running threads
    upt - show uptime

SYSTEMD

    $ {nme} srv > {nme}.service
    $ sudo mv {nme}.service /etc/systemd/system/
    $ sudo systemctl enable {nme} --now

FILES

    ~/.{nme}
    ~/.local/bin/{nme}
    ~/.local/bin/{nme}c
    ~/.local/bin/{nme}d
    ~/.local/bin/{nme}s
    ~/.local/pipx/venvs/{nme}/

AUTHOR

    Bart Thate <rssbotd@gmail.com>

COPYRIGHT

    {nme.upper()} is Public Domain."""


def hlp(event):
    "show help."
    event.reply(TXT)


hlp.target = "cli"


Commands.add(hlp)
