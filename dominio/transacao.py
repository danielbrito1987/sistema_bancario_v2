from abc import ABC, abstractmethod, abstractproperty

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(valor):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass