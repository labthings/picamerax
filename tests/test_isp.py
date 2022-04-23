# vim: set et sw=4 sts=4 fileencoding=utf-8:
#
# Python camera library for the Rasperry-Pi camera module
# Copyright (c) 2013-2017 Dave Jones <dave@waveform.org.uk>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from __future__ import (
    unicode_literals,
    print_function,
    division,
    absolute_import,
    )

# Make Py2's str equivalent to Py3's
str = type('')

import os
import tempfile
import picamerax
import pytest
from collections import namedtuple
from verify import RAW_FORMATS


RecordingCase = namedtuple('RecordingCase', ('format', 'ext', 'options'))

RECORDING_CASES = (
    RecordingCase('h264',  '.h264', {'splitter_port': 1, 'inline_headers': True, 'intra_period': 1,
                                     'resize': (320, 240), 'use_isp_resizer': False}),
    RecordingCase('h264',  '.h264', {'splitter_port': 1, 'inline_headers': True, 'intra_period': 1,
                                     'resize': (320, 240), 'use_isp_resizer': True}),
    ) + tuple(
    RecordingCase(fmt,     '.data', {'splitter_port': 1, 'resize': (320, 240), 'use_isp_resizer': False})
    for fmt in RAW_FORMATS
    if not fmt.startswith('bgr')
    ) + tuple(
    RecordingCase(fmt,     '.data', {'splitter_port': 1, 'resize': (320, 240), 'use_isp_resizer': True})
    for fmt in RAW_FORMATS
    if not fmt.startswith('bgr')
    )


@pytest.fixture(params=RECORDING_CASES)
def filenames_format_options(request):
    filename1 = tempfile.mkstemp(suffix=request.param.ext)[1]
    filename2 = tempfile.mkstemp(suffix=request.param.ext)[1]
    def fin():
        os.unlink(filename1)
        os.unlink(filename2)
    request.addfinalizer(fin)
    return filename1, filename2, request.param.format, request.param.options


# Run tests with a variety of format specs
@pytest.fixture(params=RECORDING_CASES)
def format_options(request):
    return request.param.format, request.param.options


def verify_resizer(camera, options):
    if options['use_isp_resizer'] is True:
        return isinstance(camera._encoders[options['splitter_port']].resizer, picamerax.mmalobj.MMALISPResizer)
    else:
        return isinstance(camera._encoders[options['splitter_port']].resizer, picamerax.mmalobj.MMALResizer)


def test_isp_resizer(camera, mode, filenames_format_options):
    # Ensure the ISP resizer is used when required
    # Tests to verify outputs are included in `test_record.py`
    filename1, filename2, format, options = filenames_format_options
    resolution, framerate = mode
    camera.start_recording(filename1, format=format, **options)
    try:
        camera.wait_recording(1)
        assert verify_resizer(camera, options)
        camera.split_recording(filename2)
        camera.wait_recording(1)
        assert verify_resizer(camera, options)
    finally:
        camera.stop_recording()
