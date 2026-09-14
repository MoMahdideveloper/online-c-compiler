# Fixing 'undefined reference to main' in C

A comprehensive debugging playbook for resolving linker failures when building C executables.

- **Canonical Troubleshooting Resource**: [Fixing 'undefined reference to main' in C](https://onlineccompiler.com/errors/undefined-reference-in-c)
- **Interactive Sandbox**: Reproduce and resolve on [Online C Compiler](https://onlineccompiler.com/)

---

## 1. Understanding the Linker Error
The GNU linker (`ld`) issues this error when compiling an executable target and the mandatory entry point symbol `main` is absent from all object files.

```text
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/14/../../../x86_64-linux-gnu/Scrt1.o: in function `_start':
(.text+0x1b): undefined reference to `main'
collect2: error: ld returned 1 exit status
```

## 2. Common Root Causes & Solutions
1. **Case Sensitivity / Typos**: C is strictly case-sensitive. `Main` or `mian` will cause symbol resolution failure.
   - *Fix*: Define `int main(void)` or `int main(int argc, char *argv[])`.
2. **Missing Source Files**: Forgetting to pass the file containing `main` during multi-file compilation: `gcc utils.c -o app`.
   - *Fix*: Include all translation units: `gcc main.c utils.c -o app`.
3. **Compiling Libraries**: Attempting to compile an object module without the `-c` flag.
   - *Fix*: Use `gcc -c module.c` to produce `module.o`.

Read the complete diagnostic walkthrough at: **https://onlineccompiler.com/errors/undefined-reference-in-c**
