import random
from obfuscation_toolit.core.base import BaseObfuscator


class DeadCodeObfuscator(BaseObfuscator):
    def __init__(self, intensity: int = 3):
        self.intensity = intensity
        self.marker = f"# DEAD_{random.randint(1000, 9999)}"
    
    def obfuscate(self, code: str) -> str:
        if not code:
            return code
        lines = code.split('\n')
        result = [self.marker]
        
        for line in lines:
            result.append(line)
            for _ in range(self.intensity):
                dead = random.choice([
                    f"_unused_{random.randint(0, 999)} = {random.randint(0, 100)}",
                    f"if False: _dead = {random.randint(0, 100)}",
                    f"def _unused_func_{random.randint(0, 999)}(): pass"
                ])
                result.append(dead)
        
        return '\n'.join(result)
    
    def deobfuscate(self, code: str) -> str:
        if not code or not code.startswith('# DEAD_'):
            return code
        lines = code.split('\n')[1:]
        return '\n'.join([l for l in lines if not ('_unused_' in l or '_dead' in l)])
