"""
dist_funcs
==========

Probability distribution functions for anything under the sun that arsenal
needs.
"""


from typing import Type

import astropy.units as u
import numpy as np
from astropy.units import Quantity


class ProbDistFunc():
    """
    This class is the superclass of all PDFs that arsenal will use.

    :param pdf_min: Lower limit for the PDF.  Probabilities for values below this will be zero
    :type pdf_min: float
    :param pdf_max: Upper limit for the PDF.  Probabilities for values above this will be zero
    :type pdf_max: float
    :param normalized: Should we return a normalized version of the probability when called, or just a function proportional to it?
    :type normalized: bool
    """
    def __init__(self, pdf_min:float, pdf_max:float, normalized:bool=False) -> None:
        self.min = pdf_min
        self.max = pdf_max
        if normalized:
            self.norm = self.normalization()
        else:
            self.norm = 1

    def normalization(self) -> float:
        """
        Return the normalization for this PDF.  The default base class returns a uniform distribution.

        :return: The normalization for the PDF (it's integral from self.min to self.max)
        :rtype: float
        """
        return self.max - self.min

    def prob(self, x: np.float64) -> np.float64:
        """
        Return the NON-NORMALIZED probability for value(s) x.

        :param x: The values to sample P(x) for.
        :type x: np.float64
        :return: The non-normalized probability for x
        :rtype: np.float64
        """
        return np.ones(x.shape)

    def __call__(self, x: np.float64) -> np.float64:
        """
        Return the probability for value(s) x, normalized if the PDF is initialized
        with normalized = True

        :param x: The values to sample P(x) for.
        :type x: np.float64
        :return: The probability for x, normalized if desired.
        :rtype: np.float64
        """
        p = self.prob(x)
        p[np.logical_or(x < self.min, x > self.max)] = 0
        return p/self.norm

from . import imf
