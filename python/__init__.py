import os
import sys

_netgen_bin_dir=os.path.realpath(os.path.join(os.path.dirname(__file__),'..','@NETGEN_PYTHON_RPATH_BIN@'))
_netgen_lib_dir=os.path.realpath(os.path.join(os.path.dirname(__file__),'..','@NETGEN_PYTHON_RPATH@'))

if sys.platform.startswith('win'):
    os.environ['PATH'] += ';'+os.path.realpath(os.path.join(os.path.dirname(__file__),'../../../bin'))

del sys
del os

from . import libngpy
