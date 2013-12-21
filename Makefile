#~ how to generate a self-signed key:
#~ keytool -genkey
#~ keytool -selfcert
#~ keytool -list


#~ requires eid-applet-service-1.0.1.GA.jar downloaded 
#~ from http://code.google.com/p/eid-applet/

#~ JFLAGS = -d build -sourcepath src
#~ JFLAGS = -Xlint:unchecked 
#~ JFLAGS = -classpath ~/Downloads/eid-applet-sdk/eid-applet-service-1.0.1.GA.jar
# JFLAGS =
JFLAGS = -classpath applets/eid-applet-service.jar:applets/commons-codec.jar


JC = javac
#ALIAS = mykey
ALIAS = codegears

.SUFFIXES: .java .class

.java.class:
	$(JC) $(JFLAGS) $*.java

JARFILE = applets/EIDReader.jar

SIGNERFLAGS = -tsa http://timestamp.globalsign.com/scripts/timestamp.dll -storepass "`cat ~/.secret/.keystore_password`"

SOURCES = src/eidreader/EIDReader.java

OBJECTS = Manifest.txt $(SOURCES:.java=*.class) src/eidreader/PersonalFile.class src/eidreader/BelgianReader.class src/eidreader/EstEIDUtil.class

default: jars

classes: $(SOURCES:.java=.class)

jars: classes
#	jar cvfm applets/EIDReader-unsigned.jar $(OBJECTS)
	jar cvfm $(JARFILE) $(OBJECTS)
	jarsigner $(SIGNERFLAGS) $(JARFILE) $(ALIAS)
	jarsigner $(SIGNERFLAGS) applets/eid-applet-service.jar $(ALIAS)
	jarsigner $(SIGNERFLAGS) applets/commons-codec.jar $(ALIAS)
	jarsigner $(SIGNERFLAGS) applets/commons-logging.jar $(ALIAS)


clean:
	rm src/eidreader/*.class
	rm $(JARFILE) applets/EIDReader-unsigned.jar

sync:
	cp -vur applets/* ~/vbshared2/drives/T/applets/

xpi:
	cd firefox/eidreader ; make xpi

