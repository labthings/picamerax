.. _api_camera:

========================
API - The PiCamera Class
========================

.. module:: picamerax

The picamerax library contains numerous classes, but the primary one that all
users are likely to interact with is :class:`PiCamera`, documented below.
With the exception of the contents of the :mod:`picamerax.array` module, all
classes in picamerax are accessible from the package's top level namespace.
In other words, the following import is sufficient to import everything in
the library (excepting the contents of :mod:`picamerax.array`)::

    import picamerax

PiCamera
========

.. autoclass:: PiCamera(\*, camera_num=0, stereo_mode='none', stereo_decimate=False, resolution=None, framerate=None, sensor_mode=0, led_pin=None, clock_mode='reset', framerate_range=None, isp_blocks=None)


PiVideoFrameType
================

.. autoclass:: PiVideoFrameType


PiVideoFrame
============

.. autoclass:: PiVideoFrame(index, frame_type, frame_size, video_size, split_size, timestamp)


PiResolution
============

.. autoclass:: PiResolution(width, height)


PiFramerateRange
================

.. autoclass:: PiFramerateRange(low, high)


PiSensorMode
============

.. autoclass:: PiSensorMode(resolution, framerates, video, still, full_fov)
