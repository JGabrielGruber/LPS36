import inspect
import sys


class LPS36Error(RuntimeError):

    retriable = False

    def __str__(self):
        if not self.args:
            return self.__class__.__name__
        return '{0}: {1}'.format(
            self.__class__.__name__,
            super(LPS36Error, self).__str__()
        )
