import re
import random
import string
from obfuscation_toolit.core.base import BaseObfuscator


class ClassRenameObfuscator(BaseObfuscator):
    def __init__(self, length: int = 10):
        self.length = length
        self.mapping = {}
    
    def obfuscate(self, code: str) -> str:
        if not code:
            return code
        
        class_pattern = r'\bclass\s+([A-Z][a-zA-Z0-9_]*)\b'
        classes = re.findall(class_pattern, code)
        
        for cls in set(classes):
            if cls not in self.mapping:
                self.mapping[cls] = '_C' + ''.join(random.choices(string.ascii_letters + string.digits, k=self.length))
        
        result = code
        for original, obfuscated in self.mapping.items():
            result = re.sub(r'\b' + re.escape(original) + r'\b', obfuscated, result)
        
        return result
    
    def deobfuscate(self, code: str) -> str:
        if not code:
            return code
        result = code
        for original, obfuscated in self.mapping.items():
            result = re.sub(r'\b' + re.escape(obfuscated) + r'\b', original, result)
        return result
