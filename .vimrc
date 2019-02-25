set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
Plugin 'Valloric/YouCompleteMe'
Plugin 'scrooloose/nerdtree'
Plugin 'Yggdroot/indentLine'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

" utf-8 encoding
set encoding=utf-8

" show line numbers
set number

" enable syntax highlighting
syntax enable

" set tabs to have 4 spaces
set ts=4

" expand tabs into spaces 
set expandtab

" number of spaces in tab when editing
set softtabstop=4

" indent when moving to the next line while writing code
set autoindent

" when using the >> or << commands, shift lines by 4 spaces
set shiftwidth=4

" show a visual line under the cursor's current line
set nocursorline

" show the matching part of the pair for [] {} and () 
set showmatch

" enable all Python syntax highlighting features
let python_highlight_all = 1

" color scheme
colorscheme monokai

" visual aotocomplete for command menu
set wildmenu

" redraw only when we need to
set lazyredraw

" searching 
set incsearch " search as characters are entered
set hlsearch " highlight matches

" split panes more naturally
set splitbelow
set splitright

" key mapping changes
" navigating across panes
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" toggling nerd tree
map <C-n> :NERDTreeToggle<CR>

" remove search highlights
nnoremap <esc><esc> :noh<return>

" not using swap files
set noswapfile

" turn off annoying function docs in YCM
set completeopt-=preview

" show current full path in status line
set laststatus=2
"set statusline=%!getcwd()
set statusline=%F
" set mouse enable
set mouse=n
