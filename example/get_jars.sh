# download and unpack third-party jars
# copyright notice see file readme.rst
wget http://eid-applet.googlecode.com/files/eid-applet-sdk-1.1.0.GA.zip
unzip eid-applet-sdk-1.1.0.GA.zip
mv eid-applet-sdk-1.1.0.GA/eid-applet-service-1.1.0.GA.jar eid-applet-service.jar
rm -R eid-applet-sdk-1.1.0.GA
rm eid-applet-sdk-1.1.0.GA.zip

wget http://archive.apache.org/dist/commons/logging/binaries/commons-logging-1.1.3-bin.tar.gz
tar -xvzf commons-logging-1.1.3-bin.tar.gz 
mv commons-logging-1.1.3/commons-logging-1.1.3.jar commons-logging.jar
rm -R commons-logging-1.1.3
rm commons-logging-1.1.3-bin.tar.gz

wget http://archive.apache.org/dist/commons/codec/binaries/commons-codec-1.8-bin.tar.gz
tar -xvzf commons-codec-1.8-bin.tar.gz
mv commons-codec-1.8/commons-codec-1.8.jar commons-codec.jar
rm -R commons-codec-1.8
rm commons-codec-1.8-bin.tar.gz

