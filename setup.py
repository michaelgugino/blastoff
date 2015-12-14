'''To be run as an inplace module'''
import sys, io, os, glob
from setuptools import setup, find_packages, Extension
from distutils.core import setup
from setuptools.command.test import test as TestCommand
#from Cython.Build import cythonize
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

try:
    from Cython.Distutils import build_ext
    CYTHON = True
except ImportError:
    CYTHON = False

if CYTHON:
    def list_modules(dirname):
        filenames = glob.glob(os.path.join(dirname, '*.py'))

        module_names = []
        for name in filenames:
            module, ext = os.path.splitext(os.path.basename(name))
            if module != '__init__':
                module_names.append(module)

        return module_names

    ext_modules = [
        Extension('blastoff.' + ext, [os.path.join('blastoff', ext + '.py')])
        for ext in list_modules(os.path.join('.', 'blastoff'))]

    ext_modules += [
        Extension('blastoff.views.' + ext, [os.path.join('blastoff', 'views', ext + '.py')])
        for ext in list_modules(os.path.join('.', 'blastoff', 'views'))]


    cmdclass = {'build_ext': build_ext, 'test': PyTest}

setup(
  name = 'BlastOff! app',
  ext_modules = ext_modules,
)
