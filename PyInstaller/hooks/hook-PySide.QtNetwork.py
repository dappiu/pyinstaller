hiddenimports = ['PySide.QtCore']

from PyInstaller.hooks.pyside_utils import pyside_plugins_binaries


def hook(mod):
    # Network Bearer Management in Qt4 4.7+
    mod.binaries.extend(pyside_plugins_binaries('bearer'))
    return mod
