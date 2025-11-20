# Decorators
from functools import wraps
import traceback


def db_ops(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        # class_name = self.__class__.__name__
        try:
            result = func(self, *args, **kwargs)
            self._commit()
            return result
        except Exception as e:
            print(f"\nError: {e}\n")
            self._rollback()
            # traceback.print_exc()

    return wrapper
