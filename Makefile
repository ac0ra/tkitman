.PHONY: test upload clean bootstrap build

SHELL=/bin/bash


_build:
	@for a in $$(find ./src -type d); do \
	if [ -d $$a ]; then \
	echo "processing folder $$a"; \
	if [ -f $$a/Makefile ]; then \
	$(MAKE) -C $$a; \
	fi; \
	fi; \
	done;
	@echo "Done!"


build: _build

install_meta:
	@for a in $$(find ./src -type d); do \
	if [ -d $$a ]; then \
	echo "processing folder $$a"; \
	if [ -f $$a/Makefile ]; then \
	$(MAKE) -C $$a install_meta; \
	fi; \
	fi; \
	done;
	@echo "Done!"

upload: 
	make clean

	
register:
	python setup.py register

clean:
	rm -rf venv
	rm -rf build/*
	rm -rf bin/tkitman-*
	rm -rf install.sh
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	
bootstrap: _virtualenv
ifneq ($(wildcard setup.py),)
	venv/bin/pip install -e .
endif
ifneq ($(wildcard requirements.txt),) 
	venv/bin/pip install -r requirements.txt
endif

_virtualenv_init: 
	python3 -m venv venv

_virtualenv: _virtualenv_init
	venv/bin/pip install --upgrade pip
	venv/bin/pip install --upgrade setuptools
