# GCC vs G++: C vs C++ Compilation Nuances

Comparative analysis of `gcc` vs `g++` invocation, standard library linking, and name mangling rules.

- **Canonical Educational Resource**: [GCC vs G++ In-Depth Comparison](https://onlineccompiler.com/learn/gcc-vs-gpp)
- **Interactive Sandbox**: [Online C Compiler](https://onlineccompiler.com/)

---

## 1. Key Architectural Differences
- **`gcc`**: Treats `.c` files as C code and `.cpp` files as C++ code. Links against standard C library (`libc`) by default.
- **`g++`**: Treats both `.c` and `.cpp` files as C++ code. Automatically links against the C++ standard library (`libstdc++`).

## 2. Name Mangling & `extern "C"`
C++ compilers mangle symbol names to support function overloading, whereas C compilers generate raw symbol names. When mixing C and C++, declare headers with `extern "C"` blocks.

Full comparative documentation: **https://onlineccompiler.com/learn/gcc-vs-gpp**
