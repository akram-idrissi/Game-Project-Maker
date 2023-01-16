import os 
import sys
import shutil


SOURCE_PATH='C:\_coding\Templates\games'

def get_args():
    args = sys.argv
    if(len(args) == 2): return args[1]


def main():
    destination = get_args()
    shutil.copytree(SOURCE_PATH, destination)
 

if __name__ == '__main__':
    main()