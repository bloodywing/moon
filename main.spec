# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
import pymunk
import pyxel
import os
import glob

src_lib_dir = os.path.dirname(pyxel.core._get_absolute_libpath())
dst_lib_dir = os.path.dirname(pyxel.core._get_relative_libpath())
libs = filter(os.path.isfile, glob.glob(os.path.join(src_lib_dir, "*")))

binaries = [
    ( pymunk.chipmunk_path, '.' )
]


for lib in libs:
    libname = os.path.basename(lib)
    binaries.append((os.path.join(src_lib_dir, libname), dst_lib_dir))

a = Analysis(['main.py'],
             pathex=['/home/pierre/repositories/gameoff2020'],
             binaries=binaries,
             datas=[(os.path.join('moongame', 'assets'), 'moongame/assets')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main',
          debug=False,
          onefile=True,
          bootloader_ignore_signals=False,
          strip=False,)
