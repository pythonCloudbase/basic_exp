### keYLOGGER IN PYTHON

https://pynput.readthedocs.io/en/latest

Dependency:

`sudo apt-get install python-xlib`

`pip install pyH`

`pyinstaller --onefile hello.py`

When using a packager I get an ImportError on startup
This happens when using a packager, such as PyInstaller, to package your application.

The reason for the error is that the packager attempts to build a dependency tree of the modules used by inspecting import statements, and pynput finds the platform dependent backend modules at runtime using importlib.

To solve this problem, please consult the documentation of your tool to find how to explicitly add modules.

Which modules to add depends on your distribution platform. The backend modules are those starting with an underscore ('_') in the pynput.keyboard and pynput.mouse packages. Additionally, you will need modules with corresponding names from the pynput._util package.