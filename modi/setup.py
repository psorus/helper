from distutils.core import setup, Extension
setup(name="modi", version="1.0",
      ext_modules=[Extension("modi", ["modi.c"])])
