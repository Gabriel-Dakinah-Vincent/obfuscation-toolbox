from abc import ABC, abstractmethod


class BaseObfuscator(ABC):
    @abstractmethod
    def obfuscate(self, code: str) -> str:
        pass
    
    @abstractmethod
    def deobfuscate(self, code: str) -> str:
        pass
