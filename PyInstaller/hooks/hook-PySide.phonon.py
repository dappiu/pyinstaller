hiddenimports = ['PySide.QtGui']

from PyInstaller.hooks.hookutils import qt4_plugins_binaries


def hook(mod):
    mod.binaries.extend(qt4_plugins_binaries('phonon_backend', pyside=True))
    return mod
