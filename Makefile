PYTHON=python
CONNSTR=scott/tiger@myorcl

all: clean
	$(PYTHON) Weaver
	rm -f *.pyc
	@echo to test: make test CONNSTR=myname/mypass@mydb

clean:
	rm -f *.html
	rm -f *.pyc

test:
	sh -c 'for f in *.py; do echo ======= $$f;$(PYTHON) $$f $(CONNSTR);done'
	rm -f *.pyc
