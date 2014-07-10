from __future__ import print_function

from atelier.fablib import *
setup_from_project()

env.use_mercurial = False  # i.e. use git

jb = JarBuilder('EIDReader.jar', 'src/eidreader')

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
    jb.build_jar('example/signed', 'codegears')
