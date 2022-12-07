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
    path = get_args()

    if(os.path.exists()):
        os.chdir(path)
        mkdir('lib')
        mkdir('include')
        run_command(f'COPY {SDL_LIB}, {SDL_IMG_LIB} lib')
        run_command(f'COPY {SDL_INCLUDE}, {SDL_IMG_INCLUDE} include')
        run_command(f'COPY {SDL_DLL}, {SDL_IMG_DLL} .')
 

if __name__ == '__main__':
    main()

