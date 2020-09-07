.. _api_array:

============
API - Arrays
============

.. module:: picamerax.array

.. currentmodule:: picamerax.array

The picamerax library provides a set of classes designed to aid in construction
of n-dimensional `numpy`_ arrays from camera output. In order to avoid adding a
hard dependency on numpy to picamerax, this module (:mod:`picamerax.array`) is
not automatically imported by the main picamerax package and must be explicitly
imported, e.g.::

    import picamerax
    import picamerax.array

.. _numpy: http://www.numpy.org/


PiArrayOutput
=============

.. autoclass:: PiArrayOutput


PiRGBArray
==========

.. autoclass:: PiRGBArray


PiYUVArray
==========

.. autoclass:: PiYUVArray


PiBayerArray
============

.. autoclass:: PiBayerArray


PiMotionArray
=============

.. autoclass:: PiMotionArray


PiAnalysisOutput
================

.. autoclass:: PiAnalysisOutput


PiRGBAnalysis
=============

.. autoclass:: PiRGBAnalysis


PiYUVAnalysis
=============

.. autoclass:: PiYUVAnalysis


PiMotionAnalysis
================

.. autoclass:: PiMotionAnalysis


PiArrayTransform
================

.. autoclass:: PiArrayTransform

