# ⚡ online-c-compiler Docker Image

> Official containerized compilation sandbox and toolchain for **[onlineccompiler.com](https://onlineccompiler.com/)** — Fast, in-browser GCC C compiler, debugger, and memory visualization suite.

[![Docker Image](https://img.shields.io/badge/docker-momahdideveloper%2Fonline--c--compiler-blue.svg?style=for-the-badge&logo=docker)](https://hub.docker.com/)
[![Web IDE](https://img.shields.io/badge/Online%20IDE-onlineccompiler.com-blue?style=for-the-badge&logo=c)](https://onlineccompiler.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

A lightweight Alpine-based container packaging modern GCC, Clang, GDB, Valgrind, and build utilities matching the execution environment of [onlineccompiler.com](https://onlineccompiler.com/).

👉 **Try Web IDE without Docker**: [https://onlineccompiler.com/](https://onlineccompiler.com/)

---

## 🌐 Multilingual Web Portals

* 🇪🇸 **Español**: [Compilador de C Online](https://onlineccompiler.com/es/)
* 🇧🇷 **Português**: [Compilador C Online](https://onlineccompiler.com/pt/)
* 🇩🇪 **Deutsch**: [Online C Compiler](https://onlineccompiler.com/de/)
* 🇫🇷 **Français**: [Compilateur C en Ligne](https://onlineccompiler.com/fr/)

---

## 🚀 Quick Start

### Pull and Run
```bash
docker run -it --rm momahdideveloper/online-c-compiler:latest
```

### Mount Local Directory and Compile
```bash
docker run --rm -v $(pwd):/workspace momahdideveloper/online-c-compiler:latest gcc -O2 main.c -o app && ./app
```

---

## 🛠️ Toolchain Details

* **GCC**: Latest GNU Compiler Collection (C89, C99, C11, C17, C23)
* **Clang**: LLVM frontend with address sanitizer (`-fsanitize=address`)
* **GDB**: GNU Debugger for stack and heap trace analysis
* **Valgrind**: Memory leak profiling suite

---

## 🔗 Official Links

* **Cloud Web IDE**: [https://onlineccompiler.com/](https://onlineccompiler.com/)
* **GitHub Repository**: [MoMahdideveloper/online-c-compiler-suite](https://github.com/MoMahdideveloper/online-c-compiler-suite)
* **npm CLI**: [online-c-compiler on npm](https://www.npmjs.com/package/online-c-compiler)
* **PyPI Package**: [online-c-compiler on PyPI](https://pypi.org/project/online-c-compiler/)

---

## 📄 License

MIT License © 2026 Mahdi Hatefi ([onlineccompiler.com](https://onlineccompiler.com/))
