import re
from obfuscation_toolit.core.base import BaseObfuscator


class MinifyObfuscator(BaseObfuscator):
    def obfuscate(self, code: str) -> str:
        if not code:
            return code
        lines = code.split('\n')
        result = []
        for line in lines:
            stripped = line.strip()
            if stripped and not stripped.startswith('#'):
                result.append(stripped)
        return ';'.join(result)
    
    def deobfuscate(self, code: str) -> str:
        if not code:
            return code
        return code.replace(';', '\n')
