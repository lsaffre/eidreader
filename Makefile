#~ how to generate a self-signed key:
#~ keytool -genkey
#~ keytool -selfcert
#~ keytool -list


#~ requires eid-applet-service-1.0.1.GA.jar downloaded 
#~ from http://code.google.com/p/eid-applet/

#~ JFLAGS = -d build -sourcepath src
#~ JFLAGS = -Xlint:unchecked 
#~ JFLAGS = -classpath ~/Downloads/eid-applet-sdk/eid-applet-service-1.0.1.GA.jar
JFLAGS = -classpath applets/eid-applet-service.jar
#~ JFLAGS = 

JC = javac

.SUFFIXES: .java .class

.java.class:
	$(JC) $(JFLAGS) $*.java

JARFILE = applets/EIDReader.jar

CLASSES = src/eidreader/EIDReader.java

default: jars

classes: $(CLASSES:.java=.class)

jars: classes
	jar cvfm $(JARFILE) Manifest.txt src/eidreader
	jarsigner -storepass "`cat ~/.secret/.keystore_password`" $(JARFILE) mykey

clean:
	rm src/eidreader/*.class
	rm $(JARFILE)
