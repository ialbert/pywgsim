from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize
import pywgsim

with open("README.md", "r") as fh:
    long_description = fh.read()

pywgsim_ext = Extension(
    name="pywgsim.wgsim",
    sources=[ "pywgsim/wgsim.pyx", "pywgsim/lib/wgsim_mod.c"],
    depends=["pywgsim/lib/wgsim_mod.h", "pywgsim/lib/kseq.h"],
    libraries=["z", "m"],
    include_dirs=["pywgsim/lib"]
)

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
        'cython',
        'plac',
    ],

    entry_points={
        'console_scripts': [
            'pywgsim=pywgsim.main:run',
        ],
    },

    package_data={"pywgsim": ["*.pyx", "lib/*.h", "lib/*.c"]},

    python_requires='>=3.6',

    ext_modules=cythonize([pywgsim_ext])

)
