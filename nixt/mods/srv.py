# This file is placed in the Public Domain.


"create service file"


from ..main import Commands


def srv(event):
    "create service file (pipx)."
    if event.args:
        name = event.args[0]
    else:
        name  = getpass.getuser()
    TXT = """[Unit]
Description=%s
After=network-online.target

[Service]
Type=simple
User=%s
Group=%s
ExecStart=/home/%s/.local/bin/objbots

[Install]
WantedBy=multi-user.target"""
    event.reply(TXT % (Cfg.name.upper(), name, name, name))


Commands.add(srv)
