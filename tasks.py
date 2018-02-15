from atelier.invlib.ns import ns
ns.setup_from_tasks(
    globals(), 
    # tolerate_sphinx_warnings=True,
    blogref_url="http://luc.lino-framework.org",
    revision_control_system='git')

from atelier.jarbuilder import JarBuilder
jb = JarBuilder(
    'EIDReader.jar', 'src/eidreader',
    'http://timestamp.globalsign.com/scripts/timestamp.dll')

jb.add_lib("libs/eid-applet-service.jar")
jb.add_lib("libs/commons-codec.jar")
jb.add_lib("libs/commons-logging.jar")


try:
    from invoke import ctask as task
    # before version 0.13 (see http://www.pyinvoke.org/changelog.html)
except ImportError:
    from invoke import task

@task
def classes(ctx):
    jb.build_classes()


@task(name='jars')
def jars(ctx):
    classes(ctx)
    jb.build_jar(ctx, 'example', 'mykey')
    # jb.build_jar('example/signed', 'codegears')
