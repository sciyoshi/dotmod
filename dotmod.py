import os
import imp
import sys
import six

class DotImportHook:
	def find_module(self, fullname, path=None):
		bits = fullname.split('.')

		if len(bits) <= 1:
			return

		for folder in sys.path:
			if os.path.exists(os.path.join(folder, fullname)):
				return self

		for i in range(1, len(bits) - 1):
			package, mod = '.'.join(bits[:i]), '.'.join(bits[i:])

			path = sys.modules[package].__path__

			for folder in path:
				if os.path.exists(os.path.join(folder, mod)):
					return self

	def load_module(self, fullname):
		if fullname in sys.modules:
			return sys.modules[fullname]

		sys.modules[fullname] = module = imp.new_module(fullname)

		if '.' in fullname:
			pkg, name = fullname.rsplit('.', 1)
			path = sys.modules[pkg].__path__
		else:
			pkg, name = '', fullname
			path = sys.path

		module.__package__ = pkg
		module.__loader__ = self

		bits = fullname.split('.')

		if len(bits) <= 1:
			return module

		for folder in sys.path:
			pathfunc = lambda *args: os.path.join(folder, fullname, *args)

			if os.path.exists(pathfunc()):
				module.__path__ = [pathfunc()]
				module.__file__ = pathfunc('__init__.pyc')

				six.exec_(open(pathfunc('__init__.py')).read(), module.__dict__)

				return module

		for i in range(1, len(bits) - 1):
			package, mod = '.'.join(bits[:i]), '.'.join(bits[i:])

			path = sys.modules[package].__path__

			for folder in path:
				pathfunc = lambda *args: os.path.join(folder, mod, *args)

				if os.path.exists(pathfunc()):
					module.__path__ = [pathfunc()]
					module.__file__ = pathfunc('__init__.pyc')

					six.exec_(open(pathfunc('__init__.py')).read(), module.__dict__)

					return module

		# somehow not found, delete from sys.modules
		del sys.modules[fullname]

# support reload()ing this module
try:
	hook
except NameError:
	pass
else:
	try:
		sys.meta_path.remove(hook)
	except ValueError:
		# not found, skip removing
		pass

# automatically install hook
hook = DotImportHook()

sys.meta_path.insert(0, hook)
