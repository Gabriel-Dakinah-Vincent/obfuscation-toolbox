import argparse
from obfuscation_toolit.core.registry import OBFUSCATOR_REGISTRY
from obfuscation_toolit.obfuscate import obfuscate
from obfuscation_toolit.deobfuscate import deobfuscate


def main():
    parser = argparse.ArgumentParser(description='Python code obfuscation tool')
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # List command
    subparsers.add_parser('list', help='List available obfuscation methods')
    
    # Obfuscate command
    obf_parser = subparsers.add_parser('obfuscate', help='Obfuscate code')
    obf_parser.add_argument('method', help='Obfuscation method')
    obf_parser.add_argument('code', nargs='?', help='Code to obfuscate')
    obf_parser.add_argument('--input-file', help='Input file path')
    obf_parser.add_argument('--output-file', help='Output file path')
    obf_parser.add_argument('--in-place', action='store_true', help='Modify file in place')
    obf_parser.add_argument('--level', type=int, help='Obfuscation level (for string)')
    obf_parser.add_argument('--length', type=int, help='Variable name length (for variable/function/class)')
    obf_parser.add_argument('--complexity', type=int, help='Complexity level (for control_flow/opaque_predicate)')
    obf_parser.add_argument('--density', type=int, help='Comment density (for comment)')
    obf_parser.add_argument('--key', type=int, help='XOR key (for xor)')
    obf_parser.add_argument('--intensity', type=int, help='Dead code intensity (for dead_code)')
    
    # Deobfuscate command
    deobf_parser = subparsers.add_parser('deobfuscate', help='Deobfuscate code')
    deobf_parser.add_argument('method', help='Deobfuscation method')
    deobf_parser.add_argument('code', nargs='?', help='Code to deobfuscate')
    deobf_parser.add_argument('--input-file', help='Input file path')
    deobf_parser.add_argument('--output-file', help='Output file path')
    deobf_parser.add_argument('--in-place', action='store_true', help='Modify file in place')
    deobf_parser.add_argument('--level', type=int, help='Obfuscation level (for string)')
    deobf_parser.add_argument('--length', type=int, help='Variable name length (for variable/function/class)')
    deobf_parser.add_argument('--complexity', type=int, help='Complexity level (for control_flow/opaque_predicate)')
    deobf_parser.add_argument('--density', type=int, help='Comment density (for comment)')
    deobf_parser.add_argument('--key', type=int, help='XOR key (for xor)')
    deobf_parser.add_argument('--intensity', type=int, help='Dead code intensity (for dead_code)')
    
    args = parser.parse_args()
    
    if args.command == 'list':
        print("Available obfuscation methods:")
        for method in OBFUSCATOR_REGISTRY.keys():
            print(f"  - {method}")
        return
    
    if args.command in ['obfuscate', 'deobfuscate']:
        # Get code from file or argument
        if args.input_file:
            with open(args.input_file, 'r') as f:
                code = f.read()
        elif args.code:
            code = args.code
        else:
            print("Error: Provide either code argument or --input-file")
            return
        
        # Build params
        params = {}
        if args.level is not None:
            params['level'] = args.level
        if args.length is not None:
            params['length'] = args.length
        if args.complexity is not None:
            params['complexity'] = args.complexity
        if args.density is not None:
            params['density'] = args.density
        if args.key is not None:
            params['key'] = args.key
        if args.intensity is not None:
            params['intensity'] = args.intensity
        
        # Execute operation
        try:
            if args.command == 'obfuscate':
                result = obfuscate(args.method, code, **params)
            else:
                result = deobfuscate(args.method, code, **params)
            
            # Output result
            if args.output_file:
                with open(args.output_file, 'w') as f:
                    f.write(result)
                print(f"Result written to {args.output_file}")
            elif args.in_place and args.input_file:
                with open(args.input_file, 'w') as f:
                    f.write(result)
                print(f"File {args.input_file} modified in place")
            else:
                print(result)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    main()
