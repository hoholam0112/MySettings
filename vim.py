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

if not find_executable('cmake'):
    subprocess.call(['sudo', 'apt', 'install', 'cmake'])

# Install vundle for vim
if not isdir(join(home, '.vim')):
    subprocess.call(['sudo', 'mkdir', join(home, '.vim')])
if not isdir(join(home, '.vim', 'bundle')):
    subprocess.call(['sudo', 'mkdir', join(home, '.vim/bundle')])

subprocess.call('sudo git clone https://github.com/VundleVim/Vundle.vim.git'.split(),
    cwd=join(home, '.vim/bundle'))


# Install monokai colorscheme
subprocess.call('sudo git clone https://github.com/sickill/vim-monokai.git'.split())
if not isdir(join(home, '.vim/colors')):
    subprocess.call(['sudo', 'mkdir', join(home, '.vim/colors')])

_from = join(cwd, 'vim-monokai/colors/monokai.vim')
_to = join(home, '.vim/colors/')
subprocess.call(['sudo', 'mv', _from, _to])
subprocess.call(['sudo', 'rm', '-rf', join(cwd, 'vim-monokai')]) # Remove monokai directory

# Install YouCompleteMe plugin
subprocess.call('sudo git clone https://github.com/Valloric/YouCompleteMe.git'.split(),
    cwd=join(home, '.vim/bundle'))
subprocess.call('sudo git submodule update --init --recursive'.split(),
    cwd=join(home, '.vim/bundle/YouCompleteMe'))
subprocess.call('sudo apt install build-essential cmake python3-dev'.split())
subprocess.call('sudo python3 install.py'.split(), cwd=join(home, '.vim/bundle/YouCompleteMe'))

# copy .vimrc file to home directory
_from = join(cwd, '.vimrc')
_to = home
subprocess.call(['sudo', 'cp', _from, _to])

# Run PluginInstall in command line
subprocess.call('sudo vim +PluginInstall +qall'.split())
