from setuptools import setup, Extension
import numpy.distutils.misc_util

setup(
    name = 'sphaira',
    version = '0.1',
    description = 'Work with spherical images.',
    url = 'http://sphaira.org',
    author = 'Mate Kovacs',
    author_email = 'mkovaxx@gmail.com',
    license = 'BSD',
    packages = [
        'sphaira',
    ],
    ext_modules = [
        Extension(
            'sphaira.external',
            ['sphaira/external.c'],
            include_dirs = numpy.distutils.misc_util.get_numpy_include_dirs(),
        ),
    ],
    install_requires = [
        'numpy',
        'pillow',
        'pyglet',
        'pyrr',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Topic :: Multimedia',
    ],
)
