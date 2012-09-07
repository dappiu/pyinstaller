hiddenimports = ['PySide.QtCore']

from PyInstaller.hooks.hookutils import qt4_plugins_binaries


def hook(mod):
    # Network Bearer Management in Qt4 4.7+
    mod.binaries.extend(qt4_plugins_binaries('bearer', pyside=True))
    return mod
