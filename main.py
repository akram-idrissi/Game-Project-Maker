import os 
import sys
from subprocess import run
from dotenv import dotenv_values


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

    mkdir('lib')
    mkdir('include')

    run_command(f'COPY {SDL_LIB} lib')
    run_command(f'COPY {SDL_IMG_LIB} lib')
    run_command(f'COPY {SDL_INCLUDE} include')
    run_command(f'COPY {SDL_IMG_INCLUDE} include')
    run_command(f'COPY {SDL_DLL} .')
    run_command(f'COPY {SDL_IMG_DLL} .')
 

if __name__ == '__main__':
    main()