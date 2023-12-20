# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['merlinator.py', 'main_gui.py', 'treeviews.py', 'io_utils.py', 'gui_actions.py', 'audio.py', 'audio_converter.py'],
    pathex=['data/'],
    binaries=[],
    datas=[('data/defaultPics.zip', '.'), ('data/defaultPics.zip', 'data')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='merlinator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    contents_directory='data',
)
