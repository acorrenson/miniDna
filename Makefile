

flags = --html --all-submodules --html-no-source --overwrite

repo = https://test.pypi.org/legacy/

path = /home/arthur/Documents/Github/miniDna/src

all: reset-doc doc rename

# documentation

doc: set-path
	pdoc ${flags} src/miniDna

set-path:
	export PYTHONPATH=$$PYTHONPATH:${path}

rename:
	mv miniDna docs

reset-doc:
	rm -rf docs

# upload and dist

publish: dist
	twine upload --repository-url ${repo} dist/*

dist: reset-dist
	python3 setup.py sdist bdist_wheel

reset-dist:
	rm -rf dist