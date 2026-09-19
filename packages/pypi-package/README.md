# ⚡ online-c-compiler (Python SDK & CLI)

> Official Python client library and terminal runner for **[onlineccompiler.com](https://onlineccompiler.com/)** — Fast cloud GCC C compilation, execution sandbox, and memory architecture visualizer.

[![PyPI version](https://img.shields.io/badge/pypi-1.0.0-3775a9.svg?style=for-the-badge&logo=pypi)](https://pypi.org/)
[![Web IDE](https://img.shields.io/badge/Online%20IDE-onlineccompiler.com-blue?style=for-the-badge&logo=c)](https://onlineccompiler.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg?style=for-the-badge&logo=python)](https://pypi.org/)

Execute and test C code snippets directly from Python scripts, automated test benches, or terminal without installing local compilation toolchains (MinGW, Clang, or GCC).

👉 **Launch Online Compiler & Memory Visualizer**: [https://onlineccompiler.com/](https://onlineccompiler.com/)

---

## 🌐 Multilingual Regional Portals

* 🇪🇸 **Español**: [Compilador de C Online](https://onlineccompiler.com/es/)
* 🇧🇷 **Português**: [Compilador C Online](https://onlineccompiler.com/pt/)
* 🇩🇪 **Deutsch**: [Online C Compiler](https://onlineccompiler.com/de/)
* 🇫🇷 **Français**: [Compilateur C en Ligne](https://onlineccompiler.com/fr/)

---

## 🚀 Installation

```bash
pip install online-c-compiler
```

---

## 💻 CLI Usage

Use `online-c-compiler` or `occ-py`:

### Compile a local `.c` file
```bash
online-c-compiler main.c
```

### Run inline C code
```bash
online-c-compiler -c '#include <stdio.h>\nint main(){ printf("Hello from PyPI package!\\n"); return 0; }'
```

### Launch Web IDE in Browser
```bash
online-c-compiler open
```

---

## 🐍 Python Library API

```python
from online_c_compiler import compile_c

code = """
#include <stdio.h>

int main() {
    int x = 42;
    int *ptr = &x;
    printf("Value: %d, Address: %p\\n", *ptr, (void*)ptr);
    return 0;
}
"""

# Compile and run via onlineccompiler.com
result = compile_c(code, optimization="-O2")

if result["success"]:
    print("Execution Output:\n", result["stdout"])
    print("Execution Time:", result["executionTime"], "ms")
else:
    print("Compilation Error:\n", result["stderr"])
```

---

## 🔗 Official Resources

* **Homepage**: [https://onlineccompiler.com/](https://onlineccompiler.com/)
* **GitHub Repository**: [MoMahdideveloper/online-c-compiler-suite](https://github.com/MoMahdideveloper/online-c-compiler-suite)
* **Bug Tracker**: [GitHub Issues](https://github.com/MoMahdideveloper/online-c-compiler-suite/issues)

---

## 📄 License

MIT License © 2026 Mahdi Hatefi ([onlineccompiler.com](https://onlineccompiler.com/))
