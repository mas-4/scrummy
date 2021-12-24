.PHONY:
clean:
	rm -rf build dist scrummy.egg-info
build: clean
	python setup.py sdist bdist_wheel
publish: build
	twine upload dist/*