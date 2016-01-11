## Hello, cx_Freeze and GTK+

This repo currently contains a minimal test integration of
[cx_Freeze][cxfreeze] with [PyGObject][pygi] runtime stuff.

> ![Unremarkable screenshot](https://cloud.githubusercontent.com/assets/61299/12250457/dfb4f68e-b8be-11e5-8097-54e3e11fafde.png)  
> -- This, but as a `.exe`

It supports [GTK 3.x][gtk] and [Cairo 1.x][cairo] modules initially.
To build the test executable on Windows,
you need to install [MSYS2][msys2] first and upgrade its core packages.
Then, if you're using the MINGW32 shell environment that ships with MSYS2,

```
# pacman -S mingw-w64-i686-gtk3
# pacman -S mingw-w64-i686-python2-cx_Freeze
# pacman -S mingw-w64-i686-python2-cairo
# python setup.py build_exe
```

Change `i686` to `x86_64` if you're testing with the MINGW64 shell.

The resultant executables end up in `build\exe.mingw-2.7`, and can be
run by double-clicking them in Windows Explorer. To test them from the
Windows command line, use something like

```
C:\> G:
G:\> cd hello-cxfreeze-gtk\build\exe.mingw-2.7 && hellogtk && cd\ || cd\
```

To go beyond what this Hello World script does will need more DLLs and
typelib files to be bundled for use at runtime. But this is a start.

[cxfreeze]: https://cx-freeze.readthedocs.org
[gtk]: https://en.wikipedia.org/wiki/GTK%2B
[cairo]: http://cairographics.org/
[msys2]: https://msys2.github.io/
[pygi]: https://wiki.python.org/moin/PyGobject
