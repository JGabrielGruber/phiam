from hug.types import Type
from re import match

class Email(Type):
    """Valid email"""
    __slots__ = ()

    def __call__(self, value):
        if not match(
            "^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$",
            value
        ):
            raise ValueError('Invalid email provided')
        return str(value)

email = Email()
