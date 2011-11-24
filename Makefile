install:
	cp src/eclipse_get.py /usr/bin/eclipse-get
	chmod +x /usr/bin/eclipse-get
	mkdir -p /opt/eclipse-get
	cp -r data /opt/eclipse-get/data

remove:
	rm /usr/bin/eclipse-get
	rm -r /opt/eclipse-get
