import os 
import sys
from subprocess import run


TEMPLATE_PATH='C:\_coding\Templates\games'


def run_command(command):
    run(command, shell=True)


def get_args():
    args = sys.argv
    if(len(args) == 2): return args[1]


def mkdir(dir):
    if(not os.path.exists(dir)):
        os.mkdir(dir)


def main():
    path = get_args()

    mkdir(path)
    os.chdir(path)

    run_command(f'xcopy /E {TEMPLATE_PATH} {path}')
 

if __name__ == '__main__':
    main()