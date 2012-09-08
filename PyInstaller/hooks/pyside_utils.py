import os
from PyInstaller.utils import misc

import PyInstaller.log as logging
logger = logging.getLogger('PyInstaller.build.hooks')

from PyInstaller.hooks.hookutils import eval_statement


def pyside_plugins_dir():
    plugin_dirs = eval_statement(
        "from PySide.QtCore import QCoreApplication;"
        "app=QCoreApplication([]);"
        "print map(unicode,app.libraryPaths())")
    if not plugin_dirs:
        logger.error("Cannot find PySide plugin directories")
        return ""
    for d in plugin_dirs:
        if os.path.isdir(d):
            return str(d)  # must be 8-bit chars for one-file builds
    logger.error("Cannot find existing PySide plugin directory")
    return ""


def pyside_plugins_binaries(plugin_type):
    """Return list of dynamic libraries formated for mod.binaries."""
    binaries = []
    pdir = pyside_plugins_dir()
    files = misc.dlls_in_dir(os.path.join(pdir, plugin_type))
    for f in files:
        binaries.append((
            os.path.join('pyside_plugins', plugin_type, os.path.basename(f)),
            f, 'BINARY'))
    return binaries
