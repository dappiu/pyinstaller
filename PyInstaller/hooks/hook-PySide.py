import sys
from PyInstaller.hooks.hookutils import qt4_menu_nib_dir

# For Qt to work on Mac OS X it is necessary include
# directory qt_menu.nib. This directory contains some
# resource files necessary to run PyQt/PySide app.
if sys.platform.startswith('darwin'):
    datas = [
        (qt4_menu_nib_dir(), ''),
    ]
