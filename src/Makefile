PY = python3
PYFLAGS = 
DOC = doxygen
DOCFLAGS = 
DOCCONFIG = ../Doc/Design/MIS/docconfig
PYCOMPILER = pyinstaller

SRC = apply.py

.PHONY: all prog doc clean comp

prog: 
	$(PY) $(PYFLAGS) $(SRC)

doc: 
	$(DOC) $(DOCFLAGS) $(DOCCONFIG)
	cd latex && $(MAKE)

comp: 
	$(PYCOMPILER) --onefile $(SRC)

all: comp prog doc

clean:
	rm -rf dist
	rm -rf build
	rm apply.spec
