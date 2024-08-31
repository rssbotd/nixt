# This file is placed in the Public Domain.


"skel"


from ..persist import skel


def skl(event):
    "create directories."
    skel()


skl.target = "cli"
