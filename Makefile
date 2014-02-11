#~ how to generate a self-signed key:
#~ keytool -genkey
#~ keytool -selfcert
#~ keytool -list


#~ requires eid-applet-service-1.0.1.GA.jar downloaded 
#~ from http://code.google.com/p/eid-applet/

JFLAGS =
# JFLAGS = -d build -sourcepath src
# JFLAGS = -Xlint:unchecked 
JFLAGS = -Xlint:unchecked  -classpath example/eid-applet-service.jar:example/commons-codec.jar


JC = javac
#ALIAS = mykey
ALIAS = codegears

.SUFFIXES: .java .class

.java.class:
	$(JC) $(JFLAGS) $*.java

JARFILE = example/EIDReader.jar

SIGNERFLAGS = -tsa http://timestamp.globalsign.com/scripts/timestamp.dll -storepass "`cat ~/.secret/.keystore_password`"

SOURCES = src/eidreader/EIDReader.java

OBJECTS = Manifest.txt $(SOURCES:.java=*.class) src/eidreader/PersonalFile.class src/eidreader/BelgianReader.class src/eidreader/EstEIDUtil.class

default: jars

classes: $(SOURCES:.java=.class)

jars: classes
#	jar cvfm example/EIDReader-unsigned.jar $(OBJECTS)
	jar cvfm $(JARFILE) $(OBJECTS)
	jarsigner $(SIGNERFLAGS) $(JARFILE) $(ALIAS)
	jarsigner $(SIGNERFLAGS) example/eid-applet-service.jar $(ALIAS)
	jarsigner $(SIGNERFLAGS) example/commons-codec.jar $(ALIAS)
	jarsigner $(SIGNERFLAGS) example/commons-logging.jar $(ALIAS)


clean:
	rm -f src/eidreader/*.class
	rm -f $(JARFILE) example/EIDReader-unsigned.jar

xpi:
	cd firefox/eidreader ; make xpi

