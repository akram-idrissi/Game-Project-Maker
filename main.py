import os 
import sys
from subprocess import run

# SDL 
SDL_LIB=r'C:\Users\21264\Documents\libraries\SDL2-2.24.2\lib\x64'
SDL_INCLUDE=r'C:\Users\21264\Documents\libraries\SDL2-2.24.2\include'
SDL_DLL=r'C:\Users\21264\Documents\libraries\SDL2-2.24.2\lib\x64\SDL2.dll'

# SDL image
SDL_IMG_LIB=r'C:\Users\21264\Documents\libraries\SDL2_image-2.6.2\lib\x64'
SDL_IMG_INCLUDE=r'C:\Users\21264\Documents\libraries\SDL2_image-2.6.2\include'
SDL_IMG_DLL=r'C:\Users\21264\Documents\libraries\SDL2_image-2.6.2\lib\x64\SDL2_image.dll'


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