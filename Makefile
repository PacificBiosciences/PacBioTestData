.PHONY: all clean install

all: install

python: install

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

test:
	$(eval DATASETS := `find data -name '*set.xml'`)
	@for XML in $(DATASETS); do \
		echo $$XML ;\
		grep 'ResourceId="/' $$XML && exit 1; \
		pbvalidate --quick $$XML || exit 1 ;\
	done
