# dotmod

[![Build Status](https://travis-ci.org/sciyoshi/dotmod.svg?branch=master)](https://travis-ci.org/sciyoshi/dotmod)

This project adds support for dotted folder names to Python's import system!

## Installation

Install it using `pip`:

    pip install dotmod

To use it, simply add the following line of code to one of your files:

	import dotmod

This will install a global import hook that will check for folders with
dotted names.

## Why?

If you are distributing a large application or library as separate components,
the normal way is to use namespace packages. Before Python 3.3, this was
accomplished by using `pkgutil.extend_path` or `pkg_resources.declare_namespace`
(see [the (rejected) PEP-402](http://legacy.python.org/dev/peps/pep-0402/#the-problem)
for details).

Python 3.3 added support for namespace packages without an `__init__.py` file,
so that a package could be split up across different locations in the filesystem.
The downside to this approach is that `sys.path` needs to be extended for each
one of these locations.

`dotmod` provides an approach that is compatible across Python releases. It
works by adding an import hook that checks for packages and modules with dotted
names as a fallback. For example, consider the following directory tree:

    spam/
     |- __init__.py
     |- sausage.py
     `- eggs/
         |- __init__.py
         `- ham.py
    spam.bacon/
     |- __init__.py
     `- beans.py

With `dotmod`, when a module attempts to import `spam.bacon.beans`, the hook
will notice that there is no `bacon` module in the `spam/` folder, and will
then check `spam.bacon/` for the module instead.
