from atelier.fablib import *
setup_from_project()

env.use_mercurial = False  # i.e. use git

import shutil

JARFILE = 'EIDReader.jar'

LIBDIR = Path('libs')
SOURCEDIR = Path('src/eidreader')
SOURCES = list(SOURCEDIR.listdir('*.java'))

LIBJARS = ['eid-applet-service.jar',
           'commons-codec.jar',
           'commons-logging.jar']

CLASSES = [Path('Manifest.txt')]
for src in SOURCES:
    CLASSES.append(Path(src.replace('.java', '.class')))

for n in ['PersonalFile', 'BelgianReader', 'EstEIDUtil']:
    CLASSES.append(SOURCEDIR.child(n + '.class'))

CLASSPATH = []
for n in LIBJARS:
    CLASSPATH.append(LIBDIR.child(n))
CLASSPATH = ':'.join(CLASSPATH)


def update(src, dst):
    if not dst.exists() or src.mtime() - dst.mtime() > 1:
        shutil.copy2(src, dst)


def sign_jars(outdir, alias, flags):
    jarfile = outdir.child(JARFILE)
    m = max([f.mtime() for f in CLASSES])
    if not jarfile.exists() or jarfile.mtime() < m:
        local("jar cvfm %s %s" % (jarfile, ' '.join(CLASSES)))
    local("jarsigner %s %s %s" % (flags, jarfile, alias))
    for n in LIBJARS:
        jarfile = outdir.child(n)
        update(LIBDIR.child(n), jarfile)
        local("jarsigner %s %s %s" % (flags, jarfile, alias))


@task
def classes():
    JFLAGS = "-Xlint:unchecked -classpath %s" % CLASSPATH
    for src in SOURCES:
        local("javac %s %s" % (JFLAGS, src))


@task
def jars():
    classes()
    flags = '-storepass "`cat ~/.secret/.keystore_password`"'
    sign_jars(Path('example'), 'mykey', flags)

    flags += ' -tsa http://timestamp.globalsign.com/scripts/timestamp.dll'
    sign_jars(Path('example/signed'), 'codegears', flags)


