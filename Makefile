

flags = --html --all-submodules --html-no-source --overwrite

repo = https://test.pypi.org/legacy/

all: doc rename

# documentation

doc: 
	pdoc ${flags} src/miniDna

rename:
	mv miniDna docs

reset-doc:
	rm -rf docs

# upload and dist

publish: dist
	twine upload --repository-url ${repo} dist/*

dist:
	python3 setup.py sdist bdist_wheel
