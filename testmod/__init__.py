"""
Type alias member sorting for trivial type aliases.

Declarations in the source are sorted by the output order in Sphinx 4.3.1 when
``autodoc_member_order = 'groupwise'``.
Ideally, the type aliases should be grouped together instead.

It seems like Sphinx cannot disambiguate between `int` which is a class and `Union[int, float]`
which is an instance of `typing.Union`.
Thus, using ``groupwise`` appears to treat `AliasInt`, `AliasIntFoo`, and `IntAlias` as classes, and
`AliasUnionIntFloat` and `UnionIntFloatAlias` as data.

In Python 3.10, PEP 613 introduces explicit type aliases for type hints (`typing.TypeAlias`).
Using a `TypeAlias` type hint would presumably resolve the sorting issue, but also imposes
additional burden on the source code to make Sphinx work as expected without any actual runtime
benefits (and requires Python >= 3.10).

Note: the missing docstrings for primitive aliases is resolved in Sphinx issue #9866.
"""
from typing import Union

#: Docstring
AliasInt = int

#: Docstring
class AliasIntClass:
    def __init__(self):
        pass

#: Docstring
AliasIntFoo = int

#: Docstring
class AliasUniontIntFloatClass:
    def __init__(self):
        pass

#: Docstring
IntAlias = int

#: Docstring
AliasUnionIntFloat = Union[int, float]

#: Docstring
UnionIntFloatAlias = Union[int, float]
