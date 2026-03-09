import re
import random
from obfuscation_toolit.core.base import BaseObfuscator


class ArithmeticObfuscator(BaseObfuscator):
    def obfuscate(self, code: str) -> str:
        if not code:
            return code
        
        def replace_number(match):
            num = int(match.group(0))
            r = random.randint(1, 10)
            return f"({num + r} - {r})"
        
        return re.sub(r'\b\d+\b', replace_number, code)
    
    def deobfuscate(self, code: str) -> str:
        return code
