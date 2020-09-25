#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Motion Photo Extraction
Video extraction for motion photos taken by Google camera app.
"""

import re
import sys
from os import path

__author__ = "Marc Schwede"
__license__ = "MIT License"
__version__ = "0.1"

def persist_file(filename, videodata):
    videoname = filename.replace('.jpg', '.mp4')
    if path.exists(videoname):
        sys.exit('Error: videofile %s already exists' % videoname)
    with open(videoname, 'wb') as f:
        f.write(videodata)

def extract(filename):
    with open(filename, 'rb') as file:
        data = file.read()
        length = re.findall(b'Length="(\d*)"', data)
        if not re.search(b'Mime="video/mp4"', data) or len(length) < 2:
            sys.exit('Error: no videocontent found in file %s' % filename)
        file.seek(-int(length[1].decode('utf-8')), 2)
        tmp = file.read()
        persist_file(filename, tmp)

if len(sys.argv) > 2:
    sys.exit('Wrong usage: %s <file>' % sys.argv[0])

filename = sys.argv[1]
extract(filename)
