# cython: language_level=3
#!/home/toni/.pyenv/shims/python3
'''
Created on Oct 20, 2019

@author:toni
'''

from setuptools import setup
from Cython.Build import cythonize
from Cython.Compiler import Options

Options.language_level = 3


setup(
    name='hello_app',
    ext_modules=cythonize('hello.pyx'),
    zip_safe=False,
)
