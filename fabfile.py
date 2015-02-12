from atelier.fablib import *
setup_from_fabfile(globals())

env.revision_control_system = 'git'

from atelier.jarbuilder import JarBuilder
jb = JarBuilder(
    'EIDReader.jar', 'src/eidreader',
    'http://timestamp.globalsign.com/scripts/timestamp.dll')

jb.add_lib("libs/eid-applet-service.jar")
jb.add_lib("libs/commons-codec.jar")
jb.add_lib("libs/commons-logging.jar")


@task
def classes():
    jb.build_classes()


@task
def jars():
    classes()
    jb.build_jar('example', 'mykey')
    # jb.build_jar('example/signed', 'codegears')
