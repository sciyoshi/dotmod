from setuptools import setup, find_packages

setup(
	name='dotmod',
	version='0.0.3',
	description='Import Python packages from folders with dotted names',
	url='https://github.com/sciyoshi/dotmod/',
	author='Samuel Cormier-Iijima',
	author_email='sciyoshi@gmail.com',
	license='MIT',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
	],
	keywords='namespace modules dotmod imports hooks importhook packages',
	install_requires=[
		'six>=1.8.0'
	],
	py_modules=[
		'dotmod'
	])
