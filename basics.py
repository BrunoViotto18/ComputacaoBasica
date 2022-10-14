from __future__ import annotations
from multimethods import multimethod


class Bit:
    def __init__(self, value: bool = False) -> None:
        self.__value: bool = value

    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool) -> None:
        self.__value = value

    def __bool__(self) -> None:
        raise NotImplementedError('__bool__ não implementado, não usar os operadores lógicos "and", "or" ou "not", ou qualquer processo que se baseie no valor lógico do objeto em si.')

    @multimethod
    def __and__(self, bit: bool) -> Bit:
        return Bit(self.__value and bit)

    @multimethod
    def __and__(self, bit: Bit) -> Bit:
        return Bit(self.__value and bit.value)

    @multimethod
    def __or__(self, bit: bool) -> Bit:
        return Bit(self.__value or bit)

    @multimethod
    def __or__(self, bit: Bit) -> Bit:
        return Bit(self.__value or bit.value)

    def __invert__(self) -> Bit:
        return Bit(not self.value)

    def __str__(self) -> str:
        return '1' if self.value else '0'
