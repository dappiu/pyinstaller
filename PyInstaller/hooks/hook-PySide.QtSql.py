hiddenimports = ['PySide.QtCore', 'PySide.QtGui']

from PyInstaller.hooks.hookutils import qt4_plugins_binaries


def hook(mod):
    mod.binaries.extend(qt4_plugins_binaries('sqldrivers', pyside=True))
    return mod
