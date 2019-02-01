import subprocess
import os
from distutils.spawn import find_executable
home = os.path.expanduser("~")
cwd = os.getcwd()

def isdir(_path):
    return os.path.isdir(_path)

def join(*args):
    return os.path.join(*args)

download_path = join(home, 'Downloads')

subprocess.call('sudo wget https://repo.continuum.io/archive/Anaconda3-2018.12-Linux-x86_64.sh',
    cwd=download_path, shell=True)
subprocess.call('sudo bash Anaconda3-2018.12-Linux-x86_64.sh', cwd=download_path, shell=True)
