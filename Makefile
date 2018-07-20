

flags = --html --all-submodules --html-no-source --overwrite

all: reset doc rename

doc: 
	pdoc ${flags} src/miniDna

rename:
	mv miniDna docs

reset:
	rm -rf docs/*


