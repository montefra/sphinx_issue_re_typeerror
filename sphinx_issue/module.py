'''Module documentation.

* :attr:`errors`: some attribute.
'''
a_module = None


class _Errors(object):
    def __getattr__(self, name):
        if a_module:
            return getattr(a_module, name)
        else:
            return Exception


errors = _Errors()
'''A test'''
