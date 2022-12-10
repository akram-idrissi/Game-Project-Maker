import os 
import sys
from subprocess import run


SOURCE_PATH='C:\_coding\Templates\games'


def run_command(command):
    run(command, shell=True)


def get_args():
    args = sys.argv
    if(len(args) == 2): return args[1]


def mkdir(dir):
    if(not os.path.exists(dir)):
        os.mkdir(dir)


def main():
    destination = get_args()
    run_command(f'xcopy /E {SOURCE_PATH} {destination}')
 

if __name__ == '__main__':
    main()