from setuptools import setup, find_packages
from setuptools.extension import  Extension
from Cython.Build import cythonize
import pywgsim

with open("README.md", "r") as fh:
    long_description = fh.read()

pywgsim_ext = Extension(
    name="pywgsim.wgsim",
    sources=["pywgsim/lib/wgsim_mod.c", "pywgsim/wgsim.pyx"],
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


    python_requires='>=3.6',

    ext_modules=cythonize([pywgsim_ext])

)

