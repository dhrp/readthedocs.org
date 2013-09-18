Welcome to Read The Docs
========================

|status|

.. |status| image:: https://travis-ci.org/rtfd/readthedocs.org.png?branch=master
.. _status: https://travis-ci.org/rtfd/readthedocs.org

`Read the Docs`_ hosts documentation for the open source community. It supports
Sphinx_ docs written with reStructuredText_, and can pull from your Subversion_,
Bazaar_, Git_, and Mercurial_ repositories.

The full documentation is available on `the site`_.

.. _Read the docs: http://readthedocs.org/
.. _Sphinx: http://sphinx.pocoo.org/
.. _reStructuredText: http://sphinx.pocoo.org/rest.html
.. _Subversion: http://subversion.tigris.org/
.. _Bazaar: http://bazaar.canonical.com/
.. _Git: http://git-scm.com/
.. _Mercurial: http://mercurial.selenic.com/
.. _the site: http://read-the-docs.readthedocs.org

The documentation for the site is organized into two different sections below.
One is for users of readthedocs.org, that is the first section. The next section
is for users of the code that powers the site. All of the RTD code is open
source, so you can run your own instance. Presumably in an internal install
inside your company, or something.


dotCloud specific
-----------------

* Make sure postgresql and redis are running. Without redis you might get no warning api errors
* Check set all domain specifics in settings/dotcloud.yml
* Create database 'rtfd'
* Setup the db -> run all manage commands always with --settings=settings.dotcloud
 * ``manage.py Syncdb`` - do not immediately create superuser, as it will fail
 * ``manage.py migrate``
 * ``manage.py createsuperuser``
* Manually copy docker user 'dotcloud.key' to /data/dockeruser.key, it is used to connect to the static app
* Set SLUMBER_PASS in your environment.json, it should match a superuser which is created in the database
* To make sure the static app will accept the rsync command, add the slug name to the static apps' data dir: e.g. 'docker'
