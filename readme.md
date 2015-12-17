Histogram Plot Normalized to Sum 1
==================================

Plot 1D histogram, optionally normalized to counts within specified range.

This module defines a single function ``his()`` that calls ``pyplot.hist()``
with or without custom weights, adjusted to normalize counts by the number of
elements  **WITHIN** the given input range. This is different from the
``normed=True`` option in ``pyplot.hist()``, where the integral of the histogram
adds to 1.

Warning : not tested with options like cumulative, log, etc.

Basic Usage
-----------
    from his import his
    x = 0.1*np.random.randn(1000) + 0.5

    # Histogram normalized to sum 1
    his(x, bins=40, range=[0,1], rangenorm=True)
    # Histogram normalized to sum 1 within custom range
    his(x, bins=40, range=[0.4,0.6], rangenorm=True)

Credits
-------
Emilio Donoso
