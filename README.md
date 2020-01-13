# My Settings
This codes have been tested on Ubuntu 16.04 and 18.04. Don't try to run this code in other machines.
## Vim
First, download this git repo to your local machine.
```
git clone https://github.com/hoholam0112/MySettings /where/you/want
```
Second, move to the repository and type this on your command line.
```
python vim.py
```

### Issues on YouCompleteMe: A popup window leaves some characters and highlights
1) Open ```~/.vim/colors/monokai.vim ``` with some text editer (like vim).
2) Find the line which starts with
```
hi Pmenu ...
```
3) Modify ```ctermbg=None``` to ```ctermbg=0``` in the same line.

## Conda
Move to the repo and type this on your command line.
```
python conda.py
```
Restart your session or type this.
```
source ~/.bashrc
```
