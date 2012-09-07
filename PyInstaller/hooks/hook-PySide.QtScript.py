hiddenimports = [ 'PyQt4.QtCore']

from PyInstaller.hooks.hookutils import qt4_plugins_binaries


def hook(mod):
    mod.binaries.extend(qt4_plugins_binaries('script', pyside=True))
    return mod
