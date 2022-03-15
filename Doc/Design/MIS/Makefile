PY = python3
PYFLAGS = 
DOC = doxygen
DOCFLAGS = 
DOCCONFIG = docconfig

SRC = ../../../src/apply.py

.PHONY: all prog doc clean

prog: 
	$(PY) $(PYFLAGS) $(SRC)

doc: 
	$(DOC) $(DOCFLAGS) $(DOCCONFIG)
	cd latex && $(MAKE)

all: prog doc

clean:
	rm -rf html
	rm -rf latex
