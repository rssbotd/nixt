# This file is placed in the Public Domain.


"list of commands"


from ..lib.command import Commands
from ..lib.object  import keys


def cmd(event):
    "list commands."
    event.reply(",".join(sorted(keys(Commands.cmds))))
