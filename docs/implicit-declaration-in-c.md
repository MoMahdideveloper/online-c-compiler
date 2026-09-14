# Fixing 'implicit declaration of function' in C

Understanding ISO C function prototyping and resolving implicit declaration warnings and compiler errors.

- **Canonical Troubleshooting Resource**: [Fixing 'implicit declaration of function' in C](https://onlineccompiler.com/errors/implicit-declaration-in-c)
- **Interactive Cloud IDE**: [Online C Compiler](https://onlineccompiler.com/)

---

## 1. Why Modern C Forbids Implicit Declarations
In legacy K&R C, calling an undeclared function defaulted to returning an `int`. Since ISO C99, C11, and C23, implicit declarations are strictly prohibited. In modern GCC/Clang, this triggers a compiler warning or fatal error (`-Werror=implicit-function-declaration`).

## 2. Diagnostic Steps
1. **Standard Library Headers**: If calling `printf`, include `<stdio.h>`. If calling `malloc` or `exit`, include `<stdlib.h>`.
2. **Forward Declarations**: Declare function prototypes before `main()` if defining function bodies later in the file.

Read the complete guide at: **https://onlineccompiler.com/errors/implicit-declaration-in-c**
