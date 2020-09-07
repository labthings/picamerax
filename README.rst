.. -*- rst -*-

=========
PiCameraX
=========

PiCamera + Extras
-----------------

This package provides a pure Python interface to the `Raspberry Pi`_ `camera`_
module for Python 3.2 or above, with extra features and fixes.

* Lens-shading table support (from rwb27/master)
* Read-write analog gain (from rwb27/master)
* Greyworld AWB (from chrisruk/greyworld)
* Bayer array support for HQ camera (from AlecVercruysse/master)
* Dropped support for Python 2

Why?
----

The upstream waveform80/picamera library has reached a point of stability meaning some more cutting-edge 
features will be unsuitable for inclusion, or face delays. 
This fork will include new features and fixes more rapidly, allowing the latest camera revisions, and
more experimental software features, to be easily used much earlier than they would otherwise.

Installation
------------

.. code-block::

  pip install picamerax

Links
-----

* The code is licensed under the `BSD license`_
* The `source code`_ can be obtained from GitHub, which also hosts the `bug
  tracker`_
* The `documentation`_ (which includes installation, quick-start examples, and
  lots of code recipes) can be read on ReadTheDocs
* Packages can be downloaded from `PyPI`_, but reading the installation
  instructions is more likely to be useful


.. _Raspberry Pi: https://www.raspberrypi.org/
.. _camera: https://www.raspberrypi.org/learning/getting-started-with-picamerax/
.. _PyPI: https://pypi.python.org/pypi/picamerax/
.. _documentation: https://picamerax.readthedocs.io/
.. _source code: https://github.com/waveform80/picamerax
.. _bug tracker: https://github.com/waveform80/picamerax/issues
.. _BSD license: https://opensource.org/licenses/BSD-3-Clause

Developer notes
---------------

Why CalVer?
^^^^^^^^^^^

We want `picamerax` to stay more or less in sync with upstream `picamera`. However, this fork
adds significant new features that would constitute new version numbers under semantic versioning.
If we were to adopt SemVer, we would rapidly fall completely out of sync with the upstream version
numbers. 

By using calendar versioning, and clearly tracking new additions to the library, we
can ensure the upstream base version is obvious (by looking at its release date in relation to 
our current calendar version), without worrying about what new features count as justifying 
new semantic versions.

This can change however if everyone else deems it a bad idea.
