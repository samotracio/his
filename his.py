# -*- coding: utf-8 -*-
""" Plot 1D histogram, optionally normalized to counts within specified range.

Fork of ``pyplot.hist()`` with extra argument to control counts normalization

* rangenorm = False  :  do counts at each bin

* rangenorm = True   :  do counts/counts(range) at each bin. This is effectively
                        the fraction of elements at each bin, so the sum of
                        these fractions add to 1.

This module defines a single function ``his()`` that calls ``pyplot.hist()``
with or without custom weights, adjusted to normalize counts by the number of
elements  **WITHIN** the given input range. This is different from the
``normed=True`` option in ``pyplot.hist()``, where the integral of the histogram
adds to 1.

Warning : not tested with options like cumulative, log, etc.

Basic Usage
-----------
::

    from his import his
    x = 0.1*np.random.randn(1000) + 0.5

    # Histogram normalized to sum 1
    his(x, bins=40, range=[0,1], rangenorm=True)
    # Histogram normalized to sum 1 within custom range
    his(x, bins=40, range=[0.4,0.6], rangenorm=True)

Credits
-------
Emilio Donoso
"""
import numpy as np
import matplotlib.pyplot as plt

def his(x, bins=10, range=None, histtype='step', rangenorm=False, **kwargs):
    """
    Plot 1D histogram, optionally normalized to counts within specified range.

    Parameters
    ----------
    Exactly the same as pyplot.hist(), so minimally you should provide -> data,
    bins, range. Extra optional parameter:

    **rangenorm** : bool

    * "False" : do counts at each bin. Default

    * "True" :  do counts/counts(range) at each bin. This is effectively the
                fraction or relative frequency of elements at each bin, so their sum add to 1.

    Returns
    -------
    Same as pyplot.hist() -> (counts, binlims, patches) and the plot

    Examples
    --------
    ::

        from his import his
        x = 0.1*np.random.randn(1000) + 0.5

        # Histogram normalized to sum 1
        his(x, bins=40, range=[0,1], rangenorm=True)
        # Histogram normalized to sum 1 within custom range
        his(x, bins=40, range=[0.4,0.6], rangenorm=True)
    """

    if rangenorm is False:
        ret = plt.hist(x, bins=bins, range=range, histtype=histtype, **kwargs)
    else:
        # Count the elements WITHIN the input range and normalize by that nr.
        # Very different to normalize by len(x), which would include elements
        # outside range. Not tested with other options like cumulative, log, etc.
        cc, xx = np.histogram(x, bins=bins, range=range)
        W = np.ones_like(x)/cc.sum()
        ptsout = len([v for v in x if range[0] > v or v > range[1]])
        if ptsout > 0:
            print "Warning : Points outside given range = %s" % ptsout
        ret = plt.hist(x, bins=bins, range=range, weights=W, histtype=histtype, **kwargs)
    return ret

if __name__ == "__main__":
    import sys
    his(int(sys.argv[1]))
