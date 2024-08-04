# -*- mode: python ; coding: utf-8 -*-

# menu_generator.spec

from PyInstaller.utils.hooks import collect_data_files

# Include data files (fonts and image)
datas = [
    ('Garet-Book.ttf', 'fonts'),
    ('Garet-Heavy.ttf', 'fonts'),
    ('bg.jpg', '.')
]

# PyInstaller configuration
a = Analysis(
    ['card_automation.py'],  # Ensure this matches your script name
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    cipher=None,  # Use None for no encryption
    noarchive=False,
)

# Remove cipher from PYZ and EXE
pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='menu_generator',
    debug=False,
    strip=False,
    upx=True,
    console=False,
    bundle=False,
    bootloader_ignore_signals=False,
    runtime_tmpdir=None,
    specpath=None,
    noarchive=False,
)
