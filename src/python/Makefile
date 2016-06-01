.PHONY: all clean install

all: install

install:
	pip install ./

clean:
	rm -rf build dist
	rm -rf pbtestdata/data
	find . -name "*.egg-info" | xargs rm -rf
	find . -name "*.pyc" | xargs rm -f
	find . -name "*.err" | xargs rm -f
	find . -name "*.log" | xargs rm -f
