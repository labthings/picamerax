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


Links
=====

* The code is licensed under the `BSD license`_
* The `source code`_ can be obtained from GitHub, which also hosts the `bug
  tracker`_
* The `documentation`_ (which includes installation, quick-start examples, and
  lots of code recipes) can be read on ReadTheDocs
* Packages can be downloaded from `PyPI`_, but reading the installation
  instructions is more likely to be useful


.. _Raspberry Pi: https://www.raspberrypi.org/
.. _camera: https://www.raspberrypi.org/learning/getting-started-with-picamera/
.. _PyPI: https://pypi.python.org/pypi/picamera/
.. _documentation: https://picamera.readthedocs.io/
.. _source code: https://github.com/waveform80/picamera
.. _bug tracker: https://github.com/waveform80/picamera/issues
.. _BSD license: https://opensource.org/licenses/BSD-3-Clause

