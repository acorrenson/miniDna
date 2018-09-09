

flags = --html --all-submodules --html-no-source --overwrite

repo = https://test.pypi.org/legacy/

all: reset-doc doc rename verify

verify:
	python3 -m verify.core
	
# documentation

doc: install
	pdoc ${flags} src/miniDna

install:
	sudo python3 setup.py install

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