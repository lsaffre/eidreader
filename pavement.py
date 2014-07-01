import shutil
from paver.easy import task, sh, path, needs


JARFILE = 'EIDReader.jar'

LIBDIR = path('libs')
SOURCEDIR = path('src/eidreader')
SOURCES = list(SOURCEDIR.files('*.java'))

LIBJARS = ['eid-applet-service.jar',
           'commons-codec.jar',
           'commons-logging.jar']

CLASSES = [path('Manifest.txt')]
for src in SOURCES:
    CLASSES.append(path(src.replace('.java', '.class')))

for n in ['PersonalFile', 'BelgianReader', 'EstEIDUtil']:
    CLASSES.append(SOURCEDIR / n + '.class')

CLASSPATH = []
for n in LIBJARS:
    CLASSPATH.append(LIBDIR / n)
CLASSPATH = ':'.join(CLASSPATH)


def update(src, dst):
    if not dst.exists() or src.mtime - dst.mtime > 1:
        shutil.copy2(src, dst)


def build_jar(alias):
    outdir = path('example') / alias
    jarfile = outdir / JARFILE
    m = max([f.mtime for f in CLASSES])
    # m = None
    # for fn in CLASSES:
    #     if m is None or fn.mtime > m:
    #         m = fn.mtime
    if not jarfile.exists() or jarfile.mtime < m:
        sh("jar cvfm %s %s" % (jarfile, ' '.join(CLASSES)))


def sign_jars(alias, flags):
    outdir = path('example') / alias
    jarfile = outdir / JARFILE
    sh("jarsigner %s %s %s" % (flags, jarfile, alias))
    for n in LIBJARS:
        jarfile = outdir / n
        update(LIBDIR / n, jarfile)
        sh("jarsigner %s %s %s" % (flags, jarfile, alias))


@task
def classes():
    # CLASSPATH = "example/eid-applet-service.jar:example/commons-codec.jar"
    JFLAGS = "-Xlint:unchecked -classpath %s" % CLASSPATH
    for src in SOURCES:
        sh("javac %s %s" % (JFLAGS, src))


@task
@needs('classes')
def jars():
    flags = '-storepass "`cat ~/.secret/.keystore_password`"'
    build_jar('mykey')
    sign_jars('mykey', flags)

    flags += ' -tsa http://timestamp.globalsign.com/scripts/timestamp.dll'
    build_jar('codegears')
    sign_jars('codegears', flags)



"""

jars_mykey: classes
	export SIGNERFLAGS = -storepass "`cat ~/.secret/.keystore_password`"
	export ALIAS = mykey
	export JARDIR = example/$(ALIAS)
	jar cvfm $(JARDIR)/$(JARFILE) $(OBJECTS)
	jarsigner $(SIGNERFLAGS) $(JARDIR)/$(JARFILE) $(ALIAS)
	jarsigner $(SIGNERFLAGS) $(JARDIR)/eid-applet-service.jar $(ALIAS)
	jarsigner $(SIGNERFLAGS) $(JARDIR)/commons-codec.jar $(ALIAS)
	jarsigner $(SIGNERFLAGS) $(JARDIR)/commons-logging.jar $(ALIAS)

jars_codegears: classes
	export SIGNERFLAGS=-tsa http://timestamp.globalsign.com/scripts/timestamp.dll -storepass "`cat ~/.secret/.keystore_password`"
	export ALIAS = codegears
	export JARDIR = example/$(ALIAS)s
	jar cvfm $(JARDIR)/$(JARFILE) $(OBJECTS)
	jarsigner $(SIGNERFLAGS) $(JARDIR)/$(JARFILE) $(ALIAS)
	jarsigner $(SIGNERFLAGS) $(JARDIR)/eid-applet-service.jar $(ALIAS)
	jarsigner $(SIGNERFLAGS) $(JARDIR)/commons-codec.jar $(ALIAS)
	jarsigner $(SIGNERFLAGS) $(JARDIR)/commons-logging.jar $(ALIAS)

clean:
	rm -f src/eidreader/*.class
	rm -f example/mykey/*.jar
	rm -f example/codegears/*.jar

xpi:
	cd firefox/eidreader ; make xpi

"""
