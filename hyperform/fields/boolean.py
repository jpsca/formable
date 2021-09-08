from .text import Text
from ..ftypes import type_boolean


__all__ = ("Boolean", )


class Boolean(Text):

    def type(self, value):
        return type_boolean(value)
