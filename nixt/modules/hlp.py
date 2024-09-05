# This file is placed in the Public Domain.


"help"


from ..        import __doc__ as docstr
from ..        import __author__ as author
from ..command import Commands
from ..config  import Config


def hlp(event):
    "show help."
    nme = Config.name
    args = event.args
    title = docstr.split("\n", maxsplit=1)[0]
    descr = "\n".join(docstr.split("\n")[1:])
    if args:
        nme = args[0]
        if len(args) > 1:
            title = " ".join(args[1:])
    descr = descr.strip()
    txt = f"""NAME

    {nme.upper()} - {title}

SYNOPSIS

    {nme} <cmd> [key=val] [key==val]
    {nme}c
    {nme}d
    {nme}s

DESCRIPTION

    {descr}

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

    $ {nme}d
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

    {author}

COPYRIGHT

    {nme.upper()} is Public Domain.
"""
    event.reply(txt)


hlp.target = "cli"


Commands.add(hlp)
