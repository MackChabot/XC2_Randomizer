# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['scripts\\XC2_Randomizer.py'],
    pathex=[],
    binaries=[],
    datas=[('_internal/Images', 'Images'), ('_internal/Toolset/bdat-toolset-win64.exe', 'Toolset')],
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
    a.binaries,
    a.datas,
    [],
    name='XC2_Randomizer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['_internal\\Images\\XC2Icon.ico'],
)
