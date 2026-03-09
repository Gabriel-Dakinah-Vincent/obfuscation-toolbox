from typing import Dict, Type
from obfuscation_toolit.core.base import BaseObfuscator
from obfuscation_toolit.techniques import (
    StringObfuscator, VariableObfuscator, ControlFlowObfuscator, 
    HexObfuscator, CommentObfuscator, XorObfuscator, MinifyObfuscator,
    OpaquePredicateObfuscator, DeadCodeObfuscator, ArithmeticObfuscator,
    ClassRenameObfuscator, FunctionRenameObfuscator
)


OBFUSCATOR_REGISTRY: Dict[str, Type[BaseObfuscator]] = {
    'string': StringObfuscator,
    'variable': VariableObfuscator,
    'control_flow': ControlFlowObfuscator,
    'hex': HexObfuscator,
    'comment': CommentObfuscator,
    'xor': XorObfuscator,
    'minify': MinifyObfuscator,
    'opaque_predicate': OpaquePredicateObfuscator,
    'dead_code': DeadCodeObfuscator,
    'arithmetic': ArithmeticObfuscator,
    'class_rename': ClassRenameObfuscator,
    'function_rename': FunctionRenameObfuscator,
}
