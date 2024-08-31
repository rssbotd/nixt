# This file is placed in the Public Domain.


"list of commands"


from nixt.lib.command import Commands
from nixt.lib.object  import keys


def cmd(event):
    "list commands."
    event.reply(",".join(sorted(keys(Commands.cmds))))
