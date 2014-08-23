#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Showcases *blackbody* computations.
"""

from __future__ import division, unicode_literals

import colour

# Calculating *blackbody* spectral radiance.
colour.planck_law(500 * 1e-9, 5500)

# Converting temperature to *CIE XYZ*.
cmfs = colour.STANDARD_OBSERVERS_CMFS.get(
    'CIE 1931 2 Degree Standard Observer')
blackbody_spd = colour.blackbody_spd(5000, cmfs.shape)
XYZ = colour.spectral_to_XYZ(blackbody_spd, cmfs)
print(XYZ)