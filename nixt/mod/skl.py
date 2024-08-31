# This file is placed in the Public Domain.


"skel"


from nixt.lib.persist import skel


def skl(event):
    "create directories."
    skel()


skl.target = "cli"
