develop:
	chmod +x src/eclipse_get.py
	ln -s src/eclipse_get.py /usr/bin/eclipse-get
	mkdir /opt/eclipse-get
	ln -s data /opt/eclipse-get/data

install:
	cp src/eclipse_get.py /usr/bin/eclipse-get
	chmod +x /usr/bin/eclipse-get
	mkdir /opt/eclipse-get
	cp -r data /opt/eclipse-get/data

uninstall:
	rm /usr/bin/eclipse-get
	rm -r /opt/eclipse-get