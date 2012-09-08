import os
import sys
import site

from PyInstaller import is_win, is_py26, is_py27
from PyInstaller import compat
from PyInstaller.hooks.pyside_utils import pyside_plugins_dir
from PyInstaller.hooks.hookutils import qt4_menu_nib_dir


def _getsitepackages_backport_26():
    """Copied from Python 2.7 Lib/site.py source, r87497.

    Returns a list containing all global site-packages directories
    (and possibly site-python).

    For each directory present in the global ``PREFIXES``, this function
    will find its `site-packages` subdirectory depending on the system
    environment, and will return a list of full paths.
    """
    sitepackages = []
    seen = set()

    for prefix in site.PREFIXES:
        if not prefix or prefix in seen:
            continue
        seen.add(prefix)

        if sys.platform in ('os2emx', 'riscos'):
            sitepackages.append(os.path.join(prefix, "Lib", "site-packages"))
        elif os.sep == '/':
            sitepackages.append(os.path.join(prefix, "lib",
                                             "python" + sys.version[:3],
                                             "site-packages"))
            sitepackages.append(os.path.join(prefix, "lib", "site-python"))
        else:
            sitepackages.append(prefix)
            sitepackages.append(os.path.join(prefix, "lib", "site-packages"))
        if sys.platform == "darwin":
            # for framework builds *only* we add the standard Apple
            # locations.
            from sysconfig import get_config_var
            framework = get_config_var("PYTHONFRAMEWORK")
            if framework and "/%s.framework/" % (framework,) in prefix:
                sitepackages.append(os.path.join("/Library", framework,
                                    sys.version[:3], "site-packages"))
    return sitepackages


def getsitepackages():
    sitepackages = []
    if is_py27:
        sitepackages = site.getsitepackages()
    elif is_py26:
        sitepackages = _getsitepackages_backport_26()

    # else we don't care because PySide requires Python >= 2.6

    return sitepackages


def find_first_pyside_path():
    for site_path in getsitepackages():
        pyside_path = os.path.join(site_path, 'PySide')
        if os.path.exists(pyside_path):
            return pyside_path
    return None


def prepend_to_dll_search_path(path):
    if path is not None:
        env_path = path + os.pathsep + compat.getenv('PATH')
        compat.setenv('PATH', env_path)

# On Windows the system PATH has to be extended to point to the PySide
# directory which contains the Qt dlls. If we don't do this we risk
# including different version of Qt libraries found on the PATH,
# e.g. when QtCreator is also installed.
if is_win:
    prepend_to_dll_search_path(find_first_pyside_path())

# For Qt to work on Mac OS X it is necessary include
# directory qt_menu.nib. This directory contains some
# resource files necessary to run PyQt/PySide app.
if sys.platform.startswith('darwin'):
    datas = [
        (qt4_menu_nib_dir(), ''),
    ]
