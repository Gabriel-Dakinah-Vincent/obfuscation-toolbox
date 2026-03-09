import random
from obfuscation_toolit.core.base import BaseObfuscator


class ControlFlowObfuscator(BaseObfuscator):
    def __init__(self, complexity: int = 1):
        if complexity < 1:
            raise ValueError("Complexity must be at least 1")
        self.complexity = complexity
        self.marker = f"# OBFUSCATED_CF_{random.randint(1000, 9999)}"
    
    def obfuscate(self, code: str) -> str:
        if not code:
            return code
        lines = code.split('\n')
        result = [self.marker]
        
        for line in lines:
            result.append(line)
            indent = len(line) - len(line.lstrip())
            indent_str = ' ' * indent
            
            for _ in range(self.complexity):
                dummy = random.choice([
                    f"{indent_str}if {random.choice(['True', 'False'])}: pass",
                    f"{indent_str}_ = {random.randint(0, 100)}",
                    f"{indent_str}__ = None",
                    f"{indent_str}pass if {random.choice(['True', 'False'])} else None"
                ])
                result.append(dummy)
        
        return '\n'.join(result)
    
    def deobfuscate(self, code: str) -> str:
        if not code or not code.startswith('# OBFUSCATED_CF_'):
            return code
        
        lines = code.split('\n')[1:]
        result = []
        
        for line in lines:
            stripped = line.lstrip()
            if not (stripped.startswith('if True: pass') or 
                    stripped.startswith('if False: pass') or 
                    stripped.startswith('_ = ') or
                    stripped.startswith('__ = None') or
                    stripped.startswith('pass if')):
                result.append(line)
        
        return '\n'.join(result)
