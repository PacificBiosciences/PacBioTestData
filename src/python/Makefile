.PHONY: all clean install

all: install

install:
	python setup.py install

clean:
	rm -rf build dist
	rm -rf pbtestdata/data
	rm -rf pbtestdata/version.py
	find . -name "*.egg-info" | xargs rm -rf
	find . -name "*.pyc" | xargs rm -f
	find . -name "*.err" | xargs rm -f
	find . -name "*.log" | xargs rm -f
