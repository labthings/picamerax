.. _install:

============
Installation
============

.. currentmodule:: picamerax


It is simplest to install system wide using Python's ``pip`` tool:

.. code-block:: console

    $ sudo pip install picamerax

If you wish to use the classes in the :mod:`picamerax.array` module then specify
the "array" option which will pull in numpy as a dependency:

.. code-block:: console

    $ sudo pip install "picamerax[array]"

.. warning::

    Be warned that older versions of pip will attempt to build numpy from
    source. This will take a *very* long time on a Pi (several hours on slower
    models). Modern versions of pip will download and install a pre-built
    numpy "wheel" instead which is much faster.

To upgrade your installation when new releases are made:

.. code-block:: console

    $ sudo pip install -U picamerax

If you ever need to remove your installation:

.. code-block:: console

    $ sudo pip uninstall picamerax


.. _firmware:

Firmware upgrades
=================

The behaviour of the Pi's camera module is dictated by the Pi's firmware. Over
time, considerable work has gone into fixing bugs and extending the
functionality of the Pi's camera module through new firmware releases. Whilst
the picamerax library attempts to maintain backward compatibility with older Pi
firmwares, it is only tested against the latest firmware at the time of
release, and not all functionality may be available if you are running an older
firmware. As an example, the :attr:`~PiCamera.annotate_text` attribute relies
on a recent firmware; older firmwares lacked the functionality.

You can determine the revision of your current firmware with the following
command:

.. code-block:: console

    $ uname -a

The firmware revision is the number after the ``#``:

.. code-block:: text

    Linux kermit 3.12.26+ #707 PREEMPT Sat Aug 30 17:39:19 BST 2014 armv6l GNU/Linux
                            /
                           /
      firmware revision --+

On Raspbian, the standard upgrade procedure should keep your firmware
up to date:

.. code-block:: console

    $ sudo apt-get update
    $ sudo apt-get upgrade

.. warning::

    Previously, these documents have suggested using the ``rpi-update`` utility
    to update the Pi's firmware; this is now discouraged. If you have
    previously used the ``rpi-update`` utility to update your firmware, you can
    switch back to using ``apt`` to manage it with the following commands:

    .. code-block:: console

        $ sudo apt-get update
        $ sudo apt-get install --reinstall libraspberrypi0 libraspberrypi-{bin,dev,doc} \
        >   raspberrypi-bootloader
        $ sudo rm /boot/.firmware_revision

    You will need to reboot after doing so.

.. note::

    Please note that the `PiTFT`_ screen (and similar GPIO-driven screens)
    requires a custom firmware for operation. This firmware lags behind the
    official firmware and at the time of writing lacks several features
    including long exposures and text overlays.


.. _Raspbian: https://www.raspberrypi.org/downloads/raspbian/
.. _PiTFT: https://www.adafruit.com/product/1601
