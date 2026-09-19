"""
CLI interface for online-c-compiler Python package
"""

import sys
import os
import webbrowser
import time

# Ensure safe UTF-8 output on Windows consoles
if sys.platform == "win32":
    try:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    except Exception:
        pass

from . import compile_c, __homepage__

BANNER = f"""\033[36m========================================================\033[0m
\033[1m\033[32m[+] online-c-compiler CLI (Python Edition)\033[0m
\033[90mPowered by onlineccompiler.com Cloud GCC Engine\033[0m
\033[36mWeb IDE:\033[0m \033[4m{__homepage__}\033[0m
\033[36m========================================================\033[0m
"""

def print_help():
    print(BANNER)
    print("Usage:")
    print("  online-c-compiler <file.c>       Compile and run a local C file")
    print("  online-c-compiler -c '<code>'    Compile inline C code")
    print("  online-c-compiler open           Open onlineccompiler.com in web browser")
    print("  online-c-compiler --help         Show this help message\n")
    print("Portals:")
    print("  English:    https://onlineccompiler.com/")
    print("  Español:    https://onlineccompiler.com/es/")
    print("  Português:  https://onlineccompiler.com/pt/")
    print("  Deutsch:    https://onlineccompiler.com/de/")
    print("  Français:   https://onlineccompiler.com/fr/")

def main():
    args = sys.argv[1:]
    if not args or "--help" in args or "-h" in args:
        print_help()
        sys.exit(0)
        
    if "open" in args:
        print(BANNER)
        print("Opening https://onlineccompiler.com/ in your browser...")
        webbrowser.open(__homepage__)
        sys.exit(0)
        
    code = ""
    if "-c" in args:
        idx = args.index("-c")
        if idx + 1 < len(args):
            code = args[idx + 1]
    else:
        file_path = args[0]
        if not os.path.isfile(file_path):
            print(f"\033[31mError: File not found: {file_path}\033[0m", file=sys.stderr)
            sys.exit(1)
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
            
    print(BANNER)
    print("Compiling via GCC cloud engine on onlineccompiler.com...")
    t0 = time.time()
    try:
        res = compile_c(code)
        elapsed = int((time.time() - t0) * 1000)
        if res.get("success"):
            print(f"\033[32m[OK] Execution Succeeded ({elapsed}ms | Engine: {res.get('engine', 'GCC')})\033[0m\n")
            print("--- Standard Output ---")
            print(res.get("stdout", "(no output)"))
            if res.get("stderr"):
                print("\n--- Compiler Warnings ---")
                print(f"\033[33m{res.get('stderr')}\033[0m")
        else:
            print("\033[31m[FAIL] Compilation/Execution Failed\033[0m\n")
            if res.get("stderr"):
                print("--- Compiler Errors ---")
                print(f"\033[31m{res.get('stderr')}\033[0m")
            if res.get("stdout"):
                print("--- Output ---")
                print(res.get("stdout"))
                
        print("\n\033[90mInspect memory visuals & AST at: https://onlineccompiler.com/\033[0m")
    except Exception as e:
        print(f"\033[31mError: {e}\033[0m", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
