The `example
<https://github.com/lsaffre/eidreader/tree/master/example>`__
directory is distributed as a part of :ref:`eidreader` project in
order to facilitate deployment.

It contains a set of ready-to use signed `.jar` files and some `.html`
files which are publically served at
http://test-eidreader.lino-framework.org/

.. _third_party_jars:

Note about redistributing third-party jar files
-----------------------------------------------

Three of the four ready-to use signed `.jar` files were obtained from
third party projects, and we redistribute them along with EIDReader
without any code change as signed `.jar` files:

- The file `eid-applet-services.jar` is from the
  `eid-applet <https://code.google.com/p/eid-applet/>`__
  project which is published under the LGPL. 
- `commons-logging.jar` is from the
  `commons-logging <http://commons.apache.org/proper/commons-logging/>`_
  project.
- `commons-codec.jar` is from the
  `commons-codec <http://commons.apache.org/proper/commons-codec/>`_
  project.

Both commons projects are licensed under the `Apache license 2.0
<http://www.apache.org/licenses/LICENSE-2.0>`_ which states that we
"must give any other recipients of the Work or Derivative Works a
copy of this License", so here it is:
`LICENSE-2.0.txt <https://github.com/lsaffre/eidreader/blob/master/example/LICENSE-2.0.txt>`__.

AFAICS I don't need to also redistribute the source code of these jar
files, but here is how you can get them yourself::

  $ cd eidreader/example
  $ ./get_jars.sh
  
The `.jar` files have then been built using the 
`Makefile <https://github.com/lsaffre/eidreader/blob/master/Makefile>`__::

  $ cd ..
  $ make jars


The :file:`get_jars.sh` script will:  
  
-   Download an appropriate version of :file:`eid-applet-sdk-VERSION.zip`
    from the `eid-applet downloads page 
    <http://code.google.com/p/eid-applet/downloads/list>`__
    and extract :file:`eid-applet-service-VERSION.jar`
    into a file :file:`eid-applet-service.jar` in your 
    :file:`example` directory.
    For example something like::

        $ cd eidreader/example
        $ wget http://eid-applet.googlecode.com/files/eid-applet-sdk-1.1.0.GA.zip
        $ unzip eid-applet-sdk-1.1.0.GA.zip
        $ mv eid-applet-sdk-1.1.0.GA/eid-applet-service-1.1.0.GA.jar eid-applet-service.jar
        $ rm -R eid-applet-sdk-1.1.0.GA
    

-   Download an appropriate version of     
    `LogFactory
    <http://commons.apache.org/proper/commons-logging/apidocs/org/apache/commons/logging/LogFactory.html>`_
    from 
    `commons.apache.org <http://commons.apache.org/proper/commons-logging/download_logging.cgi>`_
    and extract a file `commons-logging.jar` from it to your `example` directory.
    For example something like::

        $ wget http://servingzone.com/mirrors/apache//commons/logging/binaries/commons-logging-1.1.3-bin.tar.gz
        $ tar -xvzf commons-logging-1.1.3-bin.tar.gz 
        $ mv commons-logging-1.1.3/commons-logging-1.1.3.jar commons-logging.jar
        $ rm -R commons-logging-1.1.3

        
-   Download an appropriate version of     
    `commons-codec
    <http://commons.apache.org/proper/commons-codec/>`_
    and extract a file `commons-codec.jar` from it to your `example` directory.


        $ wget http://servingzone.com/mirrors/apache//commons/codec/binaries/commons-codec-1.8-bin.tar.gz
        $ tar -xvzf commons-codec-1.8-bin.tar.gz 
        $ mv commons-codec-1.8/commons-codec-1.8.jar commons-codec.jar
        $ rm -R commons-codec-1.8
