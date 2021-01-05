from setuptools import setup, find_packages
from setuptools.extension import Extension

try:
    from Cython.Build import cythonize

    USE_CYTHON = True
except ImportError as exc:
    USE_CYTHON = False

# Build the package differently when Cython is present.
ext = 'pyx' if USE_CYTHON else 'c'

import pywgsim

with open("README.md", "r") as fh:
    long_description = fh.read()

extensions = [
    Extension(
        name="pywgsim.wgsim",
        sources=["pywgsim/wgsim_lib." + ext, "pywgsim/src/wgsim_mod.c"],
        depends=["pywgsim/src/wgsim_mod.h", "pywgsim/src/kseq.h"],
        libraries=["z", "m"],
        include_dirs=["pywgsim/src"]
    ),
]

if USE_CYTHON:
    from Cython.Build import cythonize

    extensions = cythonize(extensions)

setup(
    name="pywgsim",
    version=pywgsim.VERSION,
    author="Istvan Albert",
    author_email="istvan.albert@gmail.com",
    description="pywgsim",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ialbert/pywgsim",
    packages=find_packages(include=["pywgsim", "pywgsim.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Operating System :: POSIX',
        'Programming Language :: C',
        'Programming Language :: Cython',
    ],
    install_requires=[
        'plac',
    ],

    entry_points={
        'console_scripts': [
            'pywgsim=pywgsim.main:run',
        ],
    },

    include_package_data=True,

    python_requires='>=3.6',

    ext_modules=extensions,

)
