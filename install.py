import subprocess
import os

# Install vundle for vim
subprocess.call('git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim'.split())

# if vim is not installed, install it 
subprocess.call(['sudo', 'apt-get', 'update'])
subprocess.call(['sudo', 'apt-get', 'install', 'vim'])

# Install monokai colorscheme
subprocess.call('git clone https://github.com/sickill/vim-monokai.git'.split())
if not os.path.isdir('~/.vim/colors'):
    os.mkdir('~/.vim/colors')
subprocess.call('mv ./vim-monokai/colors/monokai.vim ~/.vim/colors/'.split())
subprocess.call('rm -rf ./vim-monokai') # Remove monokai directory

# copy .vimrc file to home directory
subprocess.call(['cp ./.vimrc ~/'.split()])

# Run PluginInstall in command line
subprocess.call('vim +PluginInstall +qall'.split())

# Install YouCompleteMe plugin
subprocess.call('cd ~/.vim/bundle/YouCompleteMe/'.split())
subprocess.call('git submodule update --init --recursive'.split())
subprocess.call('sudo apt install build-essential cmake python3-dev'.split())
subprocess.call('python3 install.py'.split())
