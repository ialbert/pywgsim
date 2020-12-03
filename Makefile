
UNAME := $(shell uname -s)
SNAME := pywgsim/lib/wgsim_mod.c
PNAME := scripts/pywgsim-$(UNAME)
CFLAGS := -g -O2 -Wall

.PHONY: build clean sdist devel

all:
	@echo "Compiling $(PNAME)"
	gcc $(CFLAGS) -o $(PNAME) $(SNAME) -lz -lm

clean:
	rm -rf dist build pywgsim.egg-info scripts/pywgsim-*

sdist:
	python setup.py sdist

devel:
	python setup.py develop

build:
	python setup.py sdist

upload: build
	rm -rf dist
	python setup.py sdist
	#python -m twine upload --repository testpypi dist/*
	python -m twine upload --repository pypi dist/*

