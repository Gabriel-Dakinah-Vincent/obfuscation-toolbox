import re
import random
import string
import keyword
import builtins
from obfuscation_toolit.core.base import BaseObfuscator


class VariableObfuscator(BaseObfuscator):
    def __init__(self, length: int = 8):
        if length < 1:
            raise ValueError("Length must be at least 1")
        self.length = length
        self.mapping = {}
        self.protected = set(keyword.kwlist) | set(dir(builtins))
    
    def obfuscate(self, code: str) -> str:
        if not code:
            return code
        words = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', code)
        
        for word in set(words):
            if word not in self.protected and word not in self.mapping:
                new_name = self._generate_name()
                self.mapping[word] = new_name
        
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
    
    def _generate_name(self) -> str:
        while True:
            name = '_' + ''.join(random.choices(string.ascii_letters + string.digits, k=self.length))
            if name not in self.mapping.values():
                return name
