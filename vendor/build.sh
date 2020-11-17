#!/bin/sh

git clone --depth 1 https://github.com/kitao/pyxel.git
wget https://www.libsdl.org/projects/SDL_image/release/SDL2_image-2.0.5.tar.gz
wget https://www.libsdl.org/release/SDL2-2.0.12.tar.gz

tar xpf SDL2_image-2.0.5.tar.gz
tar xpf SDL2-2.0.12.tar.gz

PREFIX="$PWD/dist"
mkdir -p $PREFIX
cd SDL2-2*/
mkdir build
cd build
../configure --disable-static --prefix=$PREFIX
make dist-clean
make -j4
make install
cd ../..

cd SDL2_image-*/
mkdir build
cd build
../configure --disable-static --prefix=$PREFIX
make dist-clean
make -j4
make install
cd ../..

make -C pyxel/pyxel/core/ clean
PATH=$PREFIX/bin:$PATH make -j4 -C pyxel/pyxel/core/ all
pip install ./pyxel/ -U

#PYXEL_INSTALL_PATH=$(dirname $(python -c 'import pyxel;print(pyxel.__file__)'))
#find "$PREFIX/lib/" -iname 'lib*.*' -exec cp -H {} $PYXEL_INSTALL_PATH/core/bin/linux/ \;
