import random
from obfuscation_toolit.core.base import BaseObfuscator


class CommentObfuscator(BaseObfuscator):
    def __init__(self, density: int = 2):
        if density < 1:
            raise ValueError("Density must be at least 1")
        self.density = density
        self.comments = [
            "# Processing data",
            "# Optimizing performance", 
            "# Validating input",
            "# Checking conditions",
            "# Executing logic"
        ]
    
    def obfuscate(self, code: str) -> str:
        if not code:
            return code
        lines = code.split('\n')
        result = []
        
        for line in lines:
            result.append(line)
            if line.strip() and not line.strip().startswith('#'):
                for _ in range(self.density):
                    result.append(random.choice(self.comments))
        
        return '\n'.join(result)
    
    def deobfuscate(self, code: str) -> str:
        if not code:
            return code
        lines = code.split('\n')
        return '\n'.join([line for line in lines if line.strip() not in self.comments])
