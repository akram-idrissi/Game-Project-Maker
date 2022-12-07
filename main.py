import os 
import sys
from subprocess import run


def run_command(command):
    run(command, shell=True)


def get_args():
    args = sys.argv
    if(len(args) == 2): return args[1]


def mkdir(dir):
    if(not os.path.exists()):
        os.mkdir(dir)


def main():
    pass


if __name__ == '__main__':
    main()

