# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['page.py'],
    pathex=[],
    binaries=[],
    datas=[('_internal/Images', 'Images'), ('_internal/Toolset/bdat-toolset-win64.exe', 'Toolset'), ('__pycache__', '__pycache__')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='page',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='_internal/Images/XC2Icon.ico'
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='page',
    distpath='./dist',
)
