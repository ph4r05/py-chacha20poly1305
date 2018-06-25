# Author: Trevor Perrin
# See the LICENSE file for legal information regarding use of this file.

"""Miscellaneous functions to mask Python version differences."""

import sys
import platform

if sys.version_info >= (3,0):
    def compat26Str(x): return x

else:
    # Python 2.6 requires strings instead of bytearrays in a couple places,
    # so we define this function so it does the conversion if needed.
    # same thing with very old 2.7 versions
    # or on Jython
    if sys.version_info < (2, 7) or sys.version_info < (2, 7, 4) or platform.system() == 'Java':
        def compat26Str(x): return str(x)
    else:
        def compat26Str(x): return x

