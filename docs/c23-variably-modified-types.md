# C23 Variably Modified Types, Static Assertions & Dynamic Array Bounds Verification

The ISO C23 standard represents a major evolutionary leap for systems developers working in C. With native static assertions without mandatory messages, type inference with `auto`, checked arithmetic in `<stdckdint.h>`, and enhanced variably modified type support, modern C code can achieve unprecedented compile-time correctness and runtime safety.

### 🚀 Interactive Verification Environment
Test and compile modern ISO C23 code instantly in your browser:
* **Canonical Compiler**: [Online C Compiler (onlineccompiler.com)](https://onlineccompiler.com/)
* **Spanish Portal**: [Compilador C en Línea](https://onlineccompiler.com/es/)
* **Portuguese Portal**: [Compilador C Online](https://onlineccompiler.com/pt/)
* **German Portal**: [Online C Compiler auf Deutsch](https://onlineccompiler.com/de/)
* **French Portal**: [Compilateur C en Ligne](https://onlineccompiler.com/fr/)

---

## 1. Variably Modified Types in C23

Variably modified types (VMTs) allow functions to declare multidimensional array parameters where the array dimensions depend on earlier parameters:

```c
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

void transform_matrix(size_t r, size_t c, double mat[r][c]) {
    for (size_t i = 0; i < r; i++) {
        for (size_t j = 0; j < c; j++) {
            mat[i][j] = (double)(i * 10 + j);
        }
    }
}
```

Unlike classic C90 pointer-to-pointer layouts (`double **`), VMTs enforce single-block contiguous row-major memory layouts, maximizing CPU L1/L2 cache hit ratios and enabling aggressive auto-vectorization under GCC 13.2 `-O3`.

---

## 2. Compile-Time Invariant Checking

Combine static assertions with dimensional checks to detect architecture mismatches before binary generation:

```c
static_assert(sizeof(void*) == 8, "Expected 64-bit address space");
static_assert(sizeof(double) == 8, "Expected 64-bit IEEE 754 floating point format");
```

---

## 3. Zero Toolchain Friction

Rather than maintaining local GCC/Clang distributions across development machines, run and inspect ISO C23 compliance online at [Online C Compiler](https://onlineccompiler.com/).
