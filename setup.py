# All copyrights and related or neighbouring rights waived under CC0.
# http://creativecommons.org/publicdomain/zero/1.0/
# To the extent possible under law, Andrew Chadwick has waived all
# copyright and related or neighboring rights to this program. This
# program is published from: United Kingdom.

"""Minimal GTK setup.py for cx_Freeze, GObject-Introspection on MSYS2.

To build from the MINGW64 or MINGW32 shell:

    $ rm -fr build && python2 setup.py build_exe

To run from the Windows command line:

    X:\\> cd path\\to\\build\exe.mingw-2.7 && hellogtk && cd\\ || cd\\

This setup script only supports build_exe.

"""

import os, site, sys
from cx_Freeze import setup, Executable


assert sys.platform == "win32"


# Frozen executables made by build_exe need to have everything that GTK
# loads at runtime available under the root where the built .exe goes.

common_include_files = []


# On MSYS2's MINGW64/32 enrironments, the DLLs we want are in PATH.
# Typically this means /mingw64/bin/libwhatever.dll.  An alternative way
# of forming the list of required DLLs would be to parse the relevant
# .gir files (see below). However, libpangowin32-1.0-0.dll wouldn't be
# listed.

required_dll_search_paths = os.getenv("PATH", os.defpath).split(os.pathsep)
required_dlls = [
    'libgtk-3-0.dll',
    'libgdk-3-0.dll',
    'libepoxy-0.dll',
    'libgdk_pixbuf-2.0-0.dll',
    'libpango-1.0-0.dll',
    'libpangocairo-1.0-0.dll',
    'libpangoft2-1.0-0.dll',
    'libpangowin32-1.0-0.dll',
    'libatk-1.0-0.dll',
]

for dll in required_dlls:
    dll_path = None
    for p in required_dll_search_paths:
        p = os.path.join(p, dll)
        if os.path.isfile(p):
            dll_path = p
            break
    assert dll_path is not None, \
        "Unable to locate {} in {}".format(
            dll,
            dll_search_path,
        )
    common_include_files.append((dll_path, dll))


# We need the .typelib files at runtime.
# The related .gir files are in $PREFIX/share/gir-1.0/$NS.gir,
# but those can be omitted at runtime.

required_gi_namespaces = [
    "Gtk-3.0",
    "Gdk-3.0",
    "cairo-1.0",
    "Pango-1.0",
    "GObject-2.0",
    "GLib-2.0",
    "Gio-2.0",
    "GdkPixbuf-2.0",
    "GModule-2.0",
    "Atk-1.0",
]

for ns in required_gi_namespaces:
    subpath = "lib/girepository-1.0/{}.typelib".format(ns)
    fullpath = os.path.join(sys.prefix, subpath)
    assert os.path.isfile(fullpath), (
        "Required file {} is missing" .format(
            fullpath,
        ))
    common_include_files.append((fullpath, subpath))


# Packages that need to be bundled go here.

common_packages = [
    "gi",   # always seems to be needed
    # "cairo",   # Only needed (for foreign structs) if no "import cairo"s
]


# Executables to build.

exe1 = Executable(
    script = "hellogtk.py",
    targetName = "hellogtk.exe",
    base = "Win32GUI",
)

exe2 = Executable(
    script = "hellogtk.py",
    targetName = "hellogtk_console.exe",
    base = "Console",
)


# This is a build_exe-only setup script.

setup(
    name = "hellogtk",
    author = "Andrew Chadwick",
    version = "0.1",
    description = "GTK3+Cairo Hello World",
    options = {
        "build_exe": dict(
            compressed = False,
            include_files = common_include_files,
            silent = True,
            packages = common_packages,
        ),
    },
    executables = [exe1, exe2],
)
