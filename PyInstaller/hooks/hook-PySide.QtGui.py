hiddenimports = ['PySide.QtCore']

from PyInstaller.hooks.hookutils import qt4_plugins_binaries


def hook(mod):
    mod.binaries.extend(qt4_plugins_binaries('accessible', pyside=True))
    mod.binaries.extend(qt4_plugins_binaries('iconengines', pyside=True))
    mod.binaries.extend(qt4_plugins_binaries('imageformats', pyside=True))
    mod.binaries.extend(qt4_plugins_binaries('inputmethods', pyside=True))
    mod.binaries.extend(qt4_plugins_binaries('graphicssystems', pyside=True))
    return mod
