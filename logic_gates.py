from abc import ABC, abstractmethod
from multimethods import multimethod
from basics import Bit


class LogicGate(ABC):
    def __init__(self, a: Bit, b: Bit) -> None:
        self.__a = a
        self.__b = b

    @property
    def a(self) -> Bit:
        return self.__a

    @a.setter
    def a(self, value: bool | Bit) -> None:
        if isinstance(value, bool):
            self.__a = Bit(value)
        elif isinstance(value, Bit):
            self.__a = value
        else:
            raise TypeError(f'O tipo "{type(value)}" passado ao LogicGate.a é inválido.')

    @property
    def b(self) -> Bit:
        return self.__b

    @b.setter
    def b(self, value: bool | Bit) -> None:
        if isinstance(value, bool):
            self.__b = Bit(value)
        elif isinstance(value, Bit):
            self.__b = value
        else:
            raise TypeError(f'O tipo "{type(value)}" passado ao LogicGate.b é inválido.')

    @abstractmethod
    def value(self):
        ...


class AndGate(LogicGate):
    def __init__(self, a: Bit = Bit(False), b: Bit = Bit(False)):
        super().__init__(a, b)

    @property
    def value(self) -> Bit:
        return self.a & self.b


class OrGate(LogicGate):
    def __init__(self, a: Bit = Bit(False), b: Bit = Bit(False)):
        super().__init__(a, b)

    @property
    def value(self) -> Bit:
        return self.a | self.b


class NandGate(LogicGate):
    def __init__(self, a: Bit = Bit(False), b: Bit = Bit(False)):
        super().__init__(a, b)

    @property
    def value(self) -> Bit:
        return ~(self.a & self.b)


class NorGate(LogicGate):
    def __init__(self, a: Bit = Bit(False), b: Bit = Bit(False)):
        super().__init__(a, b)

    @property
    def value(self) -> Bit:
        return ~(self.a | self.b)


class XorGate(LogicGate):
    def __init__(self, a: Bit = Bit(False), b: Bit = Bit(False)):
        super().__init__(a, b)

    @property
    def value(self) -> Bit:
        return (self.a | self.b) & ~(self.a & self.b)
