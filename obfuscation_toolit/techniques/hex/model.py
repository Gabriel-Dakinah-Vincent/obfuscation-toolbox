from obfuscation_toolit.core.base import BaseObfuscator


class HexObfuscator(BaseObfuscator):
    def obfuscate(self, code: str) -> str:
        if not code:
            return code
        return code.encode('utf-8').hex()
    
    def deobfuscate(self, code: str) -> str:
        if not code:
            return code
        try:
            return bytes.fromhex(code).decode('utf-8')
        except (ValueError, UnicodeDecodeError) as e:
            raise ValueError(f"Invalid hex string: {e}")
