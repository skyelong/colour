# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Defines unit tests for :mod:`colour.adaptation.cmccat2000.
"""

from __future__ import division, unicode_literals

import numpy as np
import sys

if sys.version_info[:2] <= (2, 6):
    import unittest2 as unittest
else:
    import unittest

from colour.adaptation.cmccat2000 import CMCCAT2000_forward, CMCCAT2000_reverse

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013 - 2015 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['TestCMCCAT2000Forward',
           'TestCMCCAT2000Reverse']


class TestCMCCAT2000Forward(unittest.TestCase):
    """
    Defines :func:`colour.adaptation.cmccat2000.CMCCAT2000_forward` definition
    unit tests methods.
    """

    def test_CMCCAT2000_forward(self):
        """
        Tests :func:`colour.adaptation.cmccat2000.CMCCAT2000_forward`
        definition.
        """

        np.testing.assert_almost_equal(
            CMCCAT2000_forward(
                np.array([0.07049534, 0.1008, 0.09558313]) * 100,
                np.array([1.09846607, 1., 0.3558228]) * 100,
                np.array([0.95042855, 1., 1.08890037]) * 100,
                100,
                100),
            np.array([8.01087299, 10.89423054, 26.89150177]),
            decimal=7)

        np.testing.assert_almost_equal(
            CMCCAT2000_forward(
                np.array([0.4709771, 0.3495, 0.11301649]) * 100,
                np.array([0.99092745, 1., 0.85313273]) * 100,
                np.array([1.01679082, 1., 0.67610122]) * 100,
                100,
                100),
            np.array([48.97710455, 35.36874611, 9.02878274]),
            decimal=7)

        np.testing.assert_almost_equal(
            CMCCAT2000_forward(
                np.array([0.25506814, 0.1915, 0.08849752]) * 100,
                np.array([0.98070597, 1., 1.18224949]) * 100,
                np.array([0.92833635, 1., 1.0366472]) * 100,
                100,
                100),
            np.array([24.68548451, 19.08228483, 7.81570209]),
            decimal=7)

    def test_n_dimensions_CMCCAT2000_forward(self):
        """
        Tests :func:`colour.adaptation.cmccat2000.CMCCAT2000_forward`
        definition n-dimensions support.
        """

        XYZ = np.array([22.48, 22.74, 8.54])
        XYZ_w = np.array([111.15, 100.00, 35.20])
        XYZ_wr = np.array([94.81, 100.00, 107.30])
        L_A1 = 200
        L_A2 = 200

        XYZ_c = np.array([19.52698326, 23.0683396, 24.97175229])

        np.testing.assert_almost_equal(
            CMCCAT2000_forward(XYZ, XYZ_w, XYZ_wr, L_A1, L_A2),
            XYZ_c,
            decimal=7)

        XYZ = np.tile(XYZ, (6, 1))
        XYZ_c = np.tile(XYZ_c, (6, 1))
        np.testing.assert_almost_equal(
            CMCCAT2000_forward(XYZ, XYZ_w, XYZ_wr, L_A1, L_A2),
            XYZ_c,
            decimal=7)

        XYZ = np.reshape(XYZ, (2, 3, 3))
        XYZ_c = np.reshape(XYZ_c, (2, 3, 3))
        np.testing.assert_almost_equal(
            CMCCAT2000_forward(XYZ, XYZ_w, XYZ_wr, L_A1, L_A2),
            XYZ_c,
            decimal=7)


class TestCMCCAT2000Reverse(unittest.TestCase):
    """
    Defines :func:`colour.adaptation.cmccat2000.CMCCAT2000_reverse` definition
    unit tests methods.
    """

    def test_CMCCAT2000_reverse(self):
        """
        Tests :func:`colour.adaptation.cmccat2000.CMCCAT2000_reverse`
        definition.
        """

        np.testing.assert_almost_equal(
            CMCCAT2000_reverse(
                np.array([8.01087299, 10.89423054, 26.89150177]),
                np.array([1.09846607, 1., 0.3558228]) * 100,
                np.array([0.95042855, 1., 1.08890037]) * 100,
                100,
                100),
            np.array([0.07049534, 0.1008, 0.09558313]) * 100,
            decimal=7)

        np.testing.assert_almost_equal(
            CMCCAT2000_reverse(
                np.array([48.97710455, 35.36874611, 9.02878274]),
                np.array([0.99092745, 1., 0.85313273]) * 100,
                np.array([1.01679082, 1., 0.67610122]) * 100,
                100,
                100),
            np.array([0.4709771, 0.3495, 0.11301649]) * 100,
            decimal=7)

        np.testing.assert_almost_equal(
            CMCCAT2000_reverse(
                np.array([24.68548451, 19.08228483, 7.81570209]),
                np.array([0.98070597, 1., 1.18224949]) * 100,
                np.array([0.92833635, 1., 1.0366472]) * 100,
                100,
                100),
            np.array([0.25506814, 0.1915, 0.08849752]) * 100,
            decimal=7)

    def test_n_dimensions_CMCCAT2000_reverse(self):
        """
        Tests :func:`colour.adaptation.cmccat2000.CMCCAT2000_reverse`
        definition n-dimensions support.
        """

        XYZ = np.array([19.52698326, 23.0683396, 24.97175229])
        XYZ_w = np.array([111.15, 100.00, 35.20])
        XYZ_wr = np.array([94.81, 100.00, 107.30])
        L_A1 = 200
        L_A2 = 200

        XYZ_c = np.array([22.48, 22.74, 8.54])

        np.testing.assert_almost_equal(
            CMCCAT2000_reverse(XYZ, XYZ_w, XYZ_wr, L_A1, L_A2),
            XYZ_c,
            decimal=7)

        XYZ = np.tile(XYZ, (6, 1))
        XYZ_c = np.tile(XYZ_c, (6, 1))
        np.testing.assert_almost_equal(
            CMCCAT2000_reverse(XYZ, XYZ_w, XYZ_wr, L_A1, L_A2),
            XYZ_c,
            decimal=7)

        XYZ = np.reshape(XYZ, (2, 3, 3))
        XYZ_c = np.reshape(XYZ_c, (2, 3, 3))
        np.testing.assert_almost_equal(
            CMCCAT2000_reverse(XYZ, XYZ_w, XYZ_wr, L_A1, L_A2),
            XYZ_c,
            decimal=7)


if __name__ == '__main__':
    unittest.main()
