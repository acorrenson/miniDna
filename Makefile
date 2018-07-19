
all: doc index.html
	firefox docs/index.html

doc: reset
	pdoc --html --html-no-source --html-dir docs src/miniDna.py

index.html:
	mv docs/miniDna.m.html docs/index.html

reset:
	rm -rf docs/*
