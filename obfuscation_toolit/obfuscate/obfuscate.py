from obfuscation_toolit.core.registry import OBFUSCATOR_REGISTRY


def obfuscate(method: str, code: str, **params) -> str:
    if not code:
        return code
    if method not in OBFUSCATOR_REGISTRY:
        available = ', '.join(OBFUSCATOR_REGISTRY.keys())
        raise ValueError(f"Unknown obfuscation method: {method}. Available: {available}")
    
    obfuscator_class = OBFUSCATOR_REGISTRY[method]
    obfuscator = obfuscator_class(**params)
    return obfuscator.obfuscate(code)
