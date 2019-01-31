import subprocess
import os
from distutils.spawn import find_executable
home = os.path.expanduser("~")
cwd = os.getcwd()

def isdir(_path):
    return os.path.isdir(_path)

def join(*args):
    return os.path.join(*args)

# if vim is not installed, install it 
if not find_executable('vim'):
    subprocess.call(['sudo', 'apt-get', 'update'])
    subprocess.call(['sudo', 'apt-get', 'install', 'vim'])

# Install vundle for vim
if not isdir(join(home, '.vim')):
    os.mkdir(join(home, '.vim'))
if not isdir(join(home, '.vim', 'bundle')):
    os.mkdir(join(home, '.vim', 'bundle'))

subprocess.call('git clone https://github.com/VundleVim/Vundle.vim.git'.split(),
    cwd=join(home, '.vim/bundle'))


# Install monokai colorscheme
subprocess.call('git clone https://github.com/sickill/vim-monokai.git'.split())
if not isdir(join(home, '.vim/colors')):
    os.mkdir(join(home, '.vim/colors'))
_from = join(cwd, 'vim-monokai/colors/monokai.vim')
_to = join(home, '.vim/colors/')
subprocess.call(['mv', _from, _to])
subprocess.call(['rm', '-rf', join(cwd, 'vim-monokai')]) # Remove monokai directory

# Install YouCompleteMe plugin
subprocess.call('git clone https://github.com/Valloric/YouCompleteMe.git'.split(),
    cwd=join(home, '.vim/bundle'))
subprocess.call('git submodule update --init --recursive'.split(),
    cwd=join(home, '.vim/bundle/YouCompleteMe'))
subprocess.call('sudo apt install build-essential cmake python3-dev'.split())
subprocess.call('python3 install.py'.split(), cwd=join(home, '.vim/bundle/YouCompleteMe'))

# copy .vimrc file to home directory
_from = join(cwd, '.vimrc')
_to = home
subprocess.call(['cp', _from, _to])

# Run PluginInstall in command line
subprocess.call('vim +PluginInstall +qall'.split())
