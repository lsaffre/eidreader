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


def sign_jars(outdir, alias, flags):
    jarfile = outdir / JARFILE
    m = max([f.mtime for f in CLASSES])
    if not jarfile.exists() or jarfile.mtime < m:
        sh("jar cvfm %s %s" % (jarfile, ' '.join(CLASSES)))
    sh("jarsigner %s %s %s" % (flags, jarfile, alias))
    for n in LIBJARS:
        jarfile = outdir / n
        update(LIBDIR / n, jarfile)
        sh("jarsigner %s %s %s" % (flags, jarfile, alias))


@task
def classes():
    JFLAGS = "-Xlint:unchecked -classpath %s" % CLASSPATH
    for src in SOURCES:
        sh("javac %s %s" % (JFLAGS, src))


@task
@needs('classes')
def jars():
    flags = '-storepass "`cat ~/.secret/.keystore_password`"'
    sign_jars(path('example'), 'mykey', flags)

    flags += ' -tsa http://timestamp.globalsign.com/scripts/timestamp.dll'
    sign_jars(path('example/signed'), 'codegears', flags)



"""
clean:
	rm -f src/eidreader/*.class
	rm -f example/signed/*.jar

"""
