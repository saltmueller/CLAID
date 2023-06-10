import argparse
from git import Repo
from install import install_package
from create import create
from build import build 
from run import run
 
args = ""


def init():
    print("claid manager init")
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    parser.add_argument("vars", nargs="*")

    args = parser.parse_args()

    map = [("list_packages", list_packages),
           ("install", install_package),
           ("create", create),
           ("build", build),
           ("run", run)
           ]

    for entry in map:
        name, func = entry

        if(name == args.command):
            func(*args.vars)
            return
        
    print("Error, command \"claid {}\" is unknown.".format(args.command))


def list_packages(arg1, *args):
    print("listing packages")

