from PyInstaller.hooks.pyside_utils import pyside_plugins_binaries


def hook(mod):
    mod.binaries.extend(pyside_plugins_binaries('codecs'))
    return mod
