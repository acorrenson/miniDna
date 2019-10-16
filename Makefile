

flags = --html --output-dir docs

path = src/miniDna

repo = https://test.pypi.org/legacy/

all: doc
	
# documentation

doc: install
	pdoc ${flags} ${path}
	mv docs/miniDna/* docs
	rmdir docs/miniDna

install:
	sudo python3 setup.py install


# upload and dist

publish: dist
	twine upload --repository-url ${repo} dist/*

dist: reset-dist
	python3 setup.py sdist bdist_wheel

reset-dist:
	rm -rf dist