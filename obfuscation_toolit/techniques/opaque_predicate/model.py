import random
from obfuscation_toolit.core.base import BaseObfuscator


class OpaquePredicateObfuscator(BaseObfuscator):
    def __init__(self, complexity: int = 2):
        self.complexity = complexity
    
    def obfuscate(self, code: str) -> str:
        if not code:
            return code
        lines = code.split('\n')
        result = []
        
        for line in lines:
            if line.strip():
                for _ in range(self.complexity):
                    predicate = random.choice([
                        f"if (lambda: True)(): pass",
                        f"if 1 == 1: pass",
                        f"if [] == []: pass"
                    ])
                    result.append(predicate)
            result.append(line)
        
        return '\n'.join(result)
    
    def deobfuscate(self, code: str) -> str:
        if not code:
            return code
        lines = code.split('\n')
        return '\n'.join([l for l in lines if not (l.strip().startswith('if (lambda: True)():') or l.strip().startswith('if 1 == 1:') or l.strip().startswith('if [] == []:'))])
