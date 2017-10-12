'''Module documentation.

* This code raises a ``TypeError`` coming from re.py. See log
* If ``_Errors.__getattr__`` returns something else, e.g. a string, the
  documentation builds
* If the ``_Errors`` instance is assigned to a private variable an underscore,
  the documentation builds and the variable is not shown, despite using
  :private-members:
'''


class _Errors(object):
    "some doc"
    def __getattr__(self, name):
        return ValueError


variable = _Errors()
'''A test'''
