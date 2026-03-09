from obfuscation_toolit.core.base import BaseObfuscator


class XorObfuscator(BaseObfuscator):
    def __init__(self, key: int = 42):
        self.key = key
    
    def obfuscate(self, code: str) -> str:
        if not code:
            return code
        return ''.join(chr(ord(c) ^ self.key) for c in code)
    
    def deobfuscate(self, code: str) -> str:
        return self.obfuscate(code)
