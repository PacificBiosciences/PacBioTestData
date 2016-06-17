.PHONY: python

python:
	cd src/python && make install

clean:
	cd src/python && make clean
