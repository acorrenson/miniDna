
all: doc index.html
	firefox doc/index.html

doc: reset
	pdoc --html --html-no-source --html-dir doc src/miniDna.py

index.html:
	mv doc/miniDna.m.html doc/index.html

reset:
	rm -rf doc/*
