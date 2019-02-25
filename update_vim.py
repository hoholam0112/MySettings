import subprocess

subprocess.call('sudo apt-get purge vim-*', shell=True)
subprocess.call('sudo add-apt-repository ppa:jonathonf/vim', shell=True)
subprocess.call('sudo apt update', shell=True)
subprocess.call('sudo apt install vim', shell=True)
