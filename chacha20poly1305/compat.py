# Author: Trevor Perrin
# See the LICENSE file for legal information regarding use of this file.

"""Miscellaneous functions to mask Python version differences."""

import sys
import platform
import hmac

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


if hasattr(hmac, 'compare_digest'):
    ct_compare_digest = hmac.compare_digest
else:
    def ct_compare_digest(val_a, val_b):
        """Compares if string like objects are equal. Constant time."""
        if len(val_a) != len(val_b):
            return False

        result = 0
        for x, y in zip(val_a, val_b):
            result |= x ^ y

        return result == 0

