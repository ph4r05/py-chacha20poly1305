# Authors:
#   Trevor Perrin
#   Martin von Loewis - python 3 port
#   Yngve Pettersen (ported by Paul Sokolovsky) - TLS 1.2
#
# See the LICENSE file for legal information regarding use of this file.

"""cryptomath module

This module has basic math/crypto code."""
from __future__ import print_function


def divceil(divident, divisor):
    """Integer division with rounding up"""
    quot, r = divmod(divident, divisor)
    return quot + int(bool(r))

