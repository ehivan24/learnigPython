from distutils.core import setup
from Cython.Distutils import build_ext
from distutils.extension import Extension


exts = [Extension("helloCython", ["hello.pyx"],)]

setup(
      cmdclass = {'build_ext': build_ext},
      ext_modules = exts,
      )


#python setup.py build_ext --inplace

"""
hello.pyx

def sayHello(name):
    print ("hello World %s" %name)
"""


# in ipython we import it as
# import fib
# and we call fib.sayHello("Edwing")

