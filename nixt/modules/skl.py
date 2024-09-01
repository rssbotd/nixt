# This file is placed in the Public Domain.
# pylint: disable=C,I,R


"skel"


from ..persist import skel


def skl(event):
    "create directories."
    skel()
    event.nop()


skl.target = "cli"
