import re
import random
import string
import keyword
from obfuscation_toolit.core.base import BaseObfuscator


class FunctionRenameObfuscator(BaseObfuscator):
    def __init__(self, length: int = 10):
        self.length = length
        self.mapping = {}
        self.protected = set(keyword.kwlist) | {'__init__', '__str__', '__repr__', '__main__'}
    
    def obfuscate(self, code: str) -> str:
        if not code:
            return code
        
        func_pattern = r'\bdef\s+([a-zA-Z_][a-zA-Z0-9_]*)\b'
        functions = re.findall(func_pattern, code)
        
        for func in set(functions):
            if func not in self.protected and func not in self.mapping:
                self.mapping[func] = '_f' + ''.join(random.choices(string.ascii_letters + string.digits, k=self.length))
        
        result = code
        for original, obfuscated in sorted(self.mapping.items(), key=lambda x: len(x[0]), reverse=True):
            result = re.sub(r'\b' + re.escape(original) + r'\b', obfuscated, result)
        
        return result
    
    def deobfuscate(self, code: str) -> str:
        if not code:
            return code
        result = code
        for original, obfuscated in sorted(self.mapping.items(), key=lambda x: len(x[1]), reverse=True):
            result = re.sub(r'\b' + re.escape(obfuscated) + r'\b', original, result)
        return result
