#!/bin/bash
#
#
#




## Create directories
echo 'Creating directories'
mkdir -p $HOME/.toolkits/{.tkit-meta,.tkit-data,.tkit-bin,.tkit-libexec}
echo 'Cloning tkitman'
git clone https://github.com/ac0ra/tkitman.git $HOME/.toolkits/tkitman
cd $HOME/.toolkits/tkitman/
make install_meta
echo 'Please add PATH=$PATH:$HOME/.toolkits/.tkit-bin/ to your bashrc etc'
