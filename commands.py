import os, os.path, glob

MODULE = 'lombok'
VERSION = '1.2.5'

# Commands that are specific to your module

COMMANDS = []

def execute(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")

# This will be executed before any command (new, run...)
def before(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")

    if command in ["run", "start", "precompile"]:
        lombokJar = glob.glob(app.path + '/modules/lombok*/lib/lombok*.jar')[0]
        args.append('-javaagent:' + lombokJar + '=ECJ')

# This will be executed after any command (new, run...)
def after(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")

    if command == "new":
        pass
