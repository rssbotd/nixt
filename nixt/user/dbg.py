# This file is placed in the Public Domain.


"debug"


from ..command import Commands
from ..object  import fmt


def dbg(event):
    raise Exception(fmt(event))


Commands.add(dbg)
