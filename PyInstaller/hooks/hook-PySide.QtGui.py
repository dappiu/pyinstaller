hiddenimports = ['PySide.QtCore']

from PyInstaller.hooks.pyside_utils import pyside_plugins_binaries


def hook(mod):
    mod.binaries.extend(pyside_plugins_binaries('iconengines'))
    mod.binaries.extend(pyside_plugins_binaries('imageformats'))
    return mod
