"""
PyGel is a graph emulation library. It can be used to simulate, generate, store, various types of graphs and data structures.

"""

from distutils.core import setup


CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering :: Mathematics',
    ]

try:
    import distutils.command.register
except ImportError:
    kwds = {}
else:
    kwds = {'classifiers': CLASSIFIERS}

setup(name         = 'pygel',
      version      = '2.70',
      author       = 'Saket Sathe',
      author_email = 'xaeroman@users.sourceforge.net',
      license      = 'Apache License, Version 2',
      packages     = ['pygel',
                      'pygel.BaseElements',
                      'pygel.Exceptions',
                      'pygel.MetaClass',
                      'pygel.RandomGraphs',
                      'pygel.Graph'],
      **kwds
      )
