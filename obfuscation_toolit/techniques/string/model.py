import base64
import binascii
from obfuscation_toolit.core.base import BaseObfuscator


class StringObfuscator(BaseObfuscator):
    def __init__(self, level: int = 1):
        if level < 1:
            raise ValueError("Level must be at least 1")
        self.level = level
    
    def obfuscate(self, code: str) -> str:
        if not code:
            return code
        result = code.encode('utf-8')
        for _ in range(self.level):
            result = base64.b64encode(result)
        return result.decode('utf-8')
    
    def deobfuscate(self, code: str) -> str:
        if not code:
            return code
        try:
            result = code.encode('utf-8')
            for _ in range(self.level):
                result = base64.b64decode(result)
            return result.decode('utf-8')
        except (binascii.Error, UnicodeDecodeError) as e:
            raise ValueError(f"Invalid obfuscated string: {e}")
