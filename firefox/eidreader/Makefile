XPIFILE = ../../example/eidreader.xpi

default: xpi

xpi:
	rm $(XPIFILE)
	zip $(XPIFILE) chrome.manifest install.rdf content/*.js content/*.xul
